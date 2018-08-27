#include "TMath.h"
#include "TFile.h"
#include "TH1.h"
#include "TH2.h"
#include <iostream>
#include "TROOT.h"

//#include "RooWorkspace.h"
//#include "RooRealVar.h"
#include "TFile.h"
//#include "TLorentzVector.h"


//RooWorkspace *w;
//TLorentzVector vec;
//TLorentzVector vec_check;

TH1F *h_pu_data;
TH1F *h_pu_mc;
TH2F *h_muon;

void ReadFile(){

  // Pileup profile 
  
  TFile *data = new TFile("pileup/Data_PileUp_2017_69p2.root");
  TFile *mc = new TFile("pileup/MC_PileUp_Winter17_PU25ns_V2_fromMC.root");
  
  h_pu_data = (TH1F*) data->Get("pileup");
  h_pu_mc = (TH1F*) mc->Get("pileup");
  
  h_pu_data->Scale(1./h_pu_data->Integral());
  h_pu_mc->Scale(1./h_pu_mc->Integral());

  //  std::cout << h_pu_data->GetSumOfWeights() << " " << h_pu_data->GetNbinsX() << std::endl;
  //  std::cout << h_pu_mc->GetSumOfWeights() << " " << h_pu_mc->GetNbinsX() << std::endl;

  if(h_pu_data->GetNbinsX() != h_pu_mc->GetNbinsX()){
    std::cout << "Pileup histogram has different binning !" << std::endl;
  }

  
  //  TFile *muon = new TFile("leptonSF/EfficienciesAndSF_RunBtoF_Nov17Nov2017.root");
  //  h_muon = (TH2F*) muon->Get("IsoMu27_PtEtaBins/pt_abseta_ratio");


  // Muon ID/Iso/Trigger SF

  

  //  TFile *f = new TFile("CorrectionsWorkspace/htt_scalefactors_v16_5.root");
  //  w = (RooWorkspace*)f->Get("w");
  //  f->Close();

}



float getPUweight(const int npu){
  
  float data = h_pu_data->GetBinContent(h_pu_data->FindBin(npu));
  float mc = h_pu_mc->GetBinContent(h_pu_mc->FindBin(npu));

  //  std::cout << data << " " << mc << " " << npu << " -> " << data/mc << std::endl;

  if(mc > 0.){
    return data/mc;
    //    std::cout << "pu weight =" << data/mc << std::endl;
  }//else{
    //std::cout << "No predefined pileup weights" << std::endl;
  //  }
  return 1;

}

//float getMuWeight(const float pt, const float eta){
//  
//  float abseta = TMath::Abs(eta);
//
//  Int_t xbin = h_muon->GetXaxis()->FindBin(pt);
//  Int_t ybin = h_muon->GetYaxis()->FindBin(abseta);
//  
//  Float_t sf = h_muon->GetBinContent(xbin, ybin);
//  
//  //  std::cout << "pt = " << pt <<  " -> " << xbin << ",  eta = " << eta << " -> "  << ybin << " => SF = " << sf << std::endl;
//  return sf;
//
//}


//float getMuTrigWeight(Double_t pt, Double_t eta){
//  
//
//  w->var("m_pt")->setVal(pt);
//  w->var("m_eta")->setVal(eta);
//  //  double muon_id_scalefactor = w->function("m_id_ratio")->getVal();
//  //  double muon_trg_sf = w->function("m_iso_ratio")->getVal();
//  double muon_trg_sf = w->function("m_trg24OR_ratio")->getVal();
//
//  //  std::cout << pt << " " << eta << " " << muon_trg_sf<< std::endl;
//  
//  return muon_trg_sf;
//
//}


//Float_t deltaPhi(Float_t p1, Float_t p2){
//
//  Float_t res = p1 - p2;
//  while(res > TMath::Pi()){
//    res -= 2*TMath::Pi();
//  }
//  while(res < -TMath::Pi()){
//    res += 2*TMath::Pi();
//  }
//  
//  return res;
//}


//Float_t tauID_up(Float_t pt){
//
//  Float_t sf = 1. + 0.05*pt/1000;
//
//  return sf;
//}
//
//Float_t tauID_down(Float_t pt){
//
//  Float_t sf = 1. - 0.35*pt/1000;
//
//  return sf;
//}
//
//
//
//Float_t muID_up(Float_t pt){
//
////  if(abs(eta) < 1.2) return 1;
////
////
////  vec.SetPtEtaPhiM(pt, eta, phi, m);
////  Float_t p = vec.P();
////
////  Float_t sf = (0.9893 - p * 3.666*0.00001) / (0.9974 - p * 1.721 * 0.00001);
//
//
//  Float_t sf = 1;
//  if(pt < 300 ){
//    sf = 1.05;
//  }else{
//    sf = 1.1;
//  }
//
//
//  //  std::cout << pt << " " << eta << " " << phi << " " << m  << "-> p = " << p  << "-> SF = " << sf << std::endl;
//
//  return sf;
//}
//
//
//Float_t muID_down(Float_t pt){
//
////  if(abs(eta) < 1.2) return 1;
////
////
////  vec.SetPtEtaPhiM(pt, eta, phi, m);
////  Float_t p = vec.P();
////
////  Float_t sf = (0.9893 - p * 3.666*0.00001) / (0.9974 - p * 1.721 * 0.00001);
//
//
//  Float_t sf = 1;
//  if(pt < 300 ){
//    sf = 0.95;
//  }else{
//    sf = 0.9;
//  }
//
//
//  //  std::cout << pt << " " << eta << " " << phi << " " << m  << "-> p = " << p  << "-> SF = " << sf << std::endl;
//
//  return sf;
//}
//
//
//
////Float_t muP(Float_t pt, Float_t eta, Float_t phi, Float_t m){
////
////  vec_check.SetPtEtaPhiM(pt, eta, phi, m);
////  Float_t p = vec_check.P();
////
////  return p;
////}
//
//
//Float_t jtauID_up(Float_t pt){
//
//  Float_t sf = 1.;
//
//  return sf;
//}
//Float_t jtauID_down(Float_t pt){
//
//  Float_t sf = 1.; 
////  if(pt < 120){
////    sf = 1.2 - 0.004*pt;
////  }else{
////    sf = 0.72;
////  }
//
//
//  sf = 1.2 - 0.004*pt;
//
//  return sf;
//}




void functionmacro(){
  ReadFile();
}
