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


def process_event(ievent, d):	
    nt.GetEntry(ievent)

    # IDfakable = 2, IDtight = 4
    true_t = 0
    fake_lnott = 0
    fake_t = 0
    pos_eles = []
    neg_eles = []
    pos_muons = []
    neg_muons = []

    for idx, pt in enumerate(nt.Electron_pt()):
	loose = False
	tight = False
	if SS.electronID(idx, 2, year):
	    loose = True
	    if SS.electronID(idx, 4, year):
		tight = True
	genPartFlav = nt.Electron_genPartFlav()[idx] 
	fake = (genPartFlav != '\x01' and genPartFlav != '\x0f')
	if not fake and tight:
	    true_t += 1	
	elif fake and loose:
	    fake_pdgId = nt.Electron_pdgId()[idx]
	    fake_idx = idx
	    if tight:
		fake_t += 1
	    else:
		fake_lnott += 1
	
    for idx, pt in enumerate(nt.Muon_pt()):
	loose = False
	tight = False
	if SS.muonID(idx, 2, year):
	    loose = True	    
	    if SS.muonID(idx, 4, year):
	        tight = True
	genPartFlav = nt.Muon_genPartFlav()[idx]
	fake = (genPartFlav != '\x01' and genPartFlav != '\x0f')
	if not fake and tight:
	    true_t += 1	
	elif fake and loose:
	    fake_pdgId = nt.Muon_pdgId()[idx]
	    fake_idx = idx
	    if tight:
		fake_t += 1
	    else:
		fake_lnott += 1	

    if true_t == 1 and fake_t == 1 and fake_lnott == 0:
	if abs(fake_pdgId) == 11:
	    d["sr_ele"] += 1
	elif abs(fake_pdgId) == 13:
	    d["sr_muon"] += 1
	
    elif true_t == 1 and fake_lnott == 1 and fake_t == 0:
	ccpt = r.coneCorrPt(fake_pdgId, fake_idx, *iso_wps[(year, abs(fake_pdgId))])
	if abs(fake_pdgId) == 11:
	    eta = nt.Electron_eta()[fake_idx]
	elif abs(fake_pdgId) == 13:
	    eta = nt.Muon_eta()[fake_idx]	
	fr = fake_rate(year, fake_pdgId, ccpt, eta)
	
	if abs(fake_pdgId) == 11:
	    d["cr_ele"] += 1
	    d["sr_ele_estimate"] += fr/(1-fr)
	elif abs(fake_pdgId) == 13:
	    d["cr_muon"] += 1
	    d["sr_muon_estimate"] += fr/(1-fr)
    	
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
    d = {s: 0 for s in ["cr_ele", "cr_muon", "sr_ele", "sr_muon", "sr_ele_estimate", "sr_muon_estimate"]}
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
	print str(year) + ": processed file " + str(i+1) + " out of " + str(len(elements))

    print str(year) + ": " + str(total_events) + " total events"
    print d

