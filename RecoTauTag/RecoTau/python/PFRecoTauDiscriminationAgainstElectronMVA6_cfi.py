import FWCore.ParameterSet.Config as cms

from RecoTauTag.RecoTau.TauDiscriminatorTools import requireLeadTrack

pfRecoTauDiscriminationAgainstElectronMVA6 = cms.EDProducer("PFRecoTauDiscriminationAgainstElectronMVA6",

    # tau collection to discriminate
    PFTauProducer = cms.InputTag('pfTauProducer'),

    # Require leading pion ensures that:
    #  1) these is at least one track above threshold (0.5 GeV) in the signal cone
    #  2) a track OR a pi-zero in the signal cone has pT > 5 GeV
    Prediscriminants = requireLeadTrack,

    method = cms.string("BDTG"),
    loadMVAfromDB = cms.bool(True),
    returnMVA = cms.bool(True),
   
    mvaName_NoEleMatch_woGwoGSF_BL = cms.string("gbr_NoEleMatch_woGwoGSF_BL"),
    mvaName_NoEleMatch_wGwoGSF_BL = cms.string("gbr_NoEleMatch_wGwoGSF_BL"),
    mvaName_woGwGSF_BL = cms.string("gbr_woGwGSF_BL"),
    mvaName_wGwGSF_BL = cms.string("gbr_wGwGSF_BL"),
    mvaName_NoEleMatch_woGwoGSF_EC = cms.string("gbr_NoEleMatch_woGwoGSF_EC"),
    mvaName_NoEleMatch_wGwoGSF_EC = cms.string("gbr_NoEleMatch_wGwoGSF_EC"),
    mvaName_woGwGSF_EC = cms.string("gbr_woGwGSF_EC"),
    mvaName_wGwGSF_EC = cms.string("gbr_wGwGSF_EC"),

    minMVANoEleMatchWOgWOgsfBL = cms.double(0.0),
    minMVANoEleMatchWgWOgsfBL  = cms.double(0.0),
    minMVAWOgWgsfBL            = cms.double(0.0),
    minMVAWgWgsfBL             = cms.double(0.0),
    minMVANoEleMatchWOgWOgsfEC = cms.double(0.0),
    minMVANoEleMatchWgWOgsfEC  = cms.double(0.0),
    minMVAWOgWgsfEC            = cms.double(0.0),
    minMVAWgWgsfEC             = cms.double(0.0),

    srcGsfElectrons = cms.InputTag('gedGsfElectrons')
)
