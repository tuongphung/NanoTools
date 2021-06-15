#!/usr/bin/env python
from tqdm import tqdm
import ROOT as r
import os
from sys import exit
import numpy as np
from array import array
from bisect import bisect
from glob import glob 
from fake_rates import fake_rate

    
def choose_pair(true_tight_idxs, fake_loose_idxs, fake_tight_idxs):
    if true_tight_idxs[11]:
	if fake_tight_idxs[11]:
	    return 11, true_tight_idxs[11][0], 11, fake_tight_idxs[11][0], "sr", "ee"
	elif fake_tight_idxs[13]:
	    return 11, true_tight_idxs[11][0], 13, fake_tight_idxs[13][0], "sr", "em"
	elif fake_loose_idxs[11]:
	    return 11, true_tight_idxs[11][0], 11, fake_loose_idxs[11][0], "cr", "ee"
	elif fake_loose_idxs[13]:
	    return 11, true_tight_idxs[11][0], 13, fake_loose_idxs[13][0], "cr", "em"
    elif true_tight_idxs[13]:
	if fake_tight_idxs[11]:
	    return 13, true_tight_idxs[13][0], 11, fake_tight_idxs[11][0], "sr", "me"
	elif fake_tight_idxs[13]:
	    return 13, true_tight_idxs[13][0], 13, fake_tight_idxs[13][0], "sr", "mm"
	elif fake_loose_idxs[11]:
	    return 13, true_tight_idxs[13][0], 11, fake_loose_idxs[11][0], "cr", "me"
	elif fake_loose_idxs[13]:
	    return 13, true_tight_idxs[13][0], 13, fake_loose_idxs[13][0], "cr", "mm"
    elif true_tight_idxs[-11]:
	if fake_tight_idxs[-11]:
	    return -11, true_tight_idxs[-11][0], -11, fake_tight_idxs[-11][0], "sr", "ee"
	elif fake_tight_idxs[-13]:
	    return -11, true_tight_idxs[-11][0], -13, fake_tight_idxs[-13][0], "sr", "em"
	elif fake_loose_idxs[-11]:
	    return -11, true_tight_idxs[-11][0], -11, fake_loose_idxs[-11][0], "cr", "ee"
	elif fake_loose_idxs[-13]:
	    return -11, true_tight_idxs[-11][0], -13, fake_loose_idxs[-13][0], "cr", "em"
    elif true_tight_idxs[-13]:
	if fake_tight_idxs[-11]:
	    return -13, true_tight_idxs[-13][0], -11, fake_tight_idxs[-11][0], "sr", "me"
	elif fake_tight_idxs[-13]:
	    return -13, true_tight_idxs[-13][0], -13, fake_tight_idxs[-13][0], "sr", "mm"
	elif fake_loose_idxs[-11]:
	    return -13, true_tight_idxs[-13][0], -11, fake_loose_idxs[-11][0], "cr", "me"
	elif fake_loose_idxs[-13]:
	    return -13, true_tight_idxs[-13][0], -13, fake_loose_idxs[-13][0], "cr", "mm"
    else:
	return False


def clean(jet_idxs, lep_id, lep_idx):
    lep = r.TLorentzVector(0,0,0,0)
    if abs(lep_id) == 11:
	lep.SetPtEtaPhiM(nt.Electron_pt()[lep_idx], nt.Electron_eta()[lep_idx], nt.Electron_phi()[lep_idx], nt.Electron_mass()[lep_idx])
    if abs(lep_id) == 13:
	lep.SetPtEtaPhiM(nt.Muon_pt()[lep_idx], nt.Muon_eta()[lep_idx], nt.Muon_phi()[lep_idx], nt.Muon_mass()[lep_idx])
    candidates = []
    for jet_idx in jet_idxs:
	jet = r.TLorentzVector(0,0,0,0)
	jet.SetPtEtaPhiM(nt.Jet_pt()[jet_idx], nt.Jet_eta()[jet_idx], nt.Jet_phi()[jet_idx], nt.Jet_mass()[jet_idx])
	deltaR = lep.DeltaR(jet) 
	if deltaR < 0.4:
	    candidates.append((deltaR, jet_idx))
    if candidates:
	return {sorted(candidates)[0][1]}
    else:
	return set()


