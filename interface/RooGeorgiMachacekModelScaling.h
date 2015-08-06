// -*- mode: c++ -*-

#ifndef ROOGEORGIMACHACEKMODELPROCESSSCALING
#define ROOGEORGIMACHACEKMODELPROCESSSCALING

#include "RooRealProxy.h"
#include "RooAbsPdf.h"
#include "TProfile2D.h"
#include "TString.h"
  
class RooGeorgiMachacekModelScaling : public RooAbsReal {
public:

  RooGeorgiMachacekModelScaling ();

  RooGeorgiMachacekModelScaling (const char * name, const char * title, RooAbsReal& _param);
  RooGeorgiMachacekModelScaling (const RooGeorgiMachacekModelScaling& other, const char * name);
  virtual TObject * clone(const char * newname) const { 
    return new RooGeorgiMachacekModelScaling(*this, newname);
  }
  
  virtual ~RooGeorgiMachacekModelScaling ();  

protected:
  
  //  RooRealProxy x;
  //  const RooAbsReal& x;
  RooRealProxy param;
  
  // double SM_integral;
  // std::vector<double> integral_basis;
  //here:
  //std::vector<double> bins;

  virtual double evaluate() const ;
  
private:
  
  ClassDef(RooGeorgiMachacekModelScaling, 6) 
};

#endif
