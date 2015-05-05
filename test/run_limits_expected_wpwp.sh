operators_and_ranges="\
FS0,-25,25
FS1,-50,50
FM0,-25,25
FM1,-25,25
FM6,-25,25
FM7,-50,50
FT0,-2.5,2.5
FT1,-1,1
FT2,-2.5,2.5
"






for operator_and_range in $operators_and_ranges
do

operator=`echo $operator_and_range | awk -F, '{print $1}'`
lower=`echo $operator_and_range | awk -F, '{print $2}'`
upper=`echo $operator_and_range | awk -F, '{print $3}'`

combineCards.py /afs/cern.ch/work/a/anlevin/tmp/wpwp_dim8_datacard_${operator}_bin1.txt /afs/cern.ch/work/a/anlevin/tmp/wpwp_dim8_datacard_${operator}_bin2.txt /afs/cern.ch/work/a/anlevin/tmp/wpwp_dim8_datacard_${operator}_bin3.txt /afs/cern.ch/work/a/anlevin/tmp/wpwp_dim8_datacard_${operator}_bin4.txt >& os_ww_datacard_mll_${operator}.txt
python2.6 refine_grid_1d.py /afs/cern.ch/work/a/anlevin/tmp/wpwp_${operator}_scaling.root wpwp_${operator}_scaling_refined.root
text2workspace.py -m 126 os_ww_datacard_mll_${operator}.txt -o os_mll_${operator}.root -P HiggsAnalysis.CombinedLimit.OneParameterPhysicsModel:my_1d_model --PO range_param=[${lower},${upper}] --PO scaling_filename=/afs/cern.ch/work/a/anlevin/cmssw/CMSSW_7_1_5/src/HiggsAnalysis/CombinedLimit/test/wpwp_${operator}_scaling_refined.root
combine os_mll_${operator}.root -M MultiDimFit -P param --floatOtherPOIs=0 --algo=grid --points=5000 --minimizerStrategy=2 -t -1 --expectSignal=1
mv higgsCombineTest.MultiDimFit.mH120.root higgsCombineTest.MultiDimFit.mH120.expected.${operator}.root

done
