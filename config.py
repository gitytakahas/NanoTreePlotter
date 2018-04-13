import os, copy
from ROOT import TFile, TH1F, gROOT, Double
from DisplayManager import DisplayManager
from DataMCPlot import *
from array import array

gROOT.Macro('./functionmacro.C+')

import ConfigParser
import json


class config(object):

    def __init__(self, options):

        self.channel = options.channel
        
        print 'channel = ', self.channel

        self.hists = {}

        # read settings
        init = ConfigParser.SafeConfigParser() 
        init.read("./settings.ini")
        
        self.lumi = Double(init.get('settings', 'lumi'))
        self.basedir = init.get('settings', 'basedir')
        self.os_ss_ratio = Double(init.get('settings', 'os_ss_ratio'))

        print 'lumi = ', self.lumi
        print 'os_ss_ratio = ', self.os_ss_ratio

        # read processes (common for all channels)
        f = open('processes.json', 'r')
        self.processes = json.load(f)

#        print self.process


        self.dcname = None

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

        
        

        print '-'*80

#        for processname, val in self.process.iteritems():
        for processname, val in sorted(self.processes.iteritems()):

            if processname=='QCD': continue

#            print processname, val



            
            filename = self.basedir + val['file'] + '/' + options.channel + '.root'

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
                



#            print filename

            if not os.path.isfile(filename):
                print 'Register', processname.ljust(20), '[warning]', filename, 'does not exist ... skip !'
                self.processes.pop(processname, None)
                continue
            

            file = TFile(filename) 
            
            if not file.GetListOfKeys().Contains("tree"):
                print 'Register', processname.ljust(20), '[error] file (', filename , ') exits but broken ...'
                self.processes.pop(processname, None)


            if val['name']=='data_obs':
                rmflag = False
                if self.channel == 'mutau' and processname !='SingleMuon': rmflag = True
                if self.channel == 'etau' and processname !='SingleElectron':  rmflag = True
                if self.channel == 'tautau' and processname !='Tau':  rmflag = True

                if rmflag:
                    print 'Register', processname.ljust(20), '[info] file (', filename , ') removed as this is unnecessary for ' + self.channel + 'channel ...'
                    self.processes.pop(processname, None)
                    continue


#            print self.processes


                
            ntot = file.Get("h_cutflow").GetBinContent(1)
            

#            file = TFile(filename) 
            self.processes[processname]['ntot'] = ntot
            self.processes[processname]['file'] = file

            sf = self.processes[processname]['cross-section']*self.lumi*1000/self.processes[processname]['ntot']


            print 'Register', processname.ljust(20), str(int(self.processes[processname]['ntot'])).ljust(15), 'SF = ', '{0:.5f}'.format(sf).ljust(6), filename


#        print self.processes

        print '-'*80


        # DY stitching

        self.dy_xs = [4954.0, 1012.5, 332.8, 101.8, 54.8]

        self.dy_nlo_xs = 5765.4

        self.dykfactor = self.dy_nlo_xs/self.dy_xs[0]       

        print 'k-factor : DY = ', self.dykfactor, self.dy_nlo_xs, '(NLO) / ', self.dy_xs[0], '(LO)'

        self.dy_efflumi = []

        for ijet, processname in enumerate(['ZTT', 'ZTT1', 'ZTT2', 'ZTT3', 'ZTT4']):
            self.dy_efflumi.append(self.processes[processname]['ntot']/self.dy_xs[ijet])


        # calculate DY weight 

        self.dy_weight = []
        for ijet, processname in enumerate(['ZTT', 'ZTT1', 'ZTT2', 'ZTT3', 'ZTT4']):
            if processname=='ZTT':
                self.dy_weight.append(self.dykfactor*self.lumi*1000/self.dy_efflumi[ijet])
            else:
                self.dy_weight.append(self.dykfactor*self.lumi*1000/(self.dy_efflumi[0] + self.dy_efflumi[ijet]))


        self.dy_weightstr = '('

        for ii, _weight in enumerate(self.dy_weight):
            self.dy_weightstr += '(NUP==' + str(ii) + ' ? ' + str(self.dy_weight[ii]) + ': 1)*'


#        self.dy_weightstr += '1)'
        self.dy_weightstr = '1'
        print self.dy_weightstr


