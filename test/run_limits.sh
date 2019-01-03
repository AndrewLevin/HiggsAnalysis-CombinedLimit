#operators_and_ranges="\
#cwww,-30,30
#cw,-240,240
#cb,-240,240
#cpwww,-12,12
#cpw,-120,120
#"

operators_and_ranges="\
cwww,-5,5
cw,-75,75
cb,-75,75
cpwww,-2.5,2.5
cpw,-50,50
"

for operator_and_range in $operators_and_ranges
do

operator=`echo $operator_and_range | awk -F, '{print $1}'`
lower=`echo $operator_and_range | awk -F, '{print $2}'`
upper=`echo $operator_and_range | awk -F, '{print $3}'`

combineCards.py /afs/cern.ch/user/a/amlevin/wg/2016/photon_pt_bin1.txt /afs/cern.ch/user/a/amlevin/wg/2016/photon_pt_bin2.txt /afs/cern.ch/user/a/amlevin/wg/2016/photon_pt_bin3.txt /afs/cern.ch/user/a/amlevin/wg/2016/photon_pt_bin4.txt /afs/cern.ch/user/a/amlevin/wg/2016/photon_pt_bin5.txt >& wg_datacard_${operator}.txt
python2.6 refine_grid_1d.py /afs/cern.ch/user/a/amlevin/wg/2016/${operator}_scaling.root wg_${operator}_scaling_refined.root
text2workspace.py -m 126 wg_datacard_${operator}.txt -o wg_${operator}.root -P HiggsAnalysis.CombinedLimit.OneParameterPhysicsModel:my_1d_model --PO range_param=[${lower},${upper}] --PO scaling_filename=/afs/cern.ch/user/a/amlevin/combine/CMSSW_8_1_0/src/HiggsAnalysis/CombinedLimit/test/wg_${operator}_scaling_refined.root
combine wg_${operator}.root -M MultiDimFit -P param --floatOtherPOIs=0 --algo=grid --points=5000 -t -1 --expectSignal=1
mv higgsCombineTest.MultiDimFit.mH120.root higgsCombineTest.MultiDimFit.mH120.expected.${operator}.root
combine wg_${operator}.root -M MultiDimFit -P param --floatOtherPOIs=0 --algo=grid --points=5000
mv higgsCombineTest.MultiDimFit.mH120.root higgsCombineTest.MultiDimFit.mH120.observed.${operator}.root


done
