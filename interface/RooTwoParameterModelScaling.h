// -*- mode: c++ -*-

#ifndef ROOTWOPARAMETERMODELPROCESSSCALING
#define ROOTWOPARAMTERMODELPROCESSSCALING

#include "RooRealProxy.h"
#include "RooAbsPdf.h"
#include "TProfile2D.h"
#include "TH2D.h"
#include "TString.h"
  
class RooTwoParameterModelScaling : public RooAbsReal {
public:

  RooTwoParameterModelScaling ();

  RooTwoParameterModelScaling (const char * name, const char * title, RooAbsReal& _param1,
			 RooAbsReal& _param2,
			       const char * th2d_filename, const char * th2d_name);
  RooTwoParameterModelScaling (const RooTwoParameterModelScaling& other, const char * name);
  virtual TObject * clone(const char * newname) const { 
    return new RooTwoParameterModelScaling(*this, newname);
  }
  
  virtual ~RooTwoParameterModelScaling ();  

  void initialize_histograms();
  void read_histograms() const;
  
protected:
  
  //  RooRealProxy x;
  //  const RooAbsReal& x;
  RooRealProxy param1;
  RooRealProxy param2;
  
  // double SM_integral;
  // std::vector<double> integral_basis;
  //here:
  //std::vector<double> bins;

  TString th2d_filename; 
  TString th2d_name;

  TH2D ** P; //!

  virtual double evaluate() const ;
  
private:
  
  ClassDef(RooTwoParameterModelScaling, 6) 
};

#endif
