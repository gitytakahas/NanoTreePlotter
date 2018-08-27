import json
import collections as cl

processes = {} #cl.OrderedDict()


# ttbar

processes['TTLL'] = {'name':'TTLL',
                     'file':'TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8__RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1__NANOAODSIM/',
                     'cut':'1',
                     'cross-section':87.31,
                     'isSignal':0, 
                     'order':1 }

processes['TTLJ'] = {'name':'TTLJ',
                     'file':'TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8__RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1__NANOAODSIM/',
                     'cut':'1',
                     'cross-section':364.40,
                     'isSignal':0, 
                     'order':1}

processes['TTJJ'] = {'name':'TTJJ',
                     'file':'TTToHadronic_TuneCP5_13TeV-powheg-pythia8__RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1__NANOAODSIM/',
                     'cut':'1',
                     'cross-section':380.10,
                     'isSignal':0, 
                     'order':1}






# Z + jets

processes['ZTT'] = {'name':'ZTT',
#                    'file':'DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_RunIIFall17NanoAOD-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-v1',
                    'file':'ZTT',
                    'cross-section':1.,
                    'cut':'1',
                    'isSignal':0,
                    'order':3}

processes['ZTT1'] = {'name':'ZTT1',
                     'file':'DY1JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8__RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1__NANOAODSIM/',
                     'cross-section':1.,
                     'cut':'1',
                     'isSignal':0, 
                     'order':3}

processes['ZTT2'] = {'name':'ZTT2',
                     'file':'DY2JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8__RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1__NANOAODSIM/',
                     'cross-section':1.,
                     'cut':'1',
                     'isSignal':0, 
                     'order':3}

processes['ZTT3'] = {'name':'ZTT3',
                     'file':'DY3JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8__RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1__NANOAODSIM/',
                     'cross-section':1.,
                     'cut':'1',
                     'isSignal':0, 
                     'order':3}

processes['ZTT4'] = {'name':'ZTT4',
                     'file':'DY4JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8__RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1__NANOAODSIM/',
                     'cross-section':1.,
                     'cut':'1',
                     'isSignal':0, 
                     'order':3}

processes['ZTT10to50'] = {'name':'ZTT10to50',
                          'file':'DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8__ytakahas-Nano_20180518_DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8-a7a5b67d3e3590e4899e147be08660be__USER/',
                          'cross-section':18610.0,
                          'cut':'1',
                          'isSignal':0, 
                          'order':3}




## ZL + jets
#
#processes['ZL'] = {'name':'ZL',
#                   'file':'DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8',
#                   'cross-section':1.,
#                   'cut':'1',
#                   'isSignal':0,
#                   'order':3}
#
#processes['ZL1'] = {'name':'ZL1',
#                    'file':'DY1JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8',
#                    'cross-section':1.,
#                    'cut':'1',
#                    'order':3}
#
#processes['ZL2'] = {'name':'ZL2',
#                    'file':'DY2JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8',
#                    'cross-section':1.,
#                    'cut':'1',
#                    'isSignal':0, 
#                    'order':3}
#
#processes['ZL3'] = {'name':'ZL3',
#                    'file':'DY3JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8',
#                    'cross-section':1.,
#                    'cut':'1',
#                    'isSignal':0, 
#                    'order':3}
#
#processes['ZL4'] = {'name':'ZL4',
#                    'file':'DY4JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8',
#                    'cross-section':1.,
#                    'cut':'1',
#                    'isSignal':0, 
#                    'order':3}
#
#
## ZJ + jets
#
#processes['ZJ'] = {'name':'ZJ',
#                   'file':'DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8',
#                   'cross-section':1.,
#                   'cut':'1',
#                   'isSignal':0,
#                   'order':3}
#
#processes['ZJ1'] = {'name':'ZJ1',
#                    'file':'DY1JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8',
#                    'cross-section':1.,
#                    'cut':'1',
#                    'order':3}
#
#processes['ZJ2'] = {'name':'ZJ2',
#                    'file':'DY2JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8',
#                    'cross-section':1.,
#                    'cut':'1',
#                    'isSignal':0, 
#                    'order':3}
#
#processes['ZJ3'] = {'name':'ZJ3',
#                    'file':'DY3JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8',
#                    'cross-section':1.,
#                    'cut':'1',
#                    'isSignal':0, 
#                    'order':3}
#
#processes['ZJ4'] = {'name':'ZJ4',
#                    'file':'DY4JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8',
#                    'cross-section':1.,
#                    'cut':'1',
#                    'isSignal':0, 
#                    'order':3}


# W + jets

processes['W'] = {'name':'W',
                  'file':'WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8__ytakahas-NanoTest_20180507_WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8-a7a5b67d3e3590e4899e147be08660be__USER/',
                  'cross-section':1.,
                  'cut':'1',
                  'isSignal':0, 
                  'order':8}

