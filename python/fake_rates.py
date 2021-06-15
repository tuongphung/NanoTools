def fake_rate(year, pdgId, ccpt, eta):
    if year == 2016:
	if abs(pdgId) == 11:
	    return electronQCDMCFakeRate_IsoTrigs_legacy_2016(ccpt, eta)
	if abs(pdgId) == 13:
	    return muonQCDMCFakeRate_IsoTrigs_legacy_2016(ccpt, eta)
    elif year == 2017:
	if abs(pdgId) == 11:
	    return electronQCDMCFakeRate_IsoTrigs_2017(ccpt, eta)
	if abs(pdgId) == 13:
	    return muonQCDMCFakeRate_IsoTrigs_2017(ccpt, eta)
    elif year == 2018:
	if abs(pdgId) == 11:
	    return electronQCDMCFakeRate_IsoTrigs_2018(ccpt, eta)
	if abs(pdgId) == 13:
	    return muonQCDMCFakeRate_IsoTrigs_2018(ccpt, eta)
    raise Exception('Invalid year or particle id')

def electronQCDMCFakeRate_IsoTrigs_legacy_2016(pt, eta):
    if (pt>=10 and pt<15 and abs(eta)>=0.000 and abs(eta)<0.800): return 0.0000 # +-0.0%
    if (pt>=10 and pt<15 and abs(eta)>=0.800 and abs(eta)<1.479): return 0.0000 # +-0.0%
    if (pt>=10 and pt<15 and abs(eta)>=1.479 and abs(eta)<2.500): return 0.0000 # +-0.0%
    if (pt>=15 and pt<20 and abs(eta)>=0.000 and abs(eta)<0.800): return 0.3789 # +-3.0%
    if (pt>=15 and pt<20 and abs(eta)>=0.800 and abs(eta)<1.479): return 0.3942 # +-4.0%
    if (pt>=15 and pt<20 and abs(eta)>=1.479 and abs(eta)<2.500): return 0.4086 # +-6.1%
    if (pt>=20 and pt<25 and abs(eta)>=0.000 and abs(eta)<0.800): return 0.1643 # +-7.3%
    if (pt>=20 and pt<25 and abs(eta)>=0.800 and abs(eta)<1.479): return 0.1805 # +-10.3%
    if (pt>=20 and pt<25 and abs(eta)>=1.479 and abs(eta)<2.500): return 0.1628 # +-10.3%
    if (pt>=25 and pt<35 and abs(eta)>=0.000 and abs(eta)<0.800): return 0.1226 # +-8.6%
    if (pt>=25 and pt<35 and abs(eta)>=0.800 and abs(eta)<1.479): return 0.1298 # +-10.5%
    if (pt>=25 and pt<35 and abs(eta)>=1.479 and abs(eta)<2.500): return 0.1335 # +-10.7%
    if (pt>=35 and pt<50 and abs(eta)>=0.000 and abs(eta)<0.800): return 0.1568 # +-15.3%
    if (pt>=35 and pt<50 and abs(eta)>=0.800 and abs(eta)<1.479): return 0.1756 # +-14.7%
    if (pt>=35 and pt<50 and abs(eta)>=1.479 and abs(eta)<2.500): return 0.1381 # +-11.4%
    if (pt>=50 and pt<70 and abs(eta)>=0.000 and abs(eta)<0.800): return 0.2846 # +-17.2%
    if (pt>=50 and pt<70 and abs(eta)>=0.800 and abs(eta)<1.479): return 0.1756 # +-20.7%
    if (pt>=50 and pt<70 and abs(eta)>=1.479 and abs(eta)<2.500): return 0.2120 # +-15.1%
    if (pt>=70 and abs(eta)>=0.000 and abs(eta)<0.800): return 0.2561 # +-25.1%
    if (pt>=70 and abs(eta)>=0.800 and abs(eta)<1.479): return 0.2018 # +-14.6%
    if (pt>=70 and abs(eta)>=1.479 and abs(eta)<2.500): return 0.3416 # +-13.2%
    return 0.