def process_event(ievent, d):	
    nt.GetEntry(ievent)

    # IDfakable = 2, IDtight = 4
    true_tight_idxs = {key: [] for key in [-13, -11, 11, 13]}
    fake_loose_idxs = {key: [] for key in [-13, -11, 11, 13]}
    fake_tight_idxs = {key: [] for key in [-13, -11, 11, 13]}

    for idx, pt in enumerate(nt.Electron_pt()):
	if SS.electronID(idx, 2, year):
	    pdgId = nt.Electron_pdgId()[idx]
	    genPartFlav = nt.Electron_genPartFlav()[idx] 
	    fake = (genPartFlav != '\x01' and genPartFlav != '\x0f')
	    if fake:
		fake_loose_idxs[pdgId].append(idx)
	    if SS.electronID(idx, 4, year):
	        if fake:
		    fake_tight_idxs[pdgId].append(idx)
		else:
		    true_tight_idxs[pdgId].append(idx)

    for idx, pt in enumerate(nt.Muon_pt()):
	if SS.muonID(idx, 2, year):
	    pdgId = nt.Muon_pdgId()[idx]
	    genPartFlav = nt.Muon_genPartFlav()[idx] 
	    fake = (genPartFlav != '\x01' and genPartFlav != '\x0f')
	    if fake:
		fake_loose_idxs[pdgId].append(idx)
	    if SS.muonID(idx, 4, year):
	        if fake:
		    fake_tight_idxs[pdgId].append(idx)
		else:
		    true_tight_idxs[pdgId].append(idx)

    pair = choose_pair(true_tight_idxs, fake_loose_idxs, fake_tight_idxs)
    if not pair:
	return
    else:
	true_id, true_idx, fake_id, fake_idx, region, leps = pair

    jet_idxs = {i for i in range(len(nt.Jet_pt()))}
    jet_idxs -= clean(jet_idxs, true_id, true_idx)
    jet_idxs -= clean(jet_idxs, fake_id, fake_idx)
    nclean_jets = 0
    for idx in jet_idxs:
        if nt.Jet_pt()[idx] > 40 and abs(nt.Jet_eta()[idx]) < 2.4:
            nclean_jets += 1

    if nclean_jets >= 2:
        if region == "cr":
	    d[leps][region] += 1
	    ccpt = r.coneCorrPt(fake_id, fake_idx, *iso_wps[(year, abs(fake_id))])
	    if abs(fake_id) == 11:
	        eta = nt.Electron_eta()[fake_idx]
	    elif abs(fake_id) == 13:
	        eta = nt.Muon_eta()[fake_idx]	
	    fr = fake_rate(year, fake_id, ccpt, eta)
	    d[leps]["sr_estimate"] += fr/(1-fr) 
        elif region == "sr":
	    d[leps][region] += 1
    	
    return


r.gSystem.Load('../NanoCORE/NANO_CORE.so')
for include in ["Nano.cc", "SSSelections.cc", "ElectronSelections.cc", "MuonSelections.cc", "IsolationTools.cc"]: 
    r.gInterpreter.ProcessLine('#include "../NanoCORE/%s"' % include)

# CORE functions will be ROOT object members after we gSystem.Load CORE
from ROOT import nt, gconf, SS

path = {2016: "/hadoop/cms/store/user/ksalyer/FCNC_NanoSkim/fcnc_v3/TTJets_TuneCUETP8M2T4_13TeV-amcatnloFXFX-pythia8_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1_NANOAODSIM_fcnc_v3/",
	2017: "/hadoop/cms/store/user/ksalyer/FCNC_NanoSkim/fcnc_v3/TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8_RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_new_pmx_102X_mc2017_realistic_v8-v1_NANOAODSIM_fcnc_v3/",
	2018: "/hadoop/cms/store/user/ksalyer/FCNC_NanoSkim/fcnc_v3/TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8_RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext2-v1_NANOAODSIM_fcnc_v3/"}

iso_wps = {(2016, 11): (0.12, 0.80, 7.2),
	   (2016, 13): (0.16, 0.76, 7.2),
	   (2017, 11): (0.07, 0.78, 8.0),
	   (2017, 13): (0.11, 0.74, 6.8),
	   (2018, 11): (0.07, 0.78, 8.0),
	   (2018, 13): (0.11, 0.74, 6.8)}

for year in [2016, 2017, 2018]:
    gconf.year = year
    d = {key: {key2: 0 for key2 in ["cr", "sr_estimate", "sr"]} for key in ["ee", "mm", "me","em"]}
    total_events = 0

    ch = r.TChain("Events")
    for sample in glob(path[year]+"*.root"):
        ch.Add("file://" + sample)

    elements = list(ch.GetListOfFiles())
    treename = ch.GetName()
    element = elements[0]
    for i, element in enumerate(elements):
        tfile = r.TFile.Open(element.GetTitle())
        tree = tfile.Get(treename)
        nt.Init(tree)
        total_events += tree.GetEntries()
        for ievent in tqdm(range(tree.GetEntries())):
	    process_event(ievent, d)
	print "{}: processed file {} out of {}".format(year, i+1, len(elements))

    print "{}: {} total events".format(year, total_events)
    for leps in d:
	for region in ["cr", "sr_estimate", "sr"]:
	    print "{0}, {1}: {2:.2f}".format(leps, region, d[leps][region])

