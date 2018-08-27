import os, math, copy, sys, collections
from ROOT import gStyle, TCanvas, TLegend, TH1F, TFile, gROOT, Double
import MultiDraw

#from ROOT import TFile, TH1F, gROOT, Double
from DisplayManager import DisplayManager
from DataMCPlot import *
from array import array
from officialStyle import officialStyle

gROOT.Macro('./functionmacro.C+')
gROOT.SetBatch(True)
officialStyle(gStyle)
gStyle.SetOptTitle(0)


#from getTauTriggerSFs import *
#tauSFs = getTauTriggerSFs('vtight')


import ConfigParser
import json

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class config(object):

    def __init__(self, options):

        self.channel = options.channel
        
        self.hists = {}

        # read settings
        init = ConfigParser.SafeConfigParser() 
        init.read("./settings.ini")

        self.lumi = Double(init.get(self.channel, 'lumi'))
        self.basedir = init.get('common', 'basedir')
        self.signal2show = init.get(self.channel, 'signal2show').split(',')

        print '-'*80
        print 'channel = ', self.channel
        print 'lumi = ', self.lumi
        print 'Options:', options
        print '-'*80

        # read processes (common for all channels)
        f = open('processes.json', 'r')
        self.processes = json.load(f)

        self.dcname = None

        self.W_highMT = 80.

#        if options.tes!=None:
#            dcname += 'TES_' + str(options.tes)
#
#        if options.ees!=None:
#            dcname += 'EES_' + str(options.ees)
#
#        if options.mid!=None:
#            dcname += 'MID_' + str(options.mid)
#
#        if options.tid!=None:
#            dcname += 'TID_' + str(options.tid)
#
#        if options.jtf!=None:
#            dcname += 'JTF_' + str(options.jtf)
#
#        if options.topr!=None:
#            dcname += 'Topr_' + str(options.topr)

        
#        print '-'*80

        for processname, val in sorted(self.processes.iteritems()):

            if processname=='QCD': continue

            filename = self.basedir + '/' + val['file'] + '/' + options.channel + '.root'

#            if self.channel=='mutau':
#                filename = filename.replace('SingleMuon', 'SingleElectron')
#            if self.tes!=None and processname in ['TTT', 'TTJ']: 
#                filename = filename.replace('TT/', 'TT_tes_' + str(self.tes) + '/')
#
#            if self.tes!=None and processname.find('Signal')!=-1:
#                filename = filename.replace('/LQ/', '/LQ_tes_' + str(self.tes) + '/')
#
##            if self.ltf!=None and processname in ['TTT', 'TTJ']:
##                filename = filename.replace('TT/', 'TT_LTF_' + str(self.ltf) + '/')                   
#
#            if self.ees!=None and processname in ['TTT', 'TTJ']:
#                filename = filename.replace('TT/', 'TT_EES_' + str(self.ees) + '/')                   
#
##            if self.jtes!=None and processname in ['TTT', 'TTJ']:
##                filename = filename.replace('TT/', 'TT_jtes_' + str(self.jtes) + '/')                   
                



            if not os.path.isfile(filename):
                print bcolors.BOLD + bcolors.FAIL + 'Register', processname.ljust(20), '[warning]', filename, 'does not exist ... skip !' + bcolors.ENDC
                self.processes.pop(processname, None)
                continue
            