processes['W1'] = {'name':'W1',
                   'file':'W1JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8__ytakahas-NanoTest_20180507_W1JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8-a7a5b67d3e3590e4899e147be08660be__USER/',
                   'cross-section':1.,
                   'cut':'1',
                   'isSignal':0, 
                   'order':8}

processes['W2'] = {'name':'W2',
                   'file':'W2JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8__ytakahas-NanoTest_20180507_W2JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8-a7a5b67d3e3590e4899e147be08660be__USER/',
                   'cross-section':1.,
                   'cut':'1',
                   'isSignal':0, 
                   'order':8}

processes['W3'] = {'name':'W3',
                   'file':'W3JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8__ytakahas-NanoTest_20180507_W3JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8-a7a5b67d3e3590e4899e147be08660be__USER/',
                   'cross-section':1.,
                   'cut':'1',
                   'isSignal':0, 
                   'order':8}

processes['W4'] = {'name':'W4',
                   'file':'W4JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8__ytakahas-NanoTest_20180507_W4JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8-a7a5b67d3e3590e4899e147be08660be__USER/',
                   'cross-section':1.,
                   'cut':'1',
                   'isSignal':0, 
                   'order':8}


# dibosons
          
#processes['WW'] = {'name':'WW',
#                   'file':'WW_TuneCP5_13TeV-pythia8',
#                   'cross-section':63.21,
#                   'cut':'1',
#                   'isSignal':0, 
#                   'order':7}
#
#processes['WZ'] = {'name':'WZ',
#                   'file':'WZ_TuneCP5_13TeV-pythia8',
#                   'cross-section':47.13,
#                   'cut':'1',
#                   'isSignal':0, 
#                   'order':7}
#
#processes['ZZ'] = {'name':'ZZ',
#                   'file':'ZZ_TuneCP5_13TeV-pythia8',
#                   'cross-section':16.523,
#                   'cut':'1',
#                   'isSignal':0, 
#                   'order':7}


# single top
    
processes['ST_t_t'] = {'name':'ST_t_t',
                       'file':'ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8__RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1__NANOAODSIM/',
                       'cross-section':136.02,
                       'cut':'1',
                       'isSignal':0, 
                       'order':9}

processes['ST_t_tbar'] = {'name':'ST_t_tbar',
                          'file':'ST_t-channel_antitop_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8__RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1__NANOAODSIM/',
                          'cross-section':80.95,
                          'cut':'1',
                          'isSignal':0, 
                          'order':10}

processes['ST_tw_t'] = {'name':'ST_tw_t',
                        'file':'ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8__RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1__NANOAODSIM/',
                        'cross-section':35.85,
                        'cut':'1',
                        'isSignal':0, 
                        'order':11}

processes['ST_tw_tbar'] = {'name':'ST_tw_tbar',
                           'file':'ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8__RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1__NANOAODSIM/',
                           'cross-section':35.85,
                           'cut':'1',
                           'isSignal':0, 
                           'order':12}


# signals

#processes['Signal_pair_M200'] = {'name':'Signal_pair_M200',
#                                 'file':'tba',
#                                 'cross-section':60.6,
#                                 'cut':'1',
#                                 'isSignal':1, 
#                                 'order':3000}



# data

processes['SingleMuon'] = {'name':'data_obs',
                           'file':'SingleMuon',
                           'cross-section':1.,
                           'cut':'1',
                           'isSignal':0, 
                           'order':2999}

processes['SingleElectron'] = {'name':'data_obs',
                               'file':'SingleElectron',
                               'cross-section':1.,
                               'cut':'1',
                               'isSignal':0, 
                               'order':2999}

processes['Tau'] = {'name':'data_obs',
                    'file':'Tau',
                    'cross-section':1.,
                    'cut':'1',
                    'isSignal':0, 
                    'order':2999}



processes['QCD'] = {'name':'QCD',
                    'file':None,
                    'cross-section':None,
                    'cut':'1',
                    'isSignal':0, 
                    'order':0}


processes['SLQ_pair_M500'] = {'name':'SLQ_pair_M500',
                               'file':'LQ3ToTauB_Fall2017_5f_Madgraph_LO_pair-M500__nanoAOD__v1',
#                               'cross-section':0.00586,
                               'cross-section':1.,
                               'cut':'1',
                               'isSignal':1, 
                               'order':3000}

processes['VLQ_pair_M500'] = {'name':'VLQ_pair_M500',
                               'file':'VectorLQ3ToTauB_Fall2017_5f_Madgraph_LO_pair_M500__nanoAOD__v1',
#                               'cross-section':0.00586,
                               'cross-section':1.,
                               'cut':'1',
                               'isSignal':1, 
                               'order':3000}

processes['SLQ_single_M500'] = {'name':'SLQ_single_M500',
                               'file':'LQ3ToTauB_Fall2017_5f_Madgraph_LO_s-channel-M500__nanoAOD__v1',
#                               'cross-section':0.00586,
                               'cross-section':1.,
                               'cut':'1',
                               'isSignal':1, 
                               'order':3000}

