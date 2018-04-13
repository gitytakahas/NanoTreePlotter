import os, math, copy, sys, collections
from ROOT import gStyle, TCanvas, TLegend, TH1F
from officialStyle import officialStyle
from config import *
import MultiDraw


from optparse import OptionParser, OptionValueError
usage = "usage: python draw.py [tes: 30, m30 (default : None)] [w_scale: 1.1, 0.9 (default : 1)]"
parser = OptionParser(usage)


#parser.add_option(
#    "-r", "--topr", 
#    default=None,
#    type="string",
#    help="top pt reweighting variation (TT_noreweight, doubletopptreweight)",
#    dest="topr"
#    )
#
#
parser.add_option(
    "-c", "--channel", 
    default="mutau",
    type="string",
    help="channel",
    dest="channel"
    )
#
#
#parser.add_option(
#    "-t", "--tes", 
#    default=None,
#    type="string",
#    help="tau energy scale variation (m30, 30)",
#    dest="tes"
#    )
#
#parser.add_option(
#    "-j", "--jtes", 
#    default=None,
#    type="string",
#    help="jet -> tau energy scale variation (m0p1, 0p1)",
#    dest="jtes"
#    )
#
#parser.add_option(
#    "-s", "--shape", 
#    default=None,
#    type="string",
#    help="tau ID (up, down)",
#    dest="tid"
#    )
#
#parser.add_option(
#    "-u", "--jtf",
#    default=None,
#    type="string",
#    help="jet->tau fake rate (up, down)",
#    dest="jtf"
#    )
#
#parser.add_option(
#    "-e", "--ees", 
#    default=None,
#    type="string",
#    help="Electron energy scale variation (up, down)",
#    dest="ees"
#    )
#
#parser.add_option(
#    "-l", "--ltf", 
#    default=None,
#    type="string",
#    help="lep to tau up/down variation (up, down)",
#    dest="ltf"
#    )
#
#parser.add_option(
#    "-w", "--wscale",
#    default=None,
#    type="float",
#    help="additional W_scaling for the systematic evaluation (1.1, 0.9)",
#    dest="w_scale"
#    )
#
#parser.add_option(
#    "-d", "--decaymode",
#    default=None,
#    type="int",
#    help="decay mode restrictions: [0,1,10]",
#    dest="decaymode"
#    )
#
#parser.add_option(
#    "-i", "--isolation",
#    default="iso_2",
#    type="string",
#    help="isolation requirement for the tau [iso_2_vloose, iso_2_loose, iso_2_medium, iso_2, iso_2_vtight, iso_2_vvtight]",
#    dest="isolation"
#    )
#
#
#parser.add_option(
#    "-m", "--mid", 
#    default=None,
#    type="string",
#    help="tau energy scale variation (up, down)",
#    dest="mid"
#    )
#
#
#
(options, args) = parser.parse_args()


gROOT.SetBatch(True)
officialStyle(gStyle)
gStyle.SetOptTitle(0)


#config = config(basedir, lumi, options.tes, options.ltf, options.ees, options.jtes, options.tid, options.jtf, options.topr, dcname, options.channel)
#config = config(options.tes, options.ees, options.mid, options.tid, options.jtf, options.topr, options.channel)
config = config(options)
#process = config.process
#W_highMT = config.W_highMT

#sys.exit(0)

baseselection = '1'
#'iso_2==1 && pt_2 > 50 && pt_1 > 50'
##baseselection = 'iso_2==1'
#
#if options.channel=='etau':
##    pass
#    baseselection += '&& againstElectronTightMVA6_2==1 && againstMuonLoose3_2==1'
#elif options.channel=='mutau':
#    baseselection += '&& againstElectronVLooseMVA6_2==1 && againstMuonTight3_2==1'
##    pass
#
#baseselection += '&& jpt_1 > 50 && m_vis > 85'

print 'base selection = ', baseselection


