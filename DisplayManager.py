import ROOT
import copy

def add_lumi(luminumber):
    lowX=0.6
    lowY=0.842
    lumi  = ROOT.TPaveText(lowX, lowY+0.06, lowX+0.30, lowY+0.16, "NDC")
    lumi.SetBorderSize(   0 )
    lumi.SetFillStyle(    0 )
    lumi.SetTextAlign(   12 )
    lumi.SetTextColor(    1 )
    lumi.SetTextSize(0.05)
    lumi.SetTextFont (   42 )
    lumi.AddText("2016, " + str(luminumber) + " fb^{-1} (13TeV)")
    return lumi


def add_CMS():
    lowX=0.12
    lowY=0.848
    lumi  = ROOT.TPaveText(lowX, lowY+0.06, lowX+0.15, lowY+0.16, "NDC")
    lumi.SetTextFont(61)
    lumi.SetTextSize(0.055)
    lumi.SetBorderSize(   0 )
    lumi.SetFillStyle(    0 )
    lumi.SetTextAlign(   12 )
    lumi.SetTextColor(    1 )
    lumi.AddText("CMS")
    return lumi


def add_Preliminary():
    lowX=0.21
    lowY=0.84
    lumi  = ROOT.TPaveText(lowX, lowY+0.06, lowX+0.15, lowY+0.16, "NDC")
#    lumi.SetTextFont(52)
    lumi.SetTextSize(0.055)
    lumi.SetBorderSize(   0 )
    lumi.SetFillStyle(    0 )
    lumi.SetTextAlign(   12 )
    lumi.SetTextColor(    1 )
#    lumi.AddText("#it{Simulation} Preliminary")
    lumi.AddText("#it{Preliminary}")
    return lumi

def createRatioCanvas(name, errorBandFillColor=14, errorBandStyle=3354):
    cv = ROOT.TCanvas(name.replace('.pdf', ''), name.replace('.pdf', ''), 10, 10, 600, 600)

    # this is the tricky part...
    # Divide with correct margins
    cv.Divide(1, 2, 0.0, 0.0)

    # Set Pad sizes
    cv.GetPad(1).SetPad(0.0, 0.32, 1., 1.0)
    cv.GetPad(2).SetPad(0.0, 0.00, 1., 0.34)

    cv.GetPad(1).SetFillStyle(4000)
    cv.GetPad(2).SetFillStyle(4000)

    # Set pad margins 1
    cv.cd(1)
#    cv.cd(1).SetLogy()
    ROOT.gPad.SetTopMargin(0.1)
    ROOT.gPad.SetLeftMargin(0.12)
    ROOT.gPad.SetBottomMargin(0.03)
    ROOT.gPad.SetRightMargin(0.08)

    # Set pad margins 2
    cv.cd(2)
    ROOT.gPad.SetBottomMargin(0.35)
    ROOT.gPad.SetLeftMargin(0.12)
    ROOT.gPad.SetRightMargin(0.08)

    bogyHist = ROOT.TH1F("PseudoHist", "", 1, 1., 2.)
    bogyHist.SetFillColor(errorBandFillColor)
    bogyHist.SetFillStyle(errorBandStyle)
    bogyHist.SetLineColor(0)

    cv.cd(1)
    return cv


class DisplayManager(object):

    def __init__(self, name, ratio, lumi, xmin=0.42, ymin=0.6, arrows = []):

        if ratio:
            self.canvas = createRatioCanvas(name.replace('pdf', ''))
        else:
            self.canvas = ROOT.TCanvas(name.replace('.pdf', ''))

        self.lumi = lumi
        self.name = name
        self.draw_ratio = ratio
        self.histo = None
#        self.histos = []
        self.pullRange = 0.5

        self.adapt = ROOT.gROOT.GetColor(12)
#        self.new_idx = ROOT.gROOT.GetListOfColors().GetSize() + 1
        self.new_idx = 2001
        self.trans = ROOT.TColor(self.new_idx, self.adapt.GetRed(), self.adapt.GetGreen(), self.adapt.GetBlue(), "",0.5)

        self.arrows = arrows

    def Draw(self, histo):


        self.histo = histo
#        self.histo.DrawStack('HIST', None, None, None, None, 2)

#        self.histos = histos
        self.data = self.histo.Hist('data_obs')
        self.total = self.histo.returnTotal()

#        pull_histos = []

        ymax_scale = None