#            if val['name'].find('SLQ')!=-1 or val['name'].find('VLQ')!=-1:
#                
#                if (val['name'] not in self.signal2show) and ('all' not in self.signal2show):
#                    print bcolors.BOLD + bcolors.FAIL + 'Register', processname.ljust(20), '[warning]', filename, 'skipped as it is not in signal2show list' + bcolors.ENDC
#                    self.processes.pop(processname, None)
#                    continue


            file = TFile(filename) 
            
            if not file.GetListOfKeys().Contains("tree_cut_relaxed"):
                print bcolors.BOLD + bcolors.FAIL + 'Register', processname.ljust(20), '[error] file (', filename , ') exits but broken ...' + bcolors.ENDC
                self.processes.pop(processname, None)


            if val['name']=='data_obs':
                rmflag = False
                if self.channel == 'mutau' and processname !='SingleMuon': rmflag = True
                if self.channel == 'eletau' and processname !='SingleElectron':  rmflag = True
                if self.channel == 'tautau' and processname.find('Tau')==-1:  rmflag = True

                if rmflag:
                    print bcolors.BOLD + 'Register', processname.ljust(20), '[info] file (', filename , ') removed as this is unnecessary for ' + self.channel + 'channel ...'
                    self.processes.pop(processname, None)
                    continue



                
            # split ZTT, depending on genPartFlav
            if self.channel in ['mutau', 'eletau']:

                if val['name'].find('ZTT')!=-1:
                    
                    self.processes[processname]['cut'] = self.processes[processname]['cut'].replace('1', 'genPartFlav_2==5')

                    newname = self.processes[processname]['name'].replace('ZTT', 'ZL')

                    dict_zl = {'name':newname,
                               'file':self.processes[processname]['file'], 
                               'cross-section':self.processes[processname]['cross-section'], 
                               'cut':self.processes[processname]['cut'].replace('==', '<'),
                               'isSignal':self.processes[processname]['isSignal'], 
                               'order':self.processes[processname]['order']
                               }


                    self.processes[newname] = copy.deepcopy(dict_zl)
                    
                    newname = self.processes[processname]['name'].replace('ZTT', 'ZJ')
                    
                    dict_zj = {'name':newname,
                               'file':self.processes[processname]['file'], 
                               'cross-section':self.processes[processname]['cross-section'], 
                               'cut':self.processes[processname]['cut'].replace('==5', '==0'),
                               'isSignal':self.processes[processname]['isSignal'], 
                               'order':self.processes[processname]['order']
                               }
                    
                    self.processes[newname] = copy.deepcopy(dict_zj)
                    


                if val['name'] in ['TTLL', 'TTLJ', 'TTJJ']:


                    self.processes[processname]['cut'] = self.processes[processname]['cut'].replace('1', 'genPartFlav_2==5')

                    newname = self.processes[processname]['name'] + '_J'
                    
                    dict_ttj = {'name':newname,
                                'file':self.processes[processname]['file'], 
                                'cross-section':self.processes[processname]['cross-section'], 
                                'cut':self.processes[processname]['cut'].replace('==5', '==0'),
                                'isSignal':self.processes[processname]['isSignal'], 
                                'order':self.processes[processname]['order']
                                }

                    self.processes[newname] = copy.deepcopy(dict_ttj)



