import json
import collections as cl

processes = {} #cl.OrderedDict()


# ttbar

processes['TTT'] = {'name':'TTT',
                    'file':'TauTauAnalysis.TT_TuneCUETP8M1', 
                    'cut':'1',
                    'cross-section':831.76,
                    'order':1 }

processes['TTJ'] = {'name':'TTJ',
                    'file':'tba',
                    'cut':'1',
                    'cross-section':831.76,
                    'isSignal':0, 
                    'order':1}


# Z + jets

processes['ZTT'] = {'name':'ZTT',
                    'file':'DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8',
                    'cross-section':1.,
                    'cut':'1',
                    'isSignal':0,
                    'order':3}

processes['ZTT1'] = {'name':'ZTT1',
                     'file':'DY1JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8',
                     'cross-section':1.,
                     'cut':'1',
                     'order':3}

processes['ZTT2'] = {'name':'ZTT2',
                     'file':'DY2JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8',
                     'cross-section':1.,
                     'cut':'1',
                     'isSignal':0, 
                     'order':3}

processes['ZTT3'] = {'name':'ZTT3',
                     'file':'DY3JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8',
                     'cross-section':1.,
                     'cut':'1',
                     'isSignal':0, 
                     'order':3}

processes['ZTT4'] = {'name':'ZTT4',
                     'file':'DY4JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8',
                     'cross-section':1.,
                     'cut':'1',
                     'isSignal':0, 
                     'order':3}


# ZL + jets

processes['ZL'] = {'name':'ZL',
                   'file':'DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8',
                   'cross-section':1.,
                   'cut':'1',
                   'isSignal':0,
                   'order':3}

processes['ZL1'] = {'name':'ZL1',
                    'file':'DY1JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8',
                    'cross-section':1.,
                    'cut':'1',
                    'order':3}

processes['ZL2'] = {'name':'ZL2',
                    'file':'DY2JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8',
                    'cross-section':1.,
                    'cut':'1',
                    'isSignal':0, 
                    'order':3}

processes['ZL3'] = {'name':'ZL3',
                    'file':'DY3JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8',
                    'cross-section':1.,
                    'cut':'1',
                    'isSignal':0, 
                    'order':3}

processes['ZL4'] = {'name':'ZL4',
                    'file':'DY4JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8',
                    'cross-section':1.,
                    'cut':'1',
                    'isSignal':0, 
                    'order':3}


# ZJ + jets

processes['ZJ'] = {'name':'ZJ',
                   'file':'DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8',
                   'cross-section':1.,
                   'cut':'1',
                   'isSignal':0,
                   'order':3}

processes['ZJ1'] = {'name':'ZJ1',
                    'file':'DY1JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8',
                    'cross-section':1.,
                    'cut':'1',
                    'order':3}

processes['ZJ2'] = {'name':'ZJ2',
                    'file':'DY2JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8',
                    'cross-section':1.,
                    'cut':'1',
                    'isSignal':0, 
                    'order':3}

processes['ZJ3'] = {'name':'ZJ3',
                    'file':'DY3JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8',
                    'cross-section':1.,
                    'cut':'1',
                    'isSignal':0, 
                    'order':3}

processes['ZJ4'] = {'name':'ZJ4',
                    'file':'DY4JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8',
                    'cross-section':1.,
                    'cut':'1',
                    'isSignal':0, 
                    'order':3}


# W + jets

processes['W'] = {'name':'W',
                  'file':'tba',
                  'cross-section':1.,
                  'cut':'1',
                  'isSignal':0, 
                  'order':8}

processes['W1'] = {'name':'W1',
                   'file':'tba',
                   'cross-section':1.,
                   'cut':'1',
                   'isSignal':0, 
                   'order':8}

processes['W2'] = {'name':'W2',
                   'file':'tba',
                   'cross-section':1.,
                   'cut':'1',
                   'isSignal':0, 
                   'order':8}

processes['W3'] = {'name':'W3',
                   'file':'tba',
                   'cross-section':1.,
                   'cut':'1',
                   'isSignal':0, 
                   'order':8}

processes['W4'] = {'name':'W4',
                   'file':'tba',
                   'cross-section':1.,
                   'cut':'1',
                   'isSignal':0, 
                   'order':8}


# dibosons
          
processes['WW'] = {'name':'WW',
                   'file':'WW_TuneCP5_13TeV-pythia8',
                   'cross-section':63.21,
                   'cut':'1',
                   'isSignal':0, 
                   'order':7}

processes['WZ'] = {'name':'WZ',
                   'file':'WZ_TuneCP5_13TeV-pythia8',
                   'cross-section':47.13,
                   'cut':'1',
                   'isSignal':0, 
                   'order':7}

processes['ZZ'] = {'name':'ZZ',
                   'file':'ZZ_TuneCP5_13TeV-pythia8',
                   'cross-section':16.523,
                   'cut':'1',
                   'isSignal':0, 
                   'order':7}


# single top
    
processes['ST_t_t'] = {'name':'ST_t_t',
                       'file':'ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8',
                       'cross-section':136.02,
                       'cut':'1',
                       'isSignal':0, 
                       'order':9}

processes['ST_t_tbar'] = {'name':'ST_t_tbar',
                          'file':'ST_t-channel_antitop_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8',
                          'cross-section':80.95,
                          'cut':'1',
                          'isSignal':0, 
                          'order':10}

processes['ST_tw_t'] = {'name':'ST_tw_t',
                        'file':'ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8',
                        'cross-section':35.85,
                        'cut':'1',
                        'isSignal':0, 
                        'order':11}

processes['ST_tw_tbar'] = {'name':'ST_tw_tbar',
                           'file':'ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8',
                           'cross-section':35.85,
                           'cut':'1',
                           'isSignal':0, 
                           'order':12}


# signals

processes['Signal_pair_M200'] = {'name':'Signal_pair_M200',
                                 'file':'tba',
                                 'cross-section':60.6,
                                 'cut':'1',
                                 'isSignal':1, 
                                 'order':3000}



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


outputjson = open('processes.json','w')
json.dump(processes, outputjson, indent=4)
