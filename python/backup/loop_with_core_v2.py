#!/usr/bin/env python
from tqdm import tqdm
import ROOT as r
import os
from sys import exit
import numpy as np
from array import array
from bisect import bisect

ch = r.TChain("Events")
#ch.Add("file:///home/users/tuongphung21/qcd_pt300-470_RunIISummer16NanoAODv7.root");
ch.Add("root://xcache-redirector.t2.ucsd.edu:2040//store/mc/RunIIFall17NanoAODv7/QCD_Pt-300to470_MuEnrichedPt5_TuneCP5_13TeV_pythia8/NANOAODSIM/PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/*");
#ch.Add("/hadoop/cms/phedex/store/mc/RunIIAutumn18NanoAODv7/QCD_Pt-120to170_MuEnrichedPt5_TuneCP5_13TeV_pythia8/NANOAODSIM/Nano02Apr2020_102X_upgrade2018_realistic_v21-v1/70000/DE335891-829A-B943-99BE-E5A179F5F3EB.root");


r.gSystem.Load('../NanoCORE/NANO_CORE.so')
for include in ["Nano.cc", "SSSelections.cc", "ElectronSelections.cc", "MuonSelections.cc", "IsolationTools.cc"]: 
    r.gInterpreter.ProcessLine('#include "../NanoCORE/%s"' % include)

# CORE functions will be ROOT object members after we gSystem.Load CORE
from ROOT import nt, gconf, SS

year = 2016
gconf.year = year

nt.Init(ch)

ele_x_bins = {2016: [25, 35, 50], 2017: [25, 35, 50, 70], 2018: [25, 35, 50, 70]}
muon_x_bins = {2016: [15, 25, 35, 50], 2017: [20, 25, 35, 50, 70], 2018: [20, 25, 35, 50, 70]}
ele_y_bins = [0, 0.8, 1.479, 2.5]
muon_y_bins = [0, 1.2, 2.1, 2.4]
n_xbins = len(x_bins)
n_ybins = len(y_bins)
h_denom   = r.TH2F("denom", "Denominator Selection", len(x_bins)-1, array('f', x_bins), len(y_bins)-1, array('f', y_bins))
h_numer   = r.TH2F("numer", "Numerator Selection", len(x_bins)-1, array('f', x_bins), len(y_bins)-1, array('f', y_bins))
h_fr   = r.TH2F("fr", "fr", len(x_bins)-1, array('f', x_bins), len(y_bins)-1, array('f', y_bins))

def process_event(ievent):
	
    nt.GetEntry(ievent)

    # one and only one electron/muon passing the loose (denominator) selection
    # IDfakable = 2, IDtight = 4
    nloose = 0
    tight = False

    for idx, pt in enumerate(nt.Electron_pt()):
	if SS.electronID(idx, 2, year):
	    nloose += 1
	    if SS.electronID(idx, 4, year):
		tight = True
	    lep = r.TLorentzVector(0,0,0,0)
	    lep.SetPtEtaPhiM(pt, nt.Electron_eta()[idx], nt.Electron_phi()[idx], nt.Electron_mass()[idx])
	    #lep.SetPtEtaPhiM(pt, nt.Electron_eta(idx), nt.Electron_phi(idx), nt.Electron_mass(idx))

    for idx, pt in enumerate(nt.Muon_pt()):
	if SS.muonID(idx, 2, year):
    	    nloose += 1
	    lep_idx = idx
	    if SS.muonID(idx, 4, year):
		tight = True
	    lep = r.TLorentzVector(0,0,0,0)
	    lep.SetPtEtaPhiM(pt, nt.Muon_eta()[idx], nt.Muon_phi()[idx], nt.Muon_mass()[idx])
    
    if nloose == 1:
	
	ccpt = r.coneCorrPt(nt.Muon_pdgId()[lep_idx], lep_idx, 0.11, 0.74, 6.8)
	eta = lep.Eta()
	
	# at least one jet separated from the lepton by deltaR > 1
	passed = False
	for idx, pt in enumerate(nt.Jet_pt()):
	    jet = r.TLorentzVector(0,0,0,0)
	    jet.SetPtEtaPhiM(pt, nt.Jet_eta()[idx], nt.Jet_phi()[idx], nt.Jet_mass()[idx])
	    #jet.SetPtEtaPhiM(pt, nt.Jet_eta(idx), nt.Jet_phi(idx), nt.Jet_mass(idx))
	    if lep.DeltaR(jet) > 1:
		passed = True	   
		break
	if not passed:
	    return	

	# met < 20
	met = nt.MET_pt()
	if met >= 20:
	    return

	# mt(lepton, met) < 20
	mt = np.sqrt(2*lep.Pt()*met*(1-np.cos(lep.Phi()-nt.MET_phi())))
	if mt >= 20:
	    return
    	
	#if nt.event() == 6886009:
	#    print lep.Pt(), ccpt, eta, nt.Muon_dz()[lep_idx], nt.Muon_dxy()[lep_idx], nt.Muon_ptErr()[lep_idx]/nt.Muon_pt()[lep_idx], nt.Muon_miniPFRelIso_all()[lep_idx], nt.event(), met, mt 
	
	h_denom.Fill(ccpt, eta)
	gen_ids.append(nt.GenPart_pdgId()[nt.Muon_genPartIdx()[lep_idx]])
	if tight:
	    h_numer.Fill(ccpt, eta)
    	    #if x_bins[0] < ccpt < x_bins[-1] and y_bins[0] < eta < y_bins[-1]:
	    #    bin_content[get_bin_num(ccpt, eta)].append((round(ccpt, 3), round(eta, 3), nt.event()))
    return


for ievent in tqdm(range(ch.GetEntries())):
#for ievent in tqdm(range(20000)):
    process_event(ievent)

#print(h1.GetMean())

hist_pixel_x = 600
hist_pixel_y = 450
num_hist_x = 1
num_hist_y = 3
c = r.TCanvas("fake_rate", "Muon Fake Rate", hist_pixel_x * num_hist_x, hist_pixel_y * num_hist_y)
c.Divide(num_hist_x, num_hist_y)
r.gStyle.SetOptStat("ne")
#c.SetLogy()

c.cd(1)
h_numer.GetXaxis().SetTitle("cone corr p_{T} [GeV]")
h_numer.GetYaxis().SetTitle("|\eta|")
h_numer.SetMarkerSize(2.5)
h_numer.Draw("COLZ TEXT")

c.cd(2)
h_denom.GetXaxis().SetTitle("cone corr p_{T} [GeV]")
h_denom.GetYaxis().SetTitle("|\eta|")
h_denom.SetMarkerSize(2.5)
h_denom.Draw("COLZ TEXT")

c.cd(3)
h_fr = h_numer.Clone()
h_fr.SetTitle("Muon Fake Rate")
h_fr.SetName("fake_rate")
h_fr.Divide(h_denom)
stats = h_fr.GetListOfFunctions().FindObject("stats")
h_fr.SetMarkerSize(2.5)
h_fr.Draw("COLZ TEXT45")

#for i in range(1, n_xbins):
#    for j in range(1, n_ybins):
#	print (i, j), sorted(bin_content[(i,j)])

#print h_denom.GetBinContent(1, 1)

print sorted(gen_ids)

c.SaveAs("plots/fake_rate.pdf")


os.system("niceplots plots muon_fr")

#os.system("which ic && ic plot.pdf")
