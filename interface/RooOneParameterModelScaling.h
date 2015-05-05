// -*- mode: c++ -*-

#ifndef ROOONEPARAMETERMODELPROCESSSCALING
#define ROOONEPARAMETERMODELPROCESSSCALING

#include "RooRealProxy.h"
#include "RooAbsPdf.h"
#include "TProfile2D.h"
#include "TH2D.h"
#include "TString.h"
  
class RooOneParameterModelScaling : public RooAbsReal {
public:

  RooOneParameterModelScaling ();

  RooOneParameterModelScaling (const char * name, const char * title, RooAbsReal& _param,
			       const char * th2d_filename, const char * th2d_name);
  RooOneParameterModelScaling (const RooOneParameterModelScaling& other, const char * name);
  virtual TObject * clone(const char * newname) const { 
    return new RooOneParameterModelScaling(*this, newname);
  }
  
  virtual ~RooOneParameterModelScaling ();  

  void initialize_histograms();
  void read_histograms() const;
  
protected:
  
  //  RooRealProxy x;
  //  const RooAbsReal& x;
  RooRealProxy param;
  
  // double SM_integral;
  // std::vector<double> integral_basis;
  //here:
  //std::vector<double> bins;

  TString th2d_filename; 
  TString th2d_name;

  TH1D ** P; //!

  virtual double evaluate() const ;
  
private:
  
  ClassDef(RooOneParameterModelScaling, 6) 
};

#endif