#        print '-'*80
#        print self.processes
        print '-'*80



        for processname, val in sorted(self.processes.iteritems()):

            if processname=='QCD': continue

            filename = self.basedir + '/' + val['file'] + '/' + options.channel + '.root'

            file = TFile(filename) 
                
            ntot = file.Get("h_cutflow").GetBinContent(16)
            
            self.processes[processname]['ntot'] = ntot
            self.processes[processname]['file'] = file

            sf = self.processes[processname]['cross-section']*self.lumi*1000/self.processes[processname]['ntot']


            print 'Register', bcolors.BOLD + processname.ljust(20) + bcolors.ENDC, str(int(self.processes[processname]['ntot'])).ljust(15), 'SF = ', '{0:.5f}'.format(sf).ljust(6), filename



        # DY stitching
        self.dy_weightstr = '1'

        if self.processes.has_key('ZTT') and self.processes.has_key('ZTT1') and self.processes.has_key('ZTT2') and self.processes.has_key('ZTT3') and self.processes.has_key('ZTT4'):


            dy_xs = [4954.0, 1012.5, 332.8, 101.8, 54.8]
            
            dy_nlo_xs = 5765.4
            
            dykfactor = dy_nlo_xs/dy_xs[0]       

            dy_efflumi = []

            for ijet, processname in enumerate(['ZTT', 'ZTT1', 'ZTT2', 'ZTT3', 'ZTT4']):
                dy_efflumi.append(self.processes[processname]['ntot']/dy_xs[ijet])


            # calculate DY weight 
            dy_weight = []

            for ijet, processname in enumerate(['ZTT', 'ZTT1', 'ZTT2', 'ZTT3', 'ZTT4']):
                if processname=='ZTT':
                    dy_weight.append(dykfactor*self.lumi*1000/dy_efflumi[ijet])
                else:
                    dy_weight.append(dykfactor*self.lumi*1000/(dy_efflumi[0] + dy_efflumi[ijet]))


            self.dy_weightstr = '('

            for ii, _weight in enumerate(dy_weight):
                self.dy_weightstr += '(LHE_Njets==' + str(ii) + ' ? ' + str(dy_weight[ii]) + ': 1)*'


            self.dy_weightstr += '1)'




        # W stitching 

        self.w_weightstr = '1'

        if self.processes.has_key('W') and self.processes.has_key('W1') and self.processes.has_key('W2') and self.processes.has_key('W3') and self.processes.has_key('W4'):

            
            w_xs = [50380, 9644.5, 3144.5, 954.8, 485.6]
            
            w_nlo_xs = 61526.7
            
            wkfactor = w_nlo_xs/w_xs[0]       

            w_efflumi = []
            
            for ijet, processname in enumerate(['W', 'W1', 'W2', 'W3', 'W4']):
                w_efflumi.append(self.processes[processname]['ntot']/w_xs[ijet])


            w_weight = []
            for ijet, processname in enumerate(['W', 'W1', 'W2', 'W3', 'W4']):
                if processname=='W':
                    w_weight.append(wkfactor*self.lumi*1000/w_efflumi[ijet])
                else:
                    w_weight.append(wkfactor*self.lumi*1000/(w_efflumi[0] + w_efflumi[ijet]))


            self.w_weightstr= '('

            for ii, _weight in enumerate(w_weight):
                self.w_weightstr += '(LHE_Njets==' + str(ii) + ' ? ' + str(w_weight[ii]) + ': 1)*'


            self.w_weightstr += '1)'
            print self.w_weightstr





    def returnWeight(self, pname):

#        tauidsf = '1'
#
#        if self.tid=='up':
#            tauidsf = 'tauID_up(pt_2)'
#        elif self.tid=='down':
#            tauidsf = 'tauID_down(pt_2)'
#        elif self.tid==None:
#            pass
#        else:
#            print 'Invalid option !!!!!'


        weight = 'genWeight*weight*getPUweight(Pileup_nTrueInt)' 

#        if self.topr=='up':
#            weight += '*1/ttptweight'
#        elif self.topr=='down':
#            weight += '*ttptweight'


        if pname in ['ZTT', 'ZTT1', 'ZTT2', 'ZTT3', 'ZTT4',
                     'ZL', 'ZL1', 'ZL2', 'ZL3', 'ZL4',
                     'ZJ', 'ZJ1', 'ZJ2', 'ZJ3', 'ZJ4']:            

            weight += '*' + self.dy_weightstr  #+ '*(gen_match_2==5 ? ' + str(tauidsf) + ' : 1)'

        elif pname in ['W', 'W1', 'W2', 'W3', 'W4']:

            weight += '*' + self.w_weightstr  #'*(gen_match_2==5 ? ' + str(tauidsf) + ' : 1)'

        else:
            
            weight += '*' + str(self.processes[pname]['cross-section']*self.lumi*1000/self.processes[pname]['ntot'])


#        if self.channel == 'mutau':
#            weight += '*getMuWeight(pt_1, eta_1)'


        if self.processes[pname]['name'] == 'data_obs':
            weight = '1'


            

#        if self.channel == 'mutau':
#            if pname in ['SingleMuon']:
#                pass
#            else:
#                weight += '*getMuTrigWeight(pt_1, eta_1)'
#                weight += '*getTrackReco(eta_1)'