def muonQCDMCFakeRate_IsoTrigs_legacy_2016(pt, eta):
    if (pt>=10 and pt<15 and abs(eta)>=0.000 and abs(eta)<1.200): return 0.3940 # +-1.1%
    if (pt>=10 and pt<15 and abs(eta)>=1.200 and abs(eta)<2.100): return 0.4297 # +-1.3%
    if (pt>=10 and pt<15 and abs(eta)>=2.100 and abs(eta)<2.400): return 0.4809 # +-2.1%
    if (pt>=15 and pt<20 and abs(eta)>=0.000 and abs(eta)<1.200): return 0.1301 # +-1.4%
    if (pt>=15 and pt<20 and abs(eta)>=1.200 and abs(eta)<2.100): return 0.1486 # +-1.7%
    if (pt>=15 and pt<20 and abs(eta)>=2.100 and abs(eta)<2.400): return 0.1959 # +-2.8%
    if (pt>=20 and pt<25 and abs(eta)>=0.000 and abs(eta)<1.200): return 0.0885 # +-2.0%
    if (pt>=20 and pt<25 and abs(eta)>=1.200 and abs(eta)<2.100): return 0.0979 # +-2.4%
    if (pt>=20 and pt<25 and abs(eta)>=2.100 and abs(eta)<2.400): return 0.1375 # +-4.0%
    if (pt>=25 and pt<35 and abs(eta)>=0.000 and abs(eta)<1.200): return 0.0805 # +-2.3%
    if (pt>=25 and pt<35 and abs(eta)>=1.200 and abs(eta)<2.100): return 0.0878 # +-2.7%
    if (pt>=25 and pt<35 and abs(eta)>=2.100 and abs(eta)<2.400): return 0.1090 # +-4.6%
    if (pt>=35 and pt<50 and abs(eta)>=0.000 and abs(eta)<1.200): return 0.0785 # +-3.9%
    if (pt>=35 and pt<50 and abs(eta)>=1.200 and abs(eta)<2.100): return 0.0788 # +-4.7%
    if (pt>=35 and pt<50 and abs(eta)>=2.100 and abs(eta)<2.400): return 0.1008 # +-8.2%
    if (pt>=50 and pt<70 and abs(eta)>=0.000 and abs(eta)<1.200): return 0.0793 # +-8.6%
    if (pt>=50 and pt<70 and abs(eta)>=1.200 and abs(eta)<2.100): return 0.0707 # +-10.9%
    if (pt>=50 and pt<70 and abs(eta)>=2.100 and abs(eta)<2.400): return 0.1073 # +-17.2%
    if (pt>=70 and abs(eta)>=0.000 and abs(eta)<1.200): return 0.0748 # +-17.7%
    if (pt>=70 and abs(eta)>=1.200 and abs(eta)<2.100): return 0.0813 # +-19.4%
    if (pt>=70 and abs(eta)>=2.100 and abs(eta)<2.400): return 0.0930 # +-39.3%
    return 0.

def electronQCDMCFakeRate_IsoTrigs_2017(pt, eta):
    if (pt>=10 and pt<15 and abs(eta)>=0 and abs(eta)<0.8 ): return 0
    if (pt>=10 and pt<15 and abs(eta)>=0.8 and abs(eta)<1.479 ): return 0
    if (pt>=10 and pt<15 and abs(eta)>=1.479 and abs(eta)<2.5 ): return 0
    if (pt>=15 and pt<20 and abs(eta)>=0 and abs(eta)<0.8 ): return 0.473083
    if (pt>=15 and pt<20 and abs(eta)>=0.8 and abs(eta)<1.479 ): return 0.567948
    if (pt>=15 and pt<20 and abs(eta)>=1.479 and abs(eta)<2.5 ): return 0.392926
    if (pt>=20 and pt<25 and abs(eta)>=0 and abs(eta)<0.8 ): return 0.158189
    if (pt>=20 and pt<25 and abs(eta)>=0.8 and abs(eta)<1.479 ): return 0.221255
    if (pt>=20 and pt<25 and abs(eta)>=1.479 and abs(eta)<2.5 ): return 0.158681
    if (pt>=25 and pt<35 and abs(eta)>=0 and abs(eta)<0.8 ): return 0.0711147
    if (pt>=25 and pt<35 and abs(eta)>=0.8 and abs(eta)<1.479 ): return 0.0829365
    if (pt>=25 and pt<35 and abs(eta)>=1.479 and abs(eta)<2.5 ): return 0.142449
    if (pt>=35 and pt<50 and abs(eta)>=0 and abs(eta)<0.8 ): return 0.0724598
    if (pt>=35 and pt<50 and abs(eta)>=0.8 and abs(eta)<1.479 ): return 0.12906
    if (pt>=35 and pt<50 and abs(eta)>=1.479 and abs(eta)<2.5 ): return 0.147341
    if (pt>=50 and pt<70 and abs(eta)>=0 and abs(eta)<0.8 ): return 0.0876978
    if (pt>=50 and pt<70 and abs(eta)>=0.8 and abs(eta)<1.479 ): return 0.158748
    if (pt>=50 and pt<70 and abs(eta)>=1.479 and abs(eta)<2.5 ): return 0.181927
    if (pt>=70 and abs(eta)>=0 and abs(eta)<0.8 ): return 0.234259
    if (pt>=70 and abs(eta)>=0.8 and abs(eta)<1.479 ): return 0.159783
    if (pt>=70 and abs(eta)>=1.479 and abs(eta)<2.5 ): return 0.279726
    return 0.

