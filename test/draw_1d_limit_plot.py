from ROOT import *
from array import array
import sys
import time
from ROOT import TGraph

#gStyle.SetFillStyle(0)
#gStyle.SetLegendBorderSize(0);
gROOT.ForceStyle()

deltaNLL_95=ROOT.Math.chisquared_quantile_c(1-0.95,1)

npts=1000

if (len(sys.argv) != 6 and len(sys.argv) != 8):
    print "format: python2.6 draw_1d_limt_plot.py output_file_name x_axis_label limit_label input_file_name label [input_file_name_2] [label_2]"
    print "exiting"
    sys.exit(0)

f=TFile(sys.argv[4],"r")
x_axis_label=sys.argv[2]
output_file_name=sys.argv[1]
limit=f.Get("limit")

limit_label=sys.argv[3]
label=sys.argv[5]

deltaNLL=array("f",[0])
param=array("f",[0])
iToy=array("i",[0])

limit.SetBranchAddress("deltaNLL", deltaNLL)
limit.SetBranchAddress("param",param)
limit.SetBranchAddress("iToy",iToy)

graph=TGraph()


min_parval=None
max_parval=None

first_time=True

for j in range(1,limit.GetEntries()-1):
    limit.GetEntry(j)

    #the first param value is at the location of the minimum, so it is not on the grid, this can cause the fit to mess up
    if first_time:
        first_time=False
        continue
    
    if min_parval==None:
        min_parval = param[0]
    if max_parval==None:
        max_parval = param[0]
        
    if param[0] < min_parval:
        min_parval = param[0]
    if param[0] > max_parval:
        max_parval = param[0]
    graph.SetPoint(j-1,param[0],2*deltaNLL[0])


if (len(sys.argv) == 8):
    f_2=TFile(sys.argv[6],"r")

    limit_2=f_2.Get("limit")

    deltaNLL_2=array("f",[0])
    param_2=array("f",[0])
    iToy_2=array("i",[0])

    label_2=sys.argv[7]
    
    limit_2.SetBranchAddress("deltaNLL", deltaNLL_2)
    limit_2.SetBranchAddress("param",param_2)
    limit_2.SetBranchAddress("iToy",iToy_2)


    min_parval_2=None
    max_parval_2=None

    first_time_2=True

    graph_2=TGraph()

    for j in range(1,limit_2.GetEntries()-1):
        limit_2.GetEntry(j)

        #the first param value is at the location of the minimum, so it is not on the grid, this can cause the fit to mess up
        if first_time_2:
            first_time_2=False
            continue
    
        if min_parval_2==None:
            min_parval_2 = param_2[0]
        if max_parval_2==None:
            max_parval_2 = param_2[0]
        
        if param_2[0] < min_parval_2:
            min_parval_2 = param_2[0]
        if param_2[0] > max_parval_2:
            max_parval_2 = param_2[0]
        graph_2.SetPoint(j-1,param_2[0],2*deltaNLL_2[0])


for i in range(0,npts):
    parval = min_parval + i*(max_parval-min_parval)/npts
    if deltaNLL_95 > graph.Eval(parval):
        param_95_neg=parval
        break

for i in range(0,npts):
    parval = min_parval + i*(max_parval-min_parval)/npts
    if deltaNLL_95 > graph.Eval(parval):
        param_95_pos=parval        

print "95% confidence limits:"
print "["+str(param_95_neg)+","+str(param_95_pos)+"]"

graph.GetXaxis().SetTitle(x_axis_label)
graph.GetYaxis().SetTitle("2#DeltaNLL")
graph.SetLineColor(kBlue)
graph.SetMarkerColor(kBlue)
graph.Draw("AP")

if (len(sys.argv) == 8):
    graph_2.SetLineColor(kGreen+2)
    graph_2.SetMarkerColor(kGreen+2)
    graph_2.Draw("P")

gPad.Update()

l95_neg = TLine(param_95_neg,gPad.GetUymin(),param_95_neg,deltaNLL_95);
l95_neg.SetLineColor(kBlack)
l95_neg.SetLineWidth(3)
l95_neg.Draw();

l95_pos = TLine(param_95_pos,gPad.GetUymin(),param_95_pos,deltaNLL_95);
l95_pos.SetLineColor(kBlack)
l95_pos.SetLineWidth(3)
l95_pos.Draw();

print gPad.GetX1()
print gPad.GetX2()

horline = TLine(gPad.GetUxmin(),deltaNLL_95,gPad.GetUxmax(),deltaNLL_95);
horline.SetLineColor(kBlack)
horline.SetLineStyle(7)
horline.SetLineWidth(3)
horline.Draw();

leg=TLegend(0.3,0.6,0.70,0.8)

leg.AddEntry(graph,label,"l")
if (len(sys.argv) == 8):
    leg.AddEntry(graph_2,label_2,"l")
leg.AddEntry(l95_neg,limit_label,"l")
leg.SetTextSize(0.03)
leg.SetFillColor(0)

leg.Draw()

c1.Update()

c1.SaveAs(output_file_name)

#raw_input()