################################################################################
### First, evaluate W SF
#
#catname = 'highMT_ss'
#sel_highMT_ss = baseselection + ' && pfmt_1 > ' + str(W_highMT) + ' && q_1*q_2 > 0'
#
#var_pfmt_1 = {
#    'pfmt_1':{'drawname':'pfmt_1', 'nbins':40, 'min':0, 'max':200, 'label':'PF MET Transverse mass (GeV)'},
#    }
#
#config.createHistograms(catname, sel_highMT_ss, ['QCD'], var_pfmt_1)
#config.extractQCD(catname, ['QCD'], var_pfmt_1, os_ss_ratio)
#
#
#################################################################################
#
#catname = 'highMT_os'
#sel_highMT_os = baseselection + ' && pfmt_1 > ' + str(W_highMT) + ' && q_1*q_2 < 0'
#
#config.createHistograms(catname, sel_highMT_os, ['QCD'], var_pfmt_1)
#
#h_W_dd = None
#h_W_mc = None
#
#for processname, val in process.iteritems():
#        
#    if processname.find('Signal')!=-1: continue
#
#    hname = 'hist_' + catname + '_' + processname + '_pfmt_1'
#
#    if processname in ['W', 'W1', 'W2', 'W3', 'W4']:
#        if h_W_mc == None:
#            h_W_mc = copy.deepcopy(config.hists[hname])
#        else:
#            h_W_mc.Add(config.hists[hname])
#    else:
#        addfactor = -1
#        if val['name'] == 'data_obs':
#            addfactor = 1.
#            
#        if h_W_dd == None:
#            h_W_dd = copy.deepcopy(config.hists[hname])
#            h_W_dd.Scale(addfactor)
#        else:
#            h_W_dd.Add(config.hists[hname], addfactor)
#
#print 'W_yield, measured in data = ', returnIntegral(h_W_dd)
#print 'W_yield, measured in mc = ', returnIntegral(h_W_mc)
#
sf_W = 1.
#if returnIntegral(h_W_mc)!=0:
#    sf_W = returnIntegral(h_W_dd)/returnIntegral(h_W_mc)
#
#if options.w_scale!=None:
#    sf_W *= options.w_scale
#
#print 'W_yield SF = ', sf_W

#sf_W = 1.
#sf_W = 1.224
#sf_W = 0.812207330091
#sf_W = 1.04
#sf_W = 1.01483221298




##############################################################################


