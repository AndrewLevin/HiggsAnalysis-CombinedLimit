from HiggsAnalysis.CombinedLimit.AnomalousCouplingModel import *
import ROOT as r
import os

#this model is in the equal couplings scenario of HISZ or something similar
#it does the old style limits of setting the other parameter to zero
class OneParameterPhysicsModel(AnomalousCouplingModel):
    def __init__(self):
        AnomalousCouplingModel.__init__(self)
        self.channels = ['channel_name']
        self.processes = ['wg']
        self.pois = ['param']

    def buildScaling(self,process,channel):        
        scalerName = process

        self.modelBuilder.factory_('RooOneParameterModelScaling::Scaling_Wg_ch1(param,"'+self.scaling_filename+'","ewdim6_scaling_bin_1")')
        self.modelBuilder.factory_('RooOneParameterModelScaling::Scaling_Wg_ch2(param,"'+self.scaling_filename+'","ewdim6_scaling_bin_2")')
        self.modelBuilder.factory_('RooOneParameterModelScaling::Scaling_Wg_ch3(param,"'+self.scaling_filename+'","ewdim6_scaling_bin_3")')
        self.modelBuilder.factory_('RooOneParameterModelScaling::Scaling_Wg_ch4(param,"'+self.scaling_filename+'","ewdim6_scaling_bin_4")')
        self.modelBuilder.factory_('RooOneParameterModelScaling::Scaling_Wg_ch5(param,"'+self.scaling_filename+'","ewdim6_scaling_bin_5")')


        return scalerName
        

my_1d_model = OneParameterPhysicsModel()