#        print pname, 'returnweight = ', weight
        return weight




###########        self.tes = options.tes
###########        
############        self.ltf = ltf
###########
###########        self.ees = ees
###########
############        self.jtes = jtes
###########
###########        self.tid = tid
###########        
###########        self.jtf = jtf
###########
###########        self.topr = topr
###########        
###########        self.dcname = dcname
###########
###########        self.basedir = basedir
###########
###########        self.lumi = lumi
###########        
###########
###########

    def createHistograms(self, catname, selection, exceptionList, vardir, blind = False, pblind = True, dcvar = 'ht', sf_W = 1.):

        print '-'*80
        print 'category : ', catname
        print 'selection : ', selection
        print 'exceptionList : ', exceptionList
#        print 'vardir = ', vardir
        print 'SF for W = ', sf_W
        print '-'*80    

        for processname, val in self.processes.iteritems():
            if val['name'] in exceptionList: 
#                print 'Remove', processname
                continue

#            print 'processing', val['file']
            tree = val['file'].Get('tree_cut_relaxed')

            var_tuples = []
    
            for varname, var in vardir.iteritems():

                hname = 'hist_' + catname + '_' + processname + '_' + varname
       
                hist_register = TH1F(hname, hname, var['nbins'], var['min'], var['max'])
                hist_register.GetXaxis().SetTitle(var['label'])
                hist_register.GetXaxis().SetLabelSize(0)
                hist_register.Sumw2()

                if val['name'] == 'data_obs' or val['name'].find('SLQ')!=-1 or val['name'].find('VLQ')!=-1:
                    hist_register.SetMarkerStyle(20)
                    hist_register.SetMarkerSize(0.5)
        
                self.hists[hname] = hist_register

                var_tuples.append('{var} >> {hist}'.format(var=var['drawname'], hist=hname))

            weight = self.returnWeight(processname)

            if processname in ['W', 'W1', 'W2', 'W3', 'W4']:
                weight += '*' + str(sf_W)

            if blind:
                weight += '*(isData==1 ? 0 : 1)'
#                weight += '*(run==1 ? 0 : 1)'


            cutstr = selection + ' && ' + val['cut']
            cut = '({c}) * {we}'.format(c=cutstr, we=weight)

#            print 'final cut = ', cut
            tree.MultiDraw(var_tuples, cut)


        
        ensureDir('fig/' + self.channel + '/' + catname)

        for varname, var in vardir.iteritems():        

            stackname = 'stackhist_' + catname + '_' + varname
            hist = DataMCPlot(stackname, self.signal2show)
            hist.legendBorders = 0.55, 0.55, 0.88, 0.88

            # calculate Punzi significance