###        # W stitching 
###
###        self.w_xs = [50380, 9644.5, 3144.5, 954.8, 485.6]
###
###        self.w_nlo_xs = 61526.7
###
###        self.wkfactor = self.w_nlo_xs/self.w_xs[0]       
###
###        print 'k-factor : W = ', self.wkfactor, self.w_nlo_xs, '(NLO) / ', self.w_xs[0], '(LO)'
###
###        self.w_efflumi = []
###
###        for ijet, processname in enumerate(['W', 'W1', 'W2', 'W3', 'W4']):
###            self.w_efflumi.append(self.processes[processname]['ntot']/self.w_xs[ijet])
###
###
###        # calculate W weight 
###
###        self.w_weight = []
###        for ijet, processname in enumerate(['W', 'W1', 'W2', 'W3', 'W4']):
###            if processname=='W':
###                self.w_weight.append(self.wkfactor*self.lumi*1000/self.w_efflumi[ijet])
###            else:
###                self.w_weight.append(self.wkfactor*self.lumi*1000/(self.w_efflumi[0] + self.w_efflumi[ijet]))
###
###
###        self.w_weightstr= '('
###
###        for ii, _weight in enumerate(self.w_weight):
###            self.w_weightstr += '(NUP==' + str(ii) + ' ? ' + str(self.w_weight[ii]) + ': 1)*'
###
###
###        self.w_weightstr += '1)'
        self.w_weightstr = '1'
###        print self.w_weightstr
###
###



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


        weight = 'genWeight*' + str(self.processes[pname]['cross-section']*self.lumi*1000/self.processes[pname]['ntot'])  # + '*(gen_match_2==5 ? ' + str(tauidsf) + ' : 1)'

#        if self.topr=='up':
#            weight += '*1/ttptweight'
#        elif self.topr=='down':
#            weight += '*ttptweight'


        if pname in ['ZTT', 'ZTT1', 'ZTT2', 'ZTT3', 'ZTT4',
                           'ZL', 'ZL1', 'ZL2', 'ZL3', 'ZL4',
                           'ZJ', 'ZJ1', 'ZJ2', 'ZJ3', 'ZJ4']:            
            weight = 'genWeight*' + self.dy_weightstr  #+ '*(gen_match_2==5 ? ' + str(tauidsf) + ' : 1)'
#            if self.dmreweight:
#                weight += '*(decayMode_2 == 0 ? 0.961374351278 : 1.)*(decayMode_2 == 1 ? 1.01595247633 : 1.)*(decayMode_2 == 10 ? 1.0079651748 : 1.)'

        elif pname in ['W', 'W1', 'W2', 'W3', 'W4']:
            weight = 'genWeight*' + self.w_weightstr  #'*(gen_match_2==5 ? ' + str(tauidsf) + ' : 1)'

        elif self.processes[pname]['name'] == 'data_obs':
            weight = '1'
            

#        if self.channel == 'mutau':
#            if pname in ['SingleMuon']:
#                pass
#            else:
#                weight += '*getMuTrigWeight(pt_1, eta_1)'
#                weight += '*getTrackReco(eta_1)'

#        print val['name'], 'returnweight = ', weight
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
###########        self.W_lowMT = 50.
###########        self.W_highMT = 80.
###########

    def createHistograms(self, catname, selection, exceptionList, vardir, blind = False, sf_W = 1., dcvar = False):

        print '-'*80
        print 'category : ', catname
        print 'selection : ', selection
        print 'exceptionList : ', exceptionList
#        print 'vardir = ', vardir
        print 'SF for W = ', sf_W
        print '-'*80    

        for processname, val in self.processes.iteritems():
            if val['name'] in exceptionList: 
                print 'Remove', processname
                continue

        
#            tree = val['file'].Get('tree_' + self.channel + '_cut_relaxed')
            print 'processing', val['file']
            tree = val['file'].Get('tree')


            var_tuples = []
    
            for varname, var in vardir.iteritems():
#                print catname, processname, varname, var['drawname']
#                hname = 'hist_' + catname + '_' + processname + '_' + var['drawname']
                hname = 'hist_' + catname + '_' + processname + '_' + varname
#                if varname=='ht':
#                    hist_register = TH1F(hname, hname, len(binning)-1, array('d',binning))
#                else:
#                    hist_register = TH1F(hname, hname, var['nbins'], var['min'], var['max'])
       
                hist_register = TH1F(hname, hname, var['nbins'], var['min'], var['max'])
                hist_register.GetXaxis().SetTitle(var['label'])
                hist_register.GetXaxis().SetLabelSize(0)
                hist_register.Sumw2()
    
                if val['name'] == 'data_obs':
                    hist_register.SetMarkerStyle(20)
                    hist_register.SetMarkerSize(0.5)
        
                self.hists[hname] = hist_register

                var_tuples.append('{var} >> {hist}'.format(var=var['drawname'], hist=hname))

            weight = self.returnWeight(processname)
