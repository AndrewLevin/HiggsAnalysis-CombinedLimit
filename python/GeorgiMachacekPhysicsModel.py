from HiggsAnalysis.CombinedLimit.AnomalousCouplingModel import *
import ROOT as r
import os

#this model is in the equal couplings scenario of HISZ or something similar
#it does the old style limits of setting the other parameter to zero
class GeorgiMachacekPhysicsModel(AnomalousCouplingModel):
    def __init__(self):
        AnomalousCouplingModel.__init__(self)
        self.channels = ['channel_name']
        self.processes = ['WWewk']
        self.pois = ['param']

    def buildScaling(self,process,channel):        
        scalerName = process
#        self.modelBuilder.factory_('RooOneParameterModelScaling::Scaling_WWewk_wwssll8TeV2(param,"'+self.scaling_filename+'","aQGC_scaling3")')
        
        #self.modelBuilder.factory_('RooOneParameterModelScaling::Scaling_WWewk_ch1(param,"'+self.scaling_filename+'","aQGC_scaling1")')
        #self.modelBuilder.factory_('RooOneParameterModelScaling::Scaling_WWewk_ch2(param,"'+self.scaling_filename+'","aQGC_scaling2")')
        #self.modelBuilder.factory_('RooOneParameterModelScaling::Scaling_WWewk_ch3(param,"'+self.scaling_filename+'","aQGC_scaling3")')
        #self.modelBuilder.factory_('RooOneParameterModelScaling::Scaling_WWewk_ch4(param,"'+self.scaling_filename+'","aQGC_scaling4")')

        self.modelBuilder.factory_('RooGeorgiMachacekModelScaling::Scaling_WWjj_ch1(param)')
        self.modelBuilder.factory_('RooGeorgiMachacekModelScaling::Scaling_WWjj_ch2(param)')
        self.modelBuilder.factory_('RooGeorgiMachacekModelScaling::Scaling_WWjj_ch3(param)')
        self.modelBuilder.factory_('RooGeorgiMachacekModelScaling::Scaling_WWjj_ch4(param)')

        return scalerName

my_gm_model = GeorgiMachacekPhysicsModel()