#            if pblind:
#
#                hist_allbg = None
#                
#                for processname, val in self.processes.iteritems():
#                    
#                    if val['name'] == 'data_obs' or val['name'].find('LQ')!=-1: continue
#                    
#                    hname = 'hist_' + catname + '_' + processname + '_' + varname
#                    if not self.hists.has_key(hname): continue
#                    
#                    if hist_allbg == None:
#                        hist_allbg = copy.deepcopy(self.hists[hname])
#                    else:
#                        hist_allbg.Add(self.hists[hname])
#                        
#
#
#                pbflag = False
#
#                for ixbin in range(1, hist_allbg.GetXaxis().GetNbins()+1):
#                    nbg = hist_allbg.GetBinContent(ixbin)
#
#
#                    if not pbflag:
#
#                        nsigbank = []
#
#                        for processname, val in self.processes.iteritems():
#
#                            hname = 'hist_' + catname + '_' + processname + '_' + varname
#                            if not self.hists.has_key(hname): continue
#                            
#                            if val['name'].find('LQ')!=-1:
#                                nsigbank.append(self.hists[hname].GetBinContent(ixbin))
#
#                        punzi = -1
#
#                        if nbg>0:
#                            punzi = max(nsigbank)/math.sqrt(nbg + (0.09*nbg)*(0.09*nbg))
#
#                        print ixbin, max(nsigbank), nbg, punzi
#
#                        if punzi > 0.1:
#                            pbflag = True
#                            
#                    else:
#
#                        hname = 'hist_' + catname + '_data_obs_' + varname
#
#                        import pdb; pdb.set_trace()
#                        print 'data !!!!!!!!!!!!!', ixbin, self.hists[hname].GetBinContent(ixbin)
#
#                        self.hists[hname].SetBinContent(ixbin, 0)
#                        self.hists[hname].SetBinError(ixbin, 0)
##                        hist.Hist('data_obs').SetBinError(ixbin, 0)
#
#
#                        print 'data !!!!!!!!!!!!!', ixbin, self.hists[hname].GetBinContent(ixbin)





            for processname, val in self.processes.iteritems():

                hname = 'hist_' + catname + '_' + processname + '_' + varname
                if not self.hists.has_key(hname): continue

                pname = processname
                
                hist.AddHistogram(val['name'], self.hists[hname], val['order'])

                if val['name'] == 'data_obs' or val['name'].find('LQ')!=-1:
                    hist.Hist(val['name']).stack = False

                    if val['name'].find('LQ')!=-1:
                        for ixbin in range(1, hist.Hist(val['name']).weighted.GetXaxis().GetNbins()+1):
                            hist.Hist(val['name']).weighted.SetBinError(ixbin, 0)





#            hist.Group('Electroweak', ['WWTo1L1Nu2Q', 'WZTo3LNu', 'WZTo2L2Q', 'WZTo1L1Nu2Q', 'WZTo1L3Nu', 'ZZTo2Q2Nu', 'ZZTo2L2Q', 'ZZTo4L', 'ZZTo4Q', 'VVTo2L2Nu', 'ST_t_top', 'ST_t_antitop', 'ST_tw_top', 'ST_tw_antitop', 'ZTT', 'ZTT1', 'ZTT2', 'ZTT3', 'ZTT4','ZTT10to50', 'ZL', 'ZL1', 'ZL2', 'ZL3', 'ZL4', 'ZL10to50', 'ZJ', 'ZJ1', 'ZJ2', 'ZJ3', 'ZJ4', 'ZJ10to50', 'W', 'W1', 'W2', 'W3', 'W4'])
#            hist.Group('VV', ['WWTo1L1Nu2Q', 'WZTo3LNu', 'WZTo2L2Q', 'WZTo1L1Nu2Q', 'ZZTo2Q2Nu', 'ZZTo4L', 'ZZTo4Q', 'VVTo2L2Nu', 'ST_t_top', 'ST_t_antitop', 'ST_tw_top', 'ST_tw_antitop', 'ZZTo2L2Q', 'WZTo1L3Nu'])
            hist.Group('VV', ['WW', 'WZ', 'ZZ'])
            hist.Group('ST', ['ST_t_t', 'ST_t_tbar', 'ST_tw_t', 'ST_tw_tbar'])

            hist.Group('ZTT', ['ZTT', 'ZTT1', 'ZTT2', 'ZTT3', 'ZTT4','ZTT10to50'])
#            hist.Group('ZTT', ['ZTT', 'ZTT1', 'ZTT2', 'ZTT3', 'ZTT4','ZTT10to50', 'ZL', 'ZL1', 'ZL2', 'ZL3', 'ZL4', 'ZL10to50', 'ZJ', 'ZJ1', 'ZJ2', 'ZJ3', 'ZJ4', 'ZJ10to50'])
            hist.Group('ZL', ['ZL', 'ZL1', 'ZL2', 'ZL3', 'ZL4', 'ZL10to50'])
            hist.Group('ZJ', ['ZJ', 'ZJ1', 'ZJ2', 'ZJ3', 'ZJ4', 'ZJ10to50'])
            hist.Group('W', ['W', 'W1', 'W2', 'W3', 'W4'])
            hist.Group('TTT', ['TTLL', 'TTLJ', 'TTJJ'])
            hist.Group('TTJ', ['TTLL_J', 'TTLJ_J', 'TTJJ_J'])