processes['VLQ_single_M500'] = {'name':'VLQ_single_M500',
                               'file':'VectorLQ3ToTauB_Fall2017_5f_Madgraph_LO_s_channel_M500__nanoAOD__v1/',
#                               'cross-section':0.00586,
                               'cross-section':1.,
                               'cut':'1',
                               'isSignal':1, 
                               'order':3000}



processes['SLQ_pair_M1000'] = {'name':'SLQ_pair_M1000',
                               'file':'LQ3ToTauB_Fall2017_5f_Madgraph_LO_pair-M1000__nanoAOD__v1',
#                               'cross-section':0.00586,
                               'cross-section':1.,
                               'cut':'1',
                               'isSignal':1, 
                               'order':3000}

processes['VLQ_pair_M1000'] = {'name':'VLQ_pair_M1000',
                               'file':'VectorLQ3ToTauB_Fall2017_5f_Madgraph_LO_pair_M1000__nanoAOD__v1',
#                               'cross-section':0.00586,
                               'cross-section':1.,
                               'cut':'1',
                               'isSignal':1, 
                               'order':3000}

processes['SLQ_single_M1000'] = {'name':'SLQ_single_M1000',
                               'file':'LQ3ToTauB_Fall2017_5f_Madgraph_LO_s-channel-M1000__nanoAOD__v1',
#                               'cross-section':0.00586,
                               'cross-section':1.,
                               'cut':'1',
                               'isSignal':1, 
                               'order':3000}

processes['VLQ_single_M1000'] = {'name':'VLQ_single_M1000',
                               'file':'VectorLQ3ToTauB_Fall2017_5f_Madgraph_LO_s_channel_M1000__nanoAOD__v1/',
#                               'cross-section':0.00586,
                               'cross-section':1.,
                               'cut':'1',
                               'isSignal':1, 
                               'order':3000}




processes['SLQ_pair_M1500'] = {'name':'SLQ_pair_M1500',
                               'file':'LQ3ToTauB_Fall2017_5f_Madgraph_LO_pair-M1500__nanoAOD__v1',
#                               'cross-section':0.00586,
                               'cross-section':1.,
                               'cut':'1',
                               'isSignal':1, 
                               'order':3000}

processes['VLQ_pair_M1500'] = {'name':'VLQ_pair_M1500',
                               'file':'VectorLQ3ToTauB_Fall2017_5f_Madgraph_LO_pair_M1500__nanoAOD__v1',
#                               'cross-section':0.00586,
                               'cross-section':1.,
                               'cut':'1',
                               'isSignal':1, 
                               'order':3000}

processes['SLQ_single_M1500'] = {'name':'SLQ_single_M1500',
                               'file':'LQ3ToTauB_Fall2017_5f_Madgraph_LO_s-channel-M1500__nanoAOD__v1',
#                               'cross-section':0.00586,
                               'cross-section':1.,
                               'cut':'1',
                               'isSignal':1, 
                               'order':3000}

processes['VLQ_single_M1500'] = {'name':'VLQ_single_M1500',
                               'file':'VectorLQ3ToTauB_Fall2017_5f_Madgraph_LO_s_channel_M1500__nanoAOD__v1/',
#                               'cross-section':0.00586,
                               'cross-section':1.,
                               'cut':'1',
                               'isSignal':1, 
                               'order':3000}



processes['SLQ_pair_M2000'] = {'name':'SLQ_pair_M2000',
                               'file':'LQ3ToTauB_Fall2017_5f_Madgraph_LO_pair-M2000__nanoAOD__v1',
#                               'cross-section':0.00586,
                               'cross-section':1.,
                               'cut':'1',
                               'isSignal':1, 
                               'order':3000}

processes['VLQ_pair_M2000'] = {'name':'VLQ_pair_M2000',
                               'file':'VectorLQ3ToTauB_Fall2017_5f_Madgraph_LO_pair_M2000__nanoAOD__v1',
#                               'cross-section':0.00586,
                               'cross-section':1.,
                               'cut':'1',
                               'isSignal':1, 
                               'order':3000}

processes['SLQ_single_M2000'] = {'name':'SLQ_single_M2000',
                               'file':'LQ3ToTauB_Fall2017_5f_Madgraph_LO_s-channel-M2000__nanoAOD__v1',
#                               'cross-section':0.00586,
                               'cross-section':1.,
                               'cut':'1',
                               'isSignal':1, 
                               'order':3000}

processes['VLQ_single_M2000'] = {'name':'VLQ_single_M2000',
                               'file':'VectorLQ3ToTauB_Fall2017_5f_Madgraph_LO_s_channel_M2000__nanoAOD__v1/',
#                               'cross-section':0.00586,
                               'cross-section':1.,
                               'cut':'1',
                               'isSignal':1, 
                               'order':3000}



outputjson = open('processes.json','w')
json.dump(processes, outputjson, indent=4)
