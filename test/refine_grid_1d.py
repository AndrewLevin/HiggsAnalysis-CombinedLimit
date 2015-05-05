#! /usr/bin/env python

import sys
import os

import ROOT
from ROOT import *

nGridPointsForNewF=200

if (len(sys.argv) != 3 and len(sys.argv) !=6):
    print "format: python2.6.py refine_grid_1d.py input_file_name output_file_name [validation_plots_dir] [validation_plots_label] [x_axis_label]"
    print "exiting"
    sys.exit(0)

if len(sys.argv) == 6:
    validation_plots_dir=sys.argv[3]
    validation_plots_label=sys.argv[4]
    x_axis_label=sys.argv[5]

sigFile=sys.argv[1]
output_file_name=sys.argv[2]

print "input file: "+ sigFile
print "output file: "+ output_file_name

#doing this somehow avoids errors from TStreamerInfo
#TFile.Open("/data/smurf/data/Run2012_Summer12_SmurfV9_53X/mitf-alljets/wwss_qed_4_qcd_99_ls_lm_lt.root")

outfile_newF = TFile.Open(output_file_name,'RECREATE')

sigFile = TFile.Open(sigFile)

for key in sigFile.GetListOfKeys():
    anom_th1d=key.ReadObj()
    if type(anom_th1d)!=TH1D:
        print "expecting a TH1D, exiting"
        sys.exit(0)

    par1GridMin=anom_th1d.GetXaxis().GetBinLowEdge(1)
    par1GridMax=anom_th1d.GetXaxis().GetBinUpEdge(anom_th1d.GetNbinsX())
    print "par1GridMin:"+str(par1GridMin)
    print "par1GridMax:"+str(par1GridMax)
    
    func = TF1('fittingFunction','[0] + [1]*x + [2]*x*x',
               par1GridMin,par1GridMax)

    anom_th1d.Fit(func,'R0','')

    outfile_newF.cd()
    newFormatInput = TH1D(anom_th1d.GetName()
                      ,anom_th1d.GetTitle(),
                      nGridPointsForNewF,par1GridMin,par1GridMax)

    for bin_x in range(1,nGridPointsForNewF+1):
            par1_value=newFormatInput.GetXaxis().GetBinCenter(bin_x)
            yield_bin=func.GetParameter(0)+func.GetParameter(1)*par1_value+func.GetParameter(2)*par1_value*par1_value
            newFormatInput.SetBinContent(bin_x,yield_bin)        

    newFormatInput.Write()

    if len(sys.argv) == 6:

        #assumes that the last character of the histogram is the bin number

        anom_th1d.SetTitle("yield/SM yield in bin "+anom_th1d.GetName()[len(anom_th1d.GetName())-1])
        anom_th1d.GetXaxis().SetTitle(x_axis_label)
        #anom_th1d.SetTitle("")
        anom_th1d.SetStats(0)
        anom_th1d.Draw()
        gPad.Update()
        newFormatInput.SetTitle("yield/SM yield in bin "+anom_th1d.GetName()[len(anom_th1d.GetName())-1])
        newFormatInput.GetXaxis().SetTitle(x_axis_label)
        #newFormatInput.SetTitle("")
        newFormatInput.SetStats(0)
        #newFormatInput.Draw("SAME")
        gPad.Update()

        c1.SaveAs(validation_plots_dir+validation_plots_label+"_bin"+anom_th1d.GetName()[len(anom_th1d.GetName())-1]+".png")