def muonQCDMCFakeRate_IsoTrigs_2017(pt, eta):
    if (pt>=10 and pt<15 and abs(eta)>=0 and abs(eta)<1.2 ): return 0
    if (pt>=10 and pt<15 and abs(eta)>=1.2 and abs(eta)<2.1 ): return 0
    if (pt>=10 and pt<15 and abs(eta)>=2.1 and abs(eta)<2.4 ): return 0
    if (pt>=15 and pt<20 and abs(eta)>=0 and abs(eta)<1.2 ): return 0.487579
    if (pt>=15 and pt<20 and abs(eta)>=1.2 and abs(eta)<2.1 ): return 0.546476
    if (pt>=15 and pt<20 and abs(eta)>=2.1 and abs(eta)<2.4 ): return 0.623434
    if (pt>=20 and pt<25 and abs(eta)>=0 and abs(eta)<1.2 ): return 0.180429
    if (pt>=20 and pt<25 and abs(eta)>=1.2 and abs(eta)<2.1 ): return 0.23425
    if (pt>=20 and pt<25 and abs(eta)>=2.1 and abs(eta)<2.4 ): return 0.277212
    if (pt>=25 and pt<35 and abs(eta)>=0 and abs(eta)<1.2 ): return 0.0561123
    if (pt>=25 and pt<35 and abs(eta)>=1.2 and abs(eta)<2.1 ): return 0.0862896
    if (pt>=25 and pt<35 and abs(eta)>=2.1 and abs(eta)<2.4 ): return 0.0876005
    if (pt>=35 and pt<50 and abs(eta)>=0 and abs(eta)<1.2 ): return 0.045945
    if (pt>=35 and pt<50 and abs(eta)>=1.2 and abs(eta)<2.1 ): return 0.0490797
    if (pt>=35 and pt<50 and abs(eta)>=2.1 and abs(eta)<2.4 ): return 0.062571
    if (pt>=50 and pt<70 and abs(eta)>=0 and abs(eta)<1.2 ): return 0.0407374
    if (pt>=50 and pt<70 and abs(eta)>=1.2 and abs(eta)<2.1 ): return 0.0527785
    if (pt>=50 and pt<70 and abs(eta)>=2.1 and abs(eta)<2.4 ): return 0.0482802
    if (pt>=70 and abs(eta)>=0 and abs(eta)<1.2 ): return 0.042955
    if (pt>=70 and abs(eta)>=1.2 and abs(eta)<2.1 ): return 0.0332809
    if (pt>=70 and abs(eta)>=2.1 and abs(eta)<2.4 ): return 0.0815757
    return 0.