#            if processname in ['W', 'W1', 'W2', 'W3', 'W4']:
#                weight += '*' + str(sf_W)

#            print processname, weight
                
            if blind:
                weight += '*(isData==1 ? 0 : 1)'



            cutstr = selection + ' && ' + val['cut']
            cut = '({c}) * {we}'.format(c=cutstr, we=weight)

#            print tree, cut, var_tuples
            tree.MultiDraw(var_tuples, cut)

#            print processname, val, weight


        print 'making plots ...'
        
        ensureDir('fig/' + self.channel + '/' + catname)

#        print self.hists

        for varname, var in vardir.iteritems():        

            stackname = 'stackhist_' + catname + '_' + varname
            hist = DataMCPlot(stackname)
            hist.legendBorders = 0.55, 0.55, 0.88, 0.88

            for processname, val in self.processes.iteritems():

                hname = 'hist_' + catname + '_' + processname + '_' + varname
                if not self.hists.has_key(hname): continue

                pname = processname
                
                hist.AddHistogram(val['name'], self.hists[hname], val['order'])
                if val['name'] == 'data_obs' or val['name'].find('Signal')!=-1:
                    hist.Hist(val['name']).stack = False


#            hist.Group('Electroweak', ['WWTo1L1Nu2Q', 'WZTo3LNu', 'WZTo2L2Q', 'WZTo1L1Nu2Q', 'WZTo1L3Nu', 'ZZTo2Q2Nu', 'ZZTo2L2Q', 'ZZTo4L', 'ZZTo4Q', 'VVTo2L2Nu', 'ST_t_top', 'ST_t_antitop', 'ST_tw_top', 'ST_tw_antitop', 'ZTT', 'ZTT1', 'ZTT2', 'ZTT3', 'ZTT4','ZTT10to50', 'ZL', 'ZL1', 'ZL2', 'ZL3', 'ZL4', 'ZL10to50', 'ZJ', 'ZJ1', 'ZJ2', 'ZJ3', 'ZJ4', 'ZJ10to50', 'W', 'W1', 'W2', 'W3', 'W4'])
#            hist.Group('VV', ['WWTo1L1Nu2Q', 'WZTo3LNu', 'WZTo2L2Q', 'WZTo1L1Nu2Q', 'ZZTo2Q2Nu', 'ZZTo4L', 'ZZTo4Q', 'VVTo2L2Nu', 'ST_t_top', 'ST_t_antitop', 'ST_tw_top', 'ST_tw_antitop', 'ZZTo2L2Q', 'WZTo1L3Nu'])
            hist.Group('VV', ['WW', 'WZ', 'ZZ'])
            hist.Group('ST', ['ST_t_t', 'ST_t_tbar', 'ST_tw_t', 'ST_tw_tbar'])

            hist.Group('ZTT', ['ZTT', 'ZTT1', 'ZTT2', 'ZTT3', 'ZTT4','ZTT10to50'])
#            hist.Group('ZTT', ['ZTT', 'ZTT1', 'ZTT2', 'ZTT3', 'ZTT4','ZTT10to50', 'ZL', 'ZL1', 'ZL2', 'ZL3', 'ZL4', 'ZL10to50', 'ZJ', 'ZJ1', 'ZJ2', 'ZJ3', 'ZJ4', 'ZJ10to50'])
            hist.Group('ZL', ['ZL', 'ZL1', 'ZL2', 'ZL3', 'ZL4', 'ZL10to50'])
            hist.Group('ZJ', ['ZJ', 'ZJ1', 'ZJ2', 'ZJ3', 'ZJ4', 'ZJ10to50'])
            hist.Group('W', ['W', 'W1', 'W2', 'W3', 'W4'])
            hist.Group('TT', ['TTT', 'TTJ'])

            print hist

            if self.dcname==None:
                self.comparisonPlots(hist, 'fig/' + self.channel + '/' + catname + '/' + self.channel + '_' + varname + '.gif', True)

#            display = DisplayManager('fig_' + catname + '/' + stackname + '.gif', True, self.lumi, 0.42, 0.65)
#            display.Draw(hist)


#            if varname in dcvar:
#            if dcvar:
            if False:
                ensureDir('datacard/' + self.channel + '/' + catname)

                if self.dcname == None:
                    hist.WriteDataCard(filename='datacard/' + self.channel + '/' + catname + '/{}.root'.format(varname), dir='signal', mode='recreate')
                else:
                    hist.WriteDataCard(filename='datacard/' + self.channel + '/' + catname + '/' + self.dcname +'_{}.root'.format(varname), dir='signal', mode='recreate')


