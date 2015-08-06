combineCards.py /afs/cern.ch/work/a/anlevin/tmp/datacard_bin1.txt /afs/cern.ch/work/a/anlevin/tmp/datacard_bin2.txt /afs/cern.ch/work/a/anlevin/tmp/datacard_bin3.txt /afs/cern.ch/work/a/anlevin/tmp/datacard_bin4.txt >& datacard.txt
text2workspace.py -m 126 datacard.txt -o gm.root -P HiggsAnalysis.CombinedLimit.GeorgiMachacekPhysicsModel:my_gm_model --PO range_param=[0,0.5]
combine gm.root -M MultiDimFit -P param --floatOtherPOIs=0 --algo=grid --points=5000 --minimizerStrategy=2 -t -1 --expectSignal=0