#        if self.histo['Signal']:

        
#        for shist in [self.histo['Signal_M800'], self.histo['Signal_M400']]:
#        for shist in [self.histo['Signal_M400']]:
#        for shist in [self.histo['Signal_M35'], self.histo['Signal_GF_M35'], self.histo['Signal_VBF_M40']]:
#        for shist in [self.histo['Signal_M400'], self.histo['Signal_M1000'], self.histo['Signal_M2000']]:
###        for shist in [self.histo['Signal_M1000']]:
###
###            if 0:
####            if shist:
###
###                ymax_num = self.total.weighted.GetBinContent(self.total.weighted.GetMaximumBin())
###                ymax_den = shist.weighted.GetBinContent(shist.weighted.GetMaximumBin())
####                ymax_den = self.histo['Signal_M60'].weighted.GetBinContent(self.histo['Signal_M60'].weighted.GetMaximumBin())
###
####                ymax_num = self.total.weighted.GetSumOfWeights()
####                ymax_den = shist.weighted.GetSumOfWeights()
###
###                ymax_scale = 1.
###
###                if ymax_den!=0:
###                    ymax_scale = ymax_num/ymax_den
###
###
###                print 'Scale = ', ymax_num, ', ', ymax_den, 'SF = ', ymax_scale
###                shist.weighted.Scale(ymax_scale)

            # set zero error 
#            for ibin in range(1, shist.weighted.GetXaxis().GetNbins()+1):
#                shist.weighted.SetBinError(ibin, 0)

#            import pdb; pdb.set_trace()
#            shist.legendLine += ' (x' + '{0:.0f}'.format(str(ymax_scale)) + ')'
#            shist.legendLine += '(x' + '{0:.0f}'.format(ymax_scale) + ')'

        self.histo.DrawStack('HIST', None, None, None, None, 1.5)

#        self.histo.DrawStack('HIST', None, None, None, None, 2)


        if self.draw_ratio:
            self.canvas.cd(2)

            hatchname = 'ratio_' + self.data.obj.GetName() + '_' + self.total.weighted.GetName()

            hist_hatch = copy.deepcopy(self.total.weighted)
            hist_hatch.SetName(hatchname)
            hist_hatch.SetTitle(hatchname)

            
#            hist_hatch = ROOT.TH1F(hatchname, hatchname,
#                                   self.total.weighted.GetXaxis().GetNbins(), 
#                                   self.total.weighted.GetXaxis().GetXmin(), 
#                                   self.total.weighted.GetXaxis().GetXmax())

            for ibin in range(1, hist_hatch.GetXaxis().GetNbins()+1):
                hist_hatch.SetBinContent(ibin, 1)

                if(self.total.weighted.GetBinContent(ibin)!=0):
                    hist_hatch.SetBinError(ibin, self.total.weighted.GetBinError(ibin)/self.total.weighted.GetBinContent(ibin))
                

#

            histPull = copy.deepcopy(self.data.obj)
            histPull.Divide(self.total.weighted)

#            for ibin in range(1, self.data.obj.GetXaxis().GetNbins()+1):
#                print ibin, 'data = ', self.data.obj.GetBinContent(ibin), 'MC = ', self.total.weighted.GetBinContent(ibin), 'pull = ', histPull.GetBinContent(ibin)


            # convert here to the usual TH1F, as some of the functions can be used only for TH1F
            
#            hist_pull = ROOT.TH1F('hist_pull', 'hist_pull',
#                                  self.total.weighted.GetXaxis().GetNbins(),
                                  
            for ibin in range(1, histPull.GetXaxis().GetNbins()+1):

                err = 0.

                if self.total.weighted.GetBinContent(ibin)!=0:
                    err = self.data.obj.GetBinError(ibin)/self.total.weighted.GetBinContent(ibin)

                histPull.SetBinError(ibin, err)
#                print ibin, 'data = ', self.data.obj.GetBinContent(ibin), '+/-', self.data.obj.GetBinError(ibin), 'MC = ', self.total.weighted.GetBinContent(ibin) , err
                                  
            

            histPull.UseCurrentStyle()

            histPull.SetLineColor(self.data.obj.GetLineColor())
            histPull.SetMarkerColor(self.data.obj.GetLineColor())
            histPull.SetMarkerSize(self.data.obj.GetMarkerSize())
            histPull.SetLineStyle(self.data.obj.GetLineStyle())
            histPull.SetLineWidth(self.data.obj.GetLineWidth())
            
            histPull.GetYaxis().SetRangeUser(-self.pullRange + 1., self.pullRange + 1.)

            # defaultYtoPixel = 408.  # height in pixels of default canvas
            defaultYtoPixel = self.canvas.GetPad(1).YtoPixel(0.)
            pad2YtoPixel = float(self.canvas.GetPad(2).YtoPixel(0))
            pad2XaxisFactor = defaultYtoPixel / pad2YtoPixel