vardir = {
    # NOMINAL
#    'npv':{'drawname':'npv', 'nbins':80, 'min':0, 'max':80, 'label':'Nvertices'},
#    'm_vis':{'drawname':'m_vis', 'nbins':9, 'min':40, 'max':85, 'label':'visible mass (GeV)'},
#    'm_vis':{'drawname':'m_vis', 'nbins':40, 'min':0, 'max':200, 'label':'visible mass (GeV)'},
    'm_taub':{'drawname':'m_taub', 'nbins':50, 'min':0, 'max':1500, 'label':'mass (#tau + b) (GeV)'},
    'm_mub':{'drawname':'m_mub', 'nbins':50, 'min':0, 'max':1500, 'label':'mass (lepton + b) (GeV)'},
    'm_muj':{'drawname':'m_muj', 'nbins':50, 'min':0, 'max':1500, 'label':'mass (lepton + j) (GeV)'},
    'm_coll_muj':{'drawname':'m_coll_muj', 'nbins':50, 'min':0, 'max':2000, 'label':'collinear mass (lepton + j) (GeV)'},
    'm_coll_tauj':{'drawname':'m_coll_tauj', 'nbins':50, 'min':0, 'max':2000, 'label':'collinear mass (#tau + j) (GeV)'},
    'm_max_coll':{'drawname':'max(m_coll_muj, m_coll_tauj)', 'nbins':50, 'min':0, 'max':2000, 'label':'max. of collinear mass (lepton + j, #tau + j) (GeV)'},
    'm_tauj':{'drawname':'m_tauj', 'nbins':50, 'min':0, 'max':1500, 'label':'mass (#tau + j) (GeV)'},
#    'm_vis':{'drawname':'m_vis', 'nbins':15, 'min':40, 'max':85, 'label':'visible mass (GeV)'},
#    'm_vis':{'drawname':'m_vis', 'nbins':5, 'min':40, 'max':85, 'label':'visible mass (GeV)'},
#    'm_vis':{'drawname':'m_vis', 'nbins':9, 'min':42.5, 'max':87.5, 'label':'visible mass (GeV)'},
#    'm_vis':{'drawname':'m_vis', 'nbins':12, 'min':30, 'max':90, 'label':'visible mass (GeV)'},
    'm_vis':{'drawname':'m_vis', 'nbins':30, 'min':0, 'max':1500, 'label':'visible mass (GeV)'},
    'm_vis_zoom':{'drawname':'m_vis', 'nbins':30, 'min':0, 'max':150, 'label':'visible mass (GeV)'},
    'pfmt_1':{'drawname':'pfmt_1', 'nbins':30, 'min':0, 'max':250, 'label':'mT (lepton, met) (GeV)'},
    'pfmt_2':{'drawname':'pfmt_2', 'nbins':30, 'min':0, 'max':250, 'label':'mT (tau, met)(GeV)'},
#    'pfmt_1':{'drawname':'pfmt_1', 'nbins':20, 'min':0, 'max':260, 'label':'PF MET Transverse mass (GeV)'},
#    'mt_1':{'drawname':'mt_1', 'nbins':40, 'min':0, 'max':200, 'label':'MVA MET Transverse mass (GeV)'},
    'met':{'drawname':'met', 'nbins':30, 'min':0, 'max':1000, 'label':'missing E_{T} (GeV)'},
    'met_fine':{'drawname':'met', 'nbins':30, 'min':0, 'max':500, 'label':'missing E_{T} (GeV)'},
    'dR_ll':{'drawname':'dR_ll', 'nbins':30, 'min':0, 'max':2*math.pi, 'label':'#Delta R (l, #tau)'},
#    'p_1':{'drawname':'muP(pt_1, eta_1, phi_1, m_1)', 'nbins':60, 'min':0, 'max':1000, 'label':'lepton p (GeV)'},
#    'p_1_wide':{'drawname':'muP(pt_1, eta_1, phi_1, m_1)', 'nbins':60, 'min':0, 'max':2000, 'label':'lepton p (GeV)'},
    'pt_1':{'drawname':'pt_1', 'nbins':30, 'min':0, 'max':500, 'label':'lepton pT (GeV)'},
    'pt_1_wide':{'drawname':'pt_1', 'nbins':60, 'min':0, 'max':1000, 'label':'lepton pT (GeV)'},
    'pt_1_wide_2':{'drawname':'pt_1', 'nbins':60, 'min':0, 'max':2000, 'label':'lepton pT (GeV)'},
    'pt_1_zoom':{'drawname':'pt_1', 'nbins':30, 'min':0, 'max':150, 'label':'lepton pT (GeV)'},
    'pt_2_zoom':{'drawname':'pt_2', 'nbins':30, 'min':0, 'max':150, 'label':'tau pT (GeV)'},
    'max_pt':{'drawname':'max(pt_1, pt_2)', 'nbins':50, 'min':0, 'max':1000, 'label':'max lepton pT (GeV)'},
    'pt_asymm':{'drawname':'abs((pt_1 - pt_2)/(pt_1 + pt_2))', 'nbins':30, 'min':0., 'max':1., 'label':'lepton - tau pT asymm.'},
    'abs_pt_asymm':{'drawname':'abs(pt_1 - pt_2)', 'nbins':50, 'min':0., 'max':1000., 'label':'lepton - tau pT abs. asymm.'},
#    'pt_ratio':{'drawname':'pt_1/pt_2', 'nbins':30, 'min':0, 'max':1000., 'label':'lepton pT / tau pT'},
    'iso_1':{'drawname':'iso_1', 'nbins':30, 'min':0, 'max':0.15, 'label':'lepton relative isolation'},
    'ht':{'drawname':'pt_1+pt_2+jpt_1', 'nbins':50, 'min':150, 'max':2150, 'label':'scalar sum pT (GeV)'},
    'ht_bjet':{'drawname':'pt_1+pt_2+bpt_1', 'nbins':50, 'min':150, 'max':2150, 'label':'scalar sum pT with b-jet (GeV)'},

    'ht_red':{'drawname':'pt_1+pt_2+jpt_1', 'nbins':40, 'min':0, 'max':2000, 'label':'scalar sum pT (GeV)'},
    'ht_red2':{'drawname':'pt_1+pt_2+jpt_1', 'nbins':30, 'min':0, 'max':2000, 'label':'scalar sum pT (GeV)'},
    'ht_dis2':{'drawname':'pt_1+pt_2+jpt_1', 'nbins':30, 'min':0, 'max':1000, 'label':'Scalar sum pT (GeV)'},
    'ht_dis':{'drawname':'pt_1+pt_2+jpt_1', 'nbins':40, 'min':0, 'max':1000, 'label':'Scalar sum pT (GeV)'},
#    'ht_1':{'drawname':'pt_1+pt_2+jpt_1', 'nbins':20, 'min':0, 'max':1200, 'label':'scalar sum pT (GeV)'},
#    'ht_2':{'drawname':'pt_1+pt_2+jpt_1', 'nbins':40, 'min':0, 'max':1200, 'label':'scalar sum pT (GeV)'},
#    'ht_3':{'drawname':'pt_1+pt_2+jpt_1', 'nbins':50, 'min':0, 'max':1200, 'label':'scalar sum pT (GeV)'},



    'st':{'drawname':'pt_1+pt_2+jpt_1+met', 'nbins':40, 'min':0, 'max':2000, 'label':'H_{T} (GeV)'},
    'st_red':{'drawname':'pt_1+pt_2+jpt_1+met', 'nbins':30, 'min':0, 'max':2000, 'label':'sT (GeV)'},
    'st_ext':{'drawname':'pt_1+pt_2+jpt_1+met', 'nbins':50, 'min':0, 'max':2500, 'label':'sT (GeV)'},
    'm_max1':{'drawname':'max(m_mub,m_taub)', 'nbins':50, 'min':0, 'max':1500, 'label':'max. mass (#tau + b, lepton + b) (GeV)'},
    'm_max2':{'drawname':'max(m_muj,m_tauj)', 'nbins':50, 'min':0, 'max':1500, 'label':'max. mass (#tau + j, lepton + j) (GeV)'},
#    'm_max_lj':{'drawname':'m_max_lj', 'nbins':50, 'min':0, 'max':1500, 'label':'max_lj (GeV)'},
    'm_max_lb':{'drawname':'m_max_lb', 'nbins':50, 'min':0, 'max':1500, 'label':'max_lb (GeV)'},
#    'pt_2':{'drawname':'pt_2', 'nbins':30, 'min':0, 'max':100, 'label':'tau pT (GeV)'},
    'pt_2':{'drawname':'pt_2', 'nbins':30, 'min':0, 'max':500, 'label':'tau pT (GeV)'},
#    'dz_2':{'drawname':'dz_2', 'nbins':25, 'min':0, 'max':0.2, 'label':'tau dZ (cm)'},
#    'pt_2':{'drawname':'pt_2', 'nbins':1000, 'min':0, 'max':1000, 'label':'tau pT (GeV)'},
#    'm_2':{'drawname':'m_2', 'nbins':8, 'min':0, 'max':1.6, 'label':'tau mass (GeV)'},
#    'm_2':{'drawname':'m_2', 'nbins':20, 'min':0, 'max':1.6, 'label':'tau mass (GeV)'},
#    'm_2':{'drawname':'m_2', 'nbins':16, 'min':0, 'max':1.6, 'label':'tau mass (GeV)'},
#    'm_2':{'drawname':'m_2', 'nbins':16, 'min':0.05, 'max':1.65, 'label':'tau mass (GeV)'},
    'decayMode_2':{'drawname':'decayMode_2', 'nbins':11, 'min':0, 'max':11, 'label':'tau decay Mode'},
    'gen_match_2':{'drawname':'gen_match_2', 'nbins':7, 'min':0, 'max':7, 'label':'gen_match_2'},
#    'gen_match_2':{'drawname':'gen_match_2', 'nbins':1, 'min':5, 'max':6, 'label':'gen_match_2'},
    'eta_1':{'drawname':'eta_1', 'nbins':30, 'min':-2.5, 'max':2.5, 'label':'lepton eta'},
    'eta_2':{'drawname':'eta_2', 'nbins':30, 'min':-2.5, 'max':2.5, 'label':'tau eta'},
    'njets':{'drawname':'njets', 'nbins':10, 'min':0, 'max':10, 'label':'# of jets (pT > 30)'},
#    'njets_eta3':{'drawname':'njets_eta3', 'nbins':10, 'min':0, 'max':10, 'label':'# of jets (pT > 30, |#eta| < 3.0)'},
    'dphi_ll':{'drawname':'fabs(dphi_ll)', 'nbins':30, 'min':0, 'max':math.pi, 'label':'#Delta#phi(tau, lepton)'},
    'nbtag':{'drawname':'nbtag', 'nbins':6, 'min':0, 'max':6, 'label':'# of b-jets'},
#    'nfjets':{'drawname':'nfjets', 'nbins':10, 'min':0, 'max':10, 'label':'# of forward jets (pT > 30)'},
#    'byIsolationMVA3oldDMwLTraw_2':{'drawname':'byIsolationMVA3oldDMwLTraw_2', 'nbins':40, 'min':-1, 'max':1, 'label':'Tau MVA isolation'},
#    'byIsolationMVA3oldDMwLTraw_zoom_2':{'drawname':'byIsolationMVA3oldDMwLTraw_2', 'nbins':20, 'min':0.8, 'max':1, 'label':'Tau MVA isolation (zoom)'},
    'byIsolationMVA3oldDMwLTraw_morezoom_2':{'drawname':'byIsolationMVA3oldDMwLTraw_2', 'nbins':40, 'min':0.9, 'max':1, 'label':'Tau MVA isolation (zoom)'},
    'dphi_met_leg1':{'drawname':'abs(deltaPhi(phi_1, metphi))', 'nbins':40, 'min':0., 'max':math.pi, 'label':'#Delta#phi (lepton, MET)'},
    'dphi_met_leg2':{'drawname':'abs(deltaPhi(phi_2, metphi))', 'nbins':40, 'min':0., 'max':math.pi, 'label':'#Delta#phi (tau, MET)'},

#    'byIsolationMVArun2v1DBoldDMwLTrawNew_2':{'drawname':'byIsolationMVArun2v1DBoldDMwLTrawNew_2', 'nbins':40, 'min':-1, 'max':1, 'label':'New Tau MVA isolation'},
#    'byIsolationMVArun2v1DBoldDMwLTrawNew_2':{'drawname':'byIsolationMVArun2v1DBoldDMwLTrawNew_2', 'nbins':20, 'min':0.8, 'max':1, 'label':'New Tau MVA isolation (zoom)'},
#    'byIsolationMVArun2v1DBoldDMwLTrawNew_2':{'drawname':'byIsolationMVArun2v1DBoldDMwLTrawNew_2', 'nbins':40, 'min':0.9, 'max':1, 'label':'New Tau MVA isolation (zoom)'},
#    'nPhoton_2':{'drawname':'nPhoton_2', 'nbins':26, 'min':-0.5, 'max':25.5, 'label':'Number of photons'},
#    'ptWeightedDetaStrip_2':{'drawname':'ptWeightedDetaStrip_2', 'nbins':30, 'min':0, 'max':0.5, 'label':'pT weighted strip #Delta#eta'},
#    'ptWeightedDphiStrip_2':{'drawname':'ptWeightedDphiStrip_2', 'nbins':30, 'min':0, 'max':0.5, 'label':'pT weighted strip #Delta#phi'},
#    'ptWeightedDrSignal_2':{'drawname':'ptWeightedDrSignal_2', 'nbins':30, 'min':0, 'max':0.1, 'label':'pT weighted signal #DeltaR'},
#    'ptWeightedDrIsolation_2':{'drawname':'ptWeightedDrIsolation_2', 'nbins':30, 'min':0, 'max':0.5, 'label':'pT weighted isolation #DeltaR'},
#    'leadingTrackChi2_2':{'drawname':'leadingTrackChi2_2', 'nbins':30, 'min':0, 'max':20, 'label':'leading track #chi^{2}'},
#    'leadingTrackPt_2':{'drawname':'leadingTrackPt_2', 'nbins':30, 'min':0, 'max':150, 'label':'leading track pT'},
#    'eRatio_2':{'drawname':'eRatio_2', 'nbins':30, 'min':0, 'max':1, 'label':'eRatio'},
#    'dxy_Sig_2':{'drawname':'dxy_Sig_2', 'nbins':30, 'min':-30, 'max':30, 'label':'dxy significance'},
#    'ip3d_2':{'drawname':'ip3d_2', 'nbins':30, 'min':-0.03, 'max':0.03, 'label':'IP3D'},
#    'ip3d_Sig_2':{'drawname':'ip3d_Sig_2', 'nbins':30, 'min':-30, 'max':30, 'label':'IP3D significance'},
#    'hasSecondaryVertex_2':{'drawname':'hasSecondaryVertex_2', 'nbins':2, 'min':0, 'max':2, 'label':'hasSecondaryVertex'},
#    'decayDistMag_2':{'drawname':'decayDistMag_2', 'nbins':30, 'min':0, 'max':10, 'label':'decay dist mag.'},
#    'flightLenthSig_2':{'drawname':'flightLenthSig_2', 'nbins':30, 'min':-25, 'max':100, 'label':'flight length significance'},
#    'byCombinedIsolationDeltaBetaCorrRaw3Hits_2':{'drawname':'byCombinedIsolationDeltaBetaCorrRaw3Hits_2', 'nbins':30, 'min':0, 'max':200, 'label':'Tau dbeta isolation'},
#    'iso_2_loose_id':{'drawname':'iso_2_loose_id', 'nbins':2, 'min':0, 'max':2, 'label':'cut-based loose ID'},
#    'iso_2_medium_id':{'drawname':'iso_2_medium_id', 'nbins':2, 'min':0, 'max':2, 'label':'cut-based medium ID'},
#    'iso_2_tight_id':{'drawname':'iso_2_tight_id', 'nbins':2, 'min':0, 'max':2, 'label':'cut-based tight ID'},
    'iso_2_vloose':{'drawname':'iso_2_vloose', 'nbins':2, 'min':0, 'max':2, 'label':'MVA ID VLoose'},
    'iso_2_loose':{'drawname':'iso_2_loose', 'nbins':2, 'min':0, 'max':2, 'label':'MVA ID Loose'},
    'iso_2_medium':{'drawname':'iso_2_medium', 'nbins':2, 'min':0, 'max':2, 'label':'MVA ID Medium'},
    'iso_2':{'drawname':'iso_2', 'nbins':2, 'min':0, 'max':2, 'label':'MVA ID Tight'},
    'iso_2_vtight':{'drawname':'iso_2_vtight', 'nbins':2, 'min':0, 'max':2, 'label':'MVA ID VTight'},
    'iso_2_vvtight':{'drawname':'iso_2_vvtight', 'nbins':2, 'min':0, 'max':2, 'label':'MVA ID VVTight'},
    'jpt_1':{'drawname':'jpt_1', 'nbins':30, 'min':0, 'max':500, 'label':'leading jet pT (GeV)'},
    'jpt_1_wide':{'drawname':'jpt_1', 'nbins':50, 'min':0, 'max':1000, 'label':'leading jet pT (GeV)'},
#    'jpt_1_zoom':{'drawname':'jpt_1', 'nbins':30, 'min':0, 'max':150, 'label':'leading jet pT (GeV)'},
#    'jeta_1':{'drawname':'jeta_1', 'nbins':30, 'min':-5, 'max':5, 'label':'leading jet eta'},
    'jpt_2':{'drawname':'jpt_2', 'nbins':30, 'min':0, 'max':500, 'label':'sub leading jet pT (GeV)'},
#    'jeta_2':{'drawname':'jeta_2', 'nbins':30, 'min':-5, 'max':5, 'label':'sub leading jet eta'},
#    'pzeta_disc':{'drawname':'pzeta_disc', 'nbins':30, 'min':-25, 'max':100, 'label':'pZeta discriminator'},
    'pzeta_disc':{'drawname':'pzeta_disc', 'nbins':40, 'min':-250, 'max':150, 'label':'pZeta discriminator'},
    'againstElectronVLooseMVA6_2':{'drawname':'againstElectronVLooseMVA6_2', 'nbins':2, 'min':0, 'max':2, 'label':'againstElectronVLooseMVA6'},
    'againstElectronLooseMVA6_2':{'drawname':'againstElectronLooseMVA6_2', 'nbins':2, 'min':0, 'max':2, 'label':'againstElectronLooseMVA6'},
    'againstElectronMediumMVA6_2':{'drawname':'againstElectronMediumMVA6_2', 'nbins':2, 'min':0, 'max':2, 'label':'againstElectronMediumMVA6'},
    'againstElectronTightMVA6_2':{'drawname':'againstElectronTightMVA6_2', 'nbins':2, 'min':0, 'max':2, 'label':'againstElectronTightMVA6'},
    'againstElectronVTightMVA6_2':{'drawname':'againstElectronVTightMVA6_2', 'nbins':2, 'min':0, 'max':2, 'label':'againstElectronVTightMVA6'},
    'againstMuonLoose3_2':{'drawname':'againstMuonLoose3_2', 'nbins':2, 'min':0, 'max':2, 'label':'againstMuonLoose3_2'},
    'againstMuonTight3_2':{'drawname':'againstMuonTight3_2', 'nbins':2, 'min':0, 'max':2, 'label':'againstMuonTight3_2'},
#    'ntop':{'drawname':'ntop', 'nbins':5, 'min':0, 'max':5, 'label':'number of reconstructed tops'},
#    'photonPtSumOutsideSignalCone_2':{'drawname':'photonPtSumOutsideSignalCone_2', 'nbins':20, 'min':0, 'max':15, 'label':'photonPtSumOutsideSignalCone_2'},
#    'photonPtSumOutsideSignalCone_2':{'drawname':'photonPtSumOutsideSignalCone_2', 'nbins':50, 'min':0, 'max':5, 'label':'photonPtSumOutsideSignalCone_2 (zoom)'},
#    'AbsphotonPtSumOutsideSignalCone_2':{'drawname':'photonPtSumOutsideSignalCone_2*pt_2', 'nbins':30, 'min':0, 'max':250, 'label':'abs. photonPtSumOutsideSignalCone'},
#    'chargedIsoPtSum_2':{'drawname':'chargedIsoPtSum_2', 'nbins':30, 'min':0, 'max':250, 'label':'chargedIsoPtSum_2'},
#    'neutralIsoPtSum_2':{'drawname':'neutralIsoPtSum_2', 'nbins':30, 'min':0, 'max':2, 'label':'neutralIsoPtSum_2'},
#    'puCorrPtSum_2':{'drawname':'puCorrPtSum_2', 'nbins':30, 'min':0, 'max':250, 'label':'puCorrPtSum_2'},
#    'chargedIsoPtSum_zoom_2':{'drawname':'chargedIsoPtSum_2', 'nbins':30, 'min':0, 'max':2, 'label':'chargedIsoPtSum_2 (Zoom)'},
#    'neutralIsoPtSum_zoom_2':{'drawname':'neutralIsoPtSum_2', 'nbins':30, 'min':0, 'max':2, 'label':'neutralIsoPtSum_2 (Zoom)'},
#    'd0_2':{'drawname':'d0_2', 'nbins':40, 'min':-0.01, 'max':0.01, 'label':'d0_2'},
#    'chargedPionPt_2':{'drawname':'chargedPionPt_2', 'nbins':30, 'min':0, 'max':150, 'label':'chargedPionPt_2'},
#    'neutralPionPt_2':{'drawname':'neutralPionPt_2', 'nbins':30, 'min':0, 'max':150, 'label':'neutralPionPt_2'},


    }