#            hist.Group('TT', ['TTLL', 'TTLJ', 'TTJJ'])

            print hist

            self.comparisonPlots(hist, 'fig/' + self.channel + '/' + catname + '/' + self.channel + '_' + varname + '.gif', True)


            if varname in dcvar:
#            if dcvar:
#            if False:
                ensureDir('datacard/' + self.channel + '/' + catname)

                if self.dcname == None:
                    hist.WriteDataCard(filename='datacard/' + self.channel + '/' + catname + '/{}.root'.format(varname), dir='signal', mode='recreate')
                else:
                    hist.WriteDataCard(filename='datacard/' + self.channel + '/' + catname + '/' + self.dcname +'_{}.root'.format(varname), dir='signal', mode='recreate')



    def extractQCD(self, catname, exceptionList, vardir, os_ss_ratio = 1.):

        for varname, var in vardir.iteritems(): 

            h_QCD = None

            for processname, val in self.processes.iteritems():
                if processname in exceptionList: continue

                if processname.find('LQ')!=-1: 
                    continue
        
#                hname = 'hist_' + catname.replace('fakes','tau1_tight') + '_' + processname + '_' + varname
                hname = 'hist_' + catname + '_' + processname + '_' + varname
        
                addfactor = -1.
                if self.processes[processname]['name'] == 'data_obs':
                    addfactor = 1.
            
                if h_QCD == None:
                    h_QCD = copy.deepcopy(self.hists[hname])
                    h_QCD.Scale(addfactor)
                else:
                    h_QCD.Add(self.hists[hname], addfactor)

            
            h_QCD_os = copy.deepcopy(h_QCD)


            if self.channel in ['mutau', 'eletau']:
                h_QCD_os.Scale(os_ss_ratio)

#                osname = 'hist_' + catname.replace('_ss','_os').replace('fakes','tau1_tight') + '_QCD_' + varname
                osname = 'hist_' + catname.replace('_ss','_os') + '_QCD_' + varname
                h_QCD_os.SetName(osname)

                
            elif self.channel == 'tautau':

                ### Extracting loose->tight scaling factor

                if catname.find('os_loose')!=-1:

                    crname_loose = 'hist_' + catname.replace('signal','cr').replace('_os', '_ss') + '_QCD_' + varname
                    crname_tight = crname_loose.replace('loose', 'tight')
                    
                    if not self.hists.has_key(crname_loose):
                        print bcolors.BOLD + bcolors.FAIL + 'QCD: ' + crname_loose + ' is not exist' + bcolors.ENDC
                        
                    if not self.hists.has_key(crname_tight):
                        print bcolors.BOLD + bcolors.FAIL + 'QCD: ' + crname_tight + ' is not exist' + bcolors.ENDC


                    nloose = self.hists[crname_loose].GetSumOfWeights()
                    ntight = self.hists[crname_tight].GetSumOfWeights()

                    loose_tight_sf = 1.

                    if nloose!=0:
                        loose_tight_sf = ntight/nloose
                    else:
                        print bcolors.BOLD + bcolors.FAIL + 'loose_tight_sf founds 0 in denominator !' + bcolors.ENDC


#                print 'QCD SF (Loose, Tight) = ', nloose, ntight, ', SF = ', loose_tight_sf
                    h_QCD_os.Scale(loose_tight_sf)


                osname = 'hist_' + catname.replace('os_loose','os_tight') + '_QCD_' + varname
                h_QCD_os.SetName(osname)

            self.hists[osname] = h_QCD_os




    def comparisonPlots(self, hist, pname='sync.pdf', isRatio=True):
        display = DisplayManager(pname, isRatio, self.lumi, 0.42, 0.65)
        display.Draw(hist)


def ensureDir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)



def returnIntegral(hist):
    return hist.Integral(0, hist.GetNbinsX()+1)