#                print 'Pad size : ', self.total.GetXaxis().GetLabelSize(), pad2XaxisFactor
            histPull.GetXaxis().SetLabelSize(self.total.weighted.GetXaxis().GetLabelSize()*pad2XaxisFactor)
            histPull.GetXaxis().SetLabelOffset(self.total.weighted.GetXaxis().GetLabelOffset()*pad2XaxisFactor)
            histPull.GetXaxis().SetTitleSize(self.total.weighted.GetXaxis().GetTitleSize()*pad2XaxisFactor)
            histPull.GetXaxis().SetTitleOffset(self.total.weighted.GetXaxis().GetTitleOffset()/pad2XaxisFactor*2.5)

            histPull.GetYaxis().SetLabelSize(self.total.weighted.GetYaxis().GetLabelSize()*pad2XaxisFactor)
            histPull.GetYaxis().SetLabelOffset(self.total.weighted.GetYaxis().GetLabelOffset()*pad2XaxisFactor)
            histPull.GetYaxis().SetTitleSize(self.total.weighted.GetYaxis().GetTitleSize()*pad2XaxisFactor)
            histPull.GetYaxis().SetTitleOffset(0.8*self.total.weighted.GetYaxis().GetTitleOffset()/pad2XaxisFactor)

#                histos[0].GetYaxis().SetTitleOffset(1.15)
            
            histPull.GetYaxis().CenterTitle()
            histPull.GetXaxis().SetTickLength(histPull.GetXaxis().GetTickLength()*pad2XaxisFactor)
            histPull.GetYaxis().SetNdivisions(306)
                
#                print 'check : ', 0.8*self.total.weighted.GetYaxis().GetTitleOffset()/pad2XaxisFactor
            histPull.GetYaxis().SetTitleOffset(0.55)
            histPull.GetXaxis().SetTitle(self.total.weighted.GetXaxis().GetTitle())
            histPull.GetYaxis().SetTitle('Ratio')
            histPull.GetXaxis().SetTitleOffset(1.2)
            histPull.SetTitle('')

#            if ihist == 1:
#            histPull.Draw("ep")
#            hist_hatch.Draw("e2same")
#            histPull.Draw("epsame")

            
#            print 'color', self.new_idx

            hist_hatch.SetMarkerSize(0)
            hist_hatch.SetFillColor(self.new_idx)
            hist_hatch.SetFillStyle(3001)
            hist_hatch.SetLineWidth(1)

            histPull.GetXaxis().SetTitleSize(0.1)
            histPull.GetXaxis().SetLabelSize(0.1)
            histPull.Draw("ep")
            hist_hatch.Draw("e2same")
            histPull.Draw("epsame")
            
#            import pdb; pdb.set_trace()

#            else:
#                histPull.Draw("same ep")

            line = ROOT.TLine(histPull.GetXaxis().GetXmin(), 1, histPull.GetXaxis().GetXmax(), 1)
            line.SetLineStyle(2)
            line.Draw()


#            print '====================>', self.name
            if self.name.find('signal_os_inclusive_byIsolationMVA3oldDMwLTraw_morezoom_2')!=-1:

                ratiofile = ROOT.TFile(self.name.replace('.gif','').replace('.pdf','') + '_ORIGINAL.root', 'recreate')

                histPull.SetName('datamcratio')
                histPull.Write()
                ratiofile.Write()
                ratiofile.Close()


#                import pdb; pdb.set_trace()

                


            # This is a little bit ugly though ...

#            for i, h in enumerate(self.histos):
#                h.GetXaxis().SetLabelSize(0)

            self.canvas.cd(1)

        self.canvas.Update()

        l1=add_lumi(self.lumi)
        l1.Draw("same")
        l2=add_CMS()
        l2.Draw("same")
        l3=add_Preliminary()
        l3.Draw("same")

        arrowdir = []

        if len(self.arrows)!=0:
            self.canvas.cd(1)


            for ii, cut in enumerate(self.arrows):
                print ii, 'CUT = ', cut, self.total.weighted.GetMinimum(), self.total.weighted.GetMaximum()

                ar = ROOT.TArrow(cut, self.total.weighted.GetMinimum(), cut, self.total.weighted.GetMaximum()/2. , 0.02,"<|");
                
                ar.SetLineColor(ii+1)
                ar.SetFillColor(ii+1)
                ar.SetLineStyle(2)
                ar.SetLineWidth(2)
                arrowdir.append(copy.deepcopy(ar))

#        self.canvas.cd()

        for ad in arrowdir:
            ad.Draw()

        self.canvas.Print(self.name)
#        self.canvas.Print(self.name.replace('gif','pdf')) # save PDF
#        self.canvas.Print(self.name.replace('pdf','gif'))
#        self.canvas.Print(self.name.replace('pdf','eps'))

        self.canvas.cd(1).SetLogy()

#        self.canvas.Print(self.name.replace('.gif','_log.pdf'))
        self.canvas.Print(self.name.replace('.gif','_log.gif'))
        