vardir = {
    'pt_2':{'drawname':'pt_2', 'nbins':30, 'min':0, 'max':500, 'label':'tau pT (GeV)'},
    'm_vis_zoom':{'drawname':'m_vis', 'nbins':30, 'min':0, 'max':150, 'label':'visible mass (GeV)'},
}

categories = collections.OrderedDict()
categories['inclusive'] = {'sel':baseselection}
#categories['nominal_btag'] = {'sel':baseselection + ' && bpt_1 > 50'}

for catid, cat in categories.iteritems(): 

    catname = 'signal_ss_' + catid
    sel_signal_ss = cat['sel'] + ' && charge_1*charge_2 > 0'
#    sel_signal_ss = cat['sel'] + '&& pfmt_1 < 40 && pzeta_disc > -25 && nbtag==0 && q_1*q_2 > 0 && m_vis > 45 && m_vis < 85 && pt_2 > 30'
#    sel_signal_ss = cat['sel'] + '&& pfmt_1 > 50 && nbtag ==0 &&  q_1*q_2 > 0 && !(m_vis > 40 && m_vis < 105) && njets==0'

    config.createHistograms(catname, sel_signal_ss, ['QCD'], vardir, False, sf_W)
    config.extractQCD(catname, ['QCD'], vardir)

    catname = 'signal_os_' + catid
    sel_signal_os = sel_signal_ss.replace('charge_1*q_2 > 0', 'charge_1*q_2 < 0')
        

    if catid.find('btag')!=-1 and catid.find('nobtag')==-1:
        # blinded
#        config.createHistograms(catname, sel_signal_os, ['QCD'], vardir, True, sf_W, True)
        config.createHistograms(catname, sel_signal_os, ['QCD'], vardir, False, sf_W, True)
    else:
        config.createHistograms(catname, sel_signal_os, ['QCD'], vardir, False, sf_W, True)