def electronQCDMCFakeRate_IsoTrigs_2018(pt, eta):
    if (pt>=10 and pt<15 and abs(eta)>=0 and abs(eta)<0.8 ): return 0
    if (pt>=10 and pt<15 and abs(eta)>=0.8 and abs(eta)<1.479 ): return 0
    if (pt>=10 and pt<15 and abs(eta)>=1.479 and abs(eta)<2.5 ): return 0
    if (pt>=15 and pt<20 and abs(eta)>=0 and abs(eta)<0.8 ): return 0.469227
    if (pt>=15 and pt<20 and abs(eta)>=0.8 and abs(eta)<1.479 ): return 0.522789
    if (pt>=15 and pt<20 and abs(eta)>=1.479 and abs(eta)<2.5 ): return 0.407835
    if (pt>=20 and pt<25 and abs(eta)>=0 and abs(eta)<0.8 ): return 0.143496
    if (pt>=20 and pt<25 and abs(eta)>=0.8 and abs(eta)<1.479 ): return 0.201734
    if (pt>=20 and pt<25 and abs(eta)>=1.479 and abs(eta)<2.5 ): return 0.146049
    if (pt>=25 and pt<35 and abs(eta)>=0 and abs(eta)<0.8 ): return 0.0811412
    if (pt>=25 and pt<35 and abs(eta)>=0.8 and abs(eta)<1.479 ): return 0.081194
    if (pt>=25 and pt<35 and abs(eta)>=1.479 and abs(eta)<2.5 ): return 0.150573
    if (pt>=35 and pt<50 and abs(eta)>=0 and abs(eta)<0.8 ): return 0.0798284
    if (pt>=35 and pt<50 and abs(eta)>=0.8 and abs(eta)<1.479 ): return 0.125701
    if (pt>=35 and pt<50 and abs(eta)>=1.479 and abs(eta)<2.5 ): return 0.157778
    if (pt>=50 and pt<70 and abs(eta)>=0 and abs(eta)<0.8 ): return 0.0940064
    if (pt>=50 and pt<70 and abs(eta)>=0.8 and abs(eta)<1.479 ): return 0.172235
    if (pt>=50 and pt<70 and abs(eta)>=1.479 and abs(eta)<2.5 ): return 0.169947
    if (pt>=70 and abs(eta)>=0 and abs(eta)<0.8 ): return 0.218731
    if (pt>=70 and abs(eta)>=0.8 and abs(eta)<1.479 ): return 0.185943
    if (pt>=70 and abs(eta)>=1.479 and abs(eta)<2.5 ): return 0.282028
    return 0.

def muonQCDMCFakeRate_IsoTrigs_2018(pt, eta):
    if (pt>=10 and pt<15 and abs(eta)>=0 and abs(eta)<1.2 ): return 0
    if (pt>=10 and pt<15 and abs(eta)>=1.2 and abs(eta)<2.1 ): return 0
    if (pt>=10 and pt<15 and abs(eta)>=2.1 and abs(eta)<2.4 ): return 0
    if (pt>=15 and pt<20 and abs(eta)>=0 and abs(eta)<1.2 ): return 0.485363
    if (pt>=15 and pt<20 and abs(eta)>=1.2 and abs(eta)<2.1 ): return 0.548621
    if (pt>=15 and pt<20 and abs(eta)>=2.1 and abs(eta)<2.4 ): return 0.662505
    if (pt>=20 and pt<25 and abs(eta)>=0 and abs(eta)<1.2 ): return 0.169757
    if (pt>=20 and pt<25 and abs(eta)>=1.2 and abs(eta)<2.1 ): return 0.227283
    if (pt>=20 and pt<25 and abs(eta)>=2.1 and abs(eta)<2.4 ): return 0.273878
    if (pt>=25 and pt<35 and abs(eta)>=0 and abs(eta)<1.2 ): return 0.0570671
    if (pt>=25 and pt<35 and abs(eta)>=1.2 and abs(eta)<2.1 ): return 0.0852324
    if (pt>=25 and pt<35 and abs(eta)>=2.1 and abs(eta)<2.4 ): return 0.0950307
    if (pt>=35 and pt<50 and abs(eta)>=0 and abs(eta)<1.2 ): return 0.0449928
    if (pt>=35 and pt<50 and abs(eta)>=1.2 and abs(eta)<2.1 ): return 0.0530749
    if (pt>=35 and pt<50 and abs(eta)>=2.1 and abs(eta)<2.4 ): return 0.0711829
    if (pt>=50 and pt<70 and abs(eta)>=0 and abs(eta)<1.2 ): return 0.0398129
    if (pt>=50 and pt<70 and abs(eta)>=1.2 and abs(eta)<2.1 ): return 0.0531309
    if (pt>=50 and pt<70 and abs(eta)>=2.1 and abs(eta)<2.4 ): return 0.046544
    if (pt>=70 and abs(eta)>=0 and abs(eta)<1.2 ): return 0.0419674
    if (pt>=70 and abs(eta)>=1.2 and abs(eta)<2.1 ): return 0.0345744
    if (pt>=70 and abs(eta)>=2.1 and abs(eta)<2.4 ): return 0.0767373
    return 0.