#            print varname
#            if varname=='decayMode_2' or varname.find('againstElectron')!=-1:
#
#                datahist = hist.Hist('data_obs')
#                ztthist = hist.Hist('ZTT')
#                zlhist = hist.Hist('ZL')
#                zjhist = hist.Hist('ZJ')
#                total_ndy = 0
#                total_ndy_rescaled = 0
#                dysf = {}
#
#                for ibin in range(1, ztthist.obj.GetXaxis().GetNbins()+1):
#                    ndy = ztthist.obj.GetBinContent(ibin) + zjhist.obj.GetBinContent(ibin) + zlhist.obj.GetBinContent(ibin)
#                    nmc_total = hist.returnTotal().weighted.GetBinContent(ibin)
#                    ndata = datahist.obj.GetBinContent(ibin)
#                    other_mc = nmc_total - ndy
#                    total_ndy += ndy
#                        
#                    if ndy !=0:
#                        dysf[ibin-1] = (ndata - other_mc)/ndy
#                        total_ndy_rescaled += (ndata - other_mc)
#                        print 'decay mode = ', ibin-1,' Total MC = ',  nmc_total, 'Total DY = ', ndy, 'other MC = ', other_mc, 'Data = ', ndata, ' SF = ', dysf[ibin-1]
#
#                rescale = total_ndy/total_ndy_rescaled
#                print 'DY yield: before rescaling = ', total_ndy, ', after rescaling =', total_ndy_rescaled, 'rescaling factor = ', rescale
#
#
#                print '-'*80
#                for decaymode, val in dysf.iteritems():
#                    print decaymode, 'SF = ', val*rescale
#                print '-'*80

#                print ztthist.Integral(0, ztthist.GetNbinsX()+1)
#                print zjhist.Integral(0, zjhist.GetNbinsX()+1)
#                print zlhist.Integral(0, zlhist.GetNbinsX()+1)
#
#                total_original = ztthist.Integral(0, ztthist.GetNbinsX()+1) + zjhist.Integral(0, zjhist.GetNbinsX()+1) + zlhist.Integral(0, zlhist.GetNbinsX()+1)

#                print 'original yield = ', total_original


                    
                    






    def extractQCD(self, catname, exceptionList, vardir):

        for varname, var in vardir.iteritems(): 

            h_QCD = None

            for processname, val in self.processes.iteritems():
                if processname in exceptionList: continue

                if processname.find('Signal')!=-1: 
#                    print processname, '(', val['name'], ') removed from extracting QCD shape !'
                    continue
        
                hname = 'hist_' + catname + '_' + processname + '_' + varname
#                print 'QCD = ', hname
        
                addfactor = -1.
                if self.processes[processname]['name'] == 'data_obs':
                    addfactor = 1.
            
                if h_QCD == None:
                    h_QCD = copy.deepcopy(self.hists[hname])
                    h_QCD.Scale(addfactor)
#                    print 'subtract', hname, self.hists[hname].Integral(0, self.hists[hname].GetNbinsX()+1)
#                    print 'subtract_copy', h_QCD.Integral(0, h_QCD.GetNbinsX()+1)
                else:
                    h_QCD.Add(self.hists[hname], addfactor)
#                print 'subtract', hname, self.hists[hname].Integral(0, self.hists[hname].GetNbinsX()+1)
#                print 'subtract_copy', h_QCD.Integral(0, h_QCD.GetNbinsX()+1)

            
            h_QCD_os = copy.deepcopy(h_QCD)
            h_QCD_os.Scale(self.os_ss_ratio)

            osname = 'hist_' + catname.replace('_ss','_os') + '_QCD_' + varname
            h_QCD_os.SetName(osname)

#            entries = h_QCD.Integral(0, h_QCD_os.GetNbinsX()+1)
#            print '-'*80
#            print 'Original yield = ', h_QCD.Integral(0, h_QCD_os.GetNbinsX()+1)
#        #        print 'OS/SS ratio = ', os_ss_ratio
#            print 'Estimated QCD yield at ', catname, ' : ', h_QCD_os.Integral(0, h_QCD_os.GetNbinsX()+1)
#            print '-'*80

            self.hists[osname] = h_QCD_os




    def comparisonPlots(self, hist, pname='sync.pdf', isRatio=True):
        display = DisplayManager(pname, isRatio, self.lumi, 0.42, 0.65, [])
        display.Draw(hist)


def ensureDir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)



