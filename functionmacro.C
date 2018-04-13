/*
  functionmacro.C : provide QCD weights at drawing level
  modified from : https://github.com/CMS-HTT/QCDModelingEMu

  4 April 2017 Y.T
 */


#include "TMath.h"
#include "TFile.h"
#include "TH1.h"
#include <iostream>
#include "TROOT.h"

#include "RooWorkspace.h"
#include "RooRealVar.h"
#include "TFile.h"
#include "TLorentzVector.h"


RooWorkspace *w;
TLorentzVector vec;
TLorentzVector vec_check;

void ReadFile(){

  //  TFile *f = new TFile("CorrectionsWorkspace/htt_scalefactors_v16_5.root");
  //  w = (RooWorkspace*)f->Get("w");
  //  f->Close();



}


float getMuTrigWeight(Double_t pt, Double_t eta){
  

  w->var("m_pt")->setVal(pt);
  w->var("m_eta")->setVal(eta);
  //  double muon_id_scalefactor = w->function("m_id_ratio")->getVal();
  //  double muon_trg_sf = w->function("m_iso_ratio")->getVal();
  double muon_trg_sf = w->function("m_trg24OR_ratio")->getVal();

  //  std::cout << pt << " " << eta << " " << muon_trg_sf<< std::endl;
  
  return muon_trg_sf;

}


Float_t deltaPhi(Float_t p1, Float_t p2){

  Float_t res = p1 - p2;
  while(res > TMath::Pi()){
    res -= 2*TMath::Pi();
  }
  while(res < -TMath::Pi()){
    res += 2*TMath::Pi();
  }
  
  return res;
}


Float_t tauID_up(Float_t pt){

  Float_t sf = 1. + 0.05*pt/1000;

  return sf;
}

Float_t tauID_down(Float_t pt){

  Float_t sf = 1. - 0.35*pt/1000;

  return sf;
}



Float_t muID_up(Float_t pt){

//  if(abs(eta) < 1.2) return 1;
//
//
//  vec.SetPtEtaPhiM(pt, eta, phi, m);
//  Float_t p = vec.P();
//
//  Float_t sf = (0.9893 - p * 3.666*0.00001) / (0.9974 - p * 1.721 * 0.00001);


  Float_t sf = 1;
  if(pt < 300 ){
    sf = 1.05;
  }else{
    sf = 1.1;
  }


  //  std::cout << pt << " " << eta << " " << phi << " " << m  << "-> p = " << p  << "-> SF = " << sf << std::endl;

  return sf;
}


Float_t muID_down(Float_t pt){

//  if(abs(eta) < 1.2) return 1;
//
//
//  vec.SetPtEtaPhiM(pt, eta, phi, m);
//  Float_t p = vec.P();
//
//  Float_t sf = (0.9893 - p * 3.666*0.00001) / (0.9974 - p * 1.721 * 0.00001);


  Float_t sf = 1;
  if(pt < 300 ){
    sf = 0.95;
  }else{
    sf = 0.9;
  }


  //  std::cout << pt << " " << eta << " " << phi << " " << m  << "-> p = " << p  << "-> SF = " << sf << std::endl;

  return sf;
}



Float_t muP(Float_t pt, Float_t eta, Float_t phi, Float_t m){

  vec_check.SetPtEtaPhiM(pt, eta, phi, m);
  Float_t p = vec_check.P();

  return p;
}


Float_t jtauID_up(Float_t pt){

  Float_t sf = 1.;

  return sf;
}
Float_t jtauID_down(Float_t pt){

  Float_t sf = 1.; 
//  if(pt < 120){
//    sf = 1.2 - 0.004*pt;
//  }else{
//    sf = 0.72;
//  }


  sf = 1.2 - 0.004*pt;

  return sf;
}




void functionmacro(){
  std::cout << std::endl;
  std::cout << "Initialize functionmacro.C ..." << std::endl;
  std::cout << std::endl;
  //  ReadFile();
}
