# Reads in multiprocess mode a file with empty runs and lumis
# interspersed with runs and lumis with events

import FWCore.ParameterSet.Config as cms

process = cms.Process("TEST")

process.load("FWCore.Framework.test.cmsExceptionsFatal_cff")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.options = cms.untracked.PSet(multiProcesses=cms.untracked.PSet(
    maxChildProcesses=cms.untracked.int32(2),
    maxSequentialEventsPerChild=cms.untracked.uint32(1)))

process.source = cms.Source("PoolSource", fileNames = cms.untracked.vstring("file:multiprocess_test2.root"))

process.test = cms.EDAnalyzer('MulticoreRunLumiEventChecker',
    multiProcessSequentialEvents = process.options.multiProcesses.maxSequentialEventsPerChild,
    eventSequence = cms.untracked.VEventID(
        cms.EventID(100, 0, 0),
        cms.EventID(100, 1, 0),
        cms.EventID(100, 1, 0),
        cms.EventID(100, 2, 0),
        cms.EventID(100, 2, 0),
        cms.EventID(100, 3, 0),
        cms.EventID(100, 3, 0),
        cms.EventID(100, 0, 0),
        cms.EventID(101, 0, 0),
        cms.EventID(101, 1, 0),
        cms.EventID(101, 1, 0),
        cms.EventID(101, 2, 0),
        cms.EventID(101, 2, 0),
        cms.EventID(101, 3, 0),
        cms.EventID(101, 3, 0),
        cms.EventID(101, 0, 0),
        cms.EventID(102, 0, 0),
        cms.EventID(102, 1, 0),
        cms.EventID(102, 1, 1),
        cms.EventID(102, 1, 2),
        cms.EventID(102, 1, 0),
        cms.EventID(102, 2, 0),
        cms.EventID(102, 2, 3),
        cms.EventID(102, 2, 4),
        cms.EventID(102, 2, 0),
        cms.EventID(102, 3, 0),
        cms.EventID(102, 3, 5),
        cms.EventID(102, 3, 0),
        cms.EventID(102, 0, 0),
        cms.EventID(103, 0, 0),
        cms.EventID(103, 1, 0),
        cms.EventID(103, 1, 0),
        cms.EventID(103, 2, 0),
        cms.EventID(103, 2, 0),
        cms.EventID(103, 3, 0),
        cms.EventID(103, 3, 0),
        cms.EventID(103, 0, 0),
        cms.EventID(104, 0, 0),
        cms.EventID(104, 1, 0),
        cms.EventID(104, 1, 1),
        cms.EventID(104, 1, 2),
        cms.EventID(104, 1, 0),
        cms.EventID(104, 2, 0),
        cms.EventID(104, 2, 3),
        cms.EventID(104, 2, 4),
        cms.EventID(104, 2, 0),
        cms.EventID(104, 3, 0),
        cms.EventID(104, 3, 5),
        cms.EventID(104, 3, 0),
        cms.EventID(104, 0, 0),
        cms.EventID(105, 0, 0),
        cms.EventID(105, 1, 0),
        cms.EventID(105, 1, 1),
        cms.EventID(105, 1, 0),
        cms.EventID(105, 2, 0),
        cms.EventID(105, 2, 0),
        cms.EventID(105, 3, 0),
        cms.EventID(105, 3, 5),
        cms.EventID(105, 3, 0),
        cms.EventID(105, 0, 0),
        cms.EventID(106, 0, 0),
        cms.EventID(106, 1, 0),
        cms.EventID(106, 1, 0),
        cms.EventID(106, 2, 0),
        cms.EventID(106, 2, 3),
        cms.EventID(106, 2, 0),
        cms.EventID(106, 3, 0),
        cms.EventID(106, 3, 0),
        cms.EventID(106, 0, 0),
        cms.EventID(107, 0, 0),
        cms.EventID(107, 1, 0),
        cms.EventID(107, 1, 1),
        cms.EventID(107, 1, 2),
        cms.EventID(107, 1, 0),
        cms.EventID(107, 2, 0),
        cms.EventID(107, 2, 3),
        cms.EventID(107, 2, 4),
        cms.EventID(107, 2, 0),
        cms.EventID(107, 3, 0),
        cms.EventID(107, 3, 5),
        cms.EventID(107, 3, 0),
        cms.EventID(107, 0, 0),
        cms.EventID(108, 0, 0),
        cms.EventID(108, 1, 0),
        cms.EventID(108, 1, 0),
        cms.EventID(108, 2, 0),
        cms.EventID(108, 2, 0),
        cms.EventID(108, 3, 0),
        cms.EventID(108, 3, 0),
        cms.EventID(108, 0, 0),
        cms.EventID(109, 0, 0),
        cms.EventID(109, 1, 0),
        cms.EventID(109, 1, 0),
        cms.EventID(109, 2, 0),
        cms.EventID(109, 2, 0),
        cms.EventID(109, 3, 0),
        cms.EventID(109, 3, 0),
        cms.EventID(109, 0, 0),
        cms.EventID(110, 0, 0),
        cms.EventID(110, 1, 0),
        cms.EventID(110, 1, 1),
        cms.EventID(110, 1, 2),
        cms.EventID(110, 1, 0),
        cms.EventID(110, 2, 0),
        cms.EventID(110, 2, 3),
        cms.EventID(110, 2, 0),
        cms.EventID(110, 3, 0),
        cms.EventID(110, 3, 0),
        cms.EventID(110, 0, 0),
        cms.EventID(111, 0, 0),
        cms.EventID(111, 1, 0),
        cms.EventID(111, 1, 0),
        cms.EventID(111, 2, 0),
        cms.EventID(111, 2, 0),
        cms.EventID(111, 3, 0),
        cms.EventID(111, 3, 0),
        cms.EventID(111, 0, 0),
        cms.EventID(112, 0, 0),
        cms.EventID(112, 1, 0),
        cms.EventID(112, 1, 0),
        cms.EventID(112, 2, 0),
        cms.EventID(112, 2, 3),
        cms.EventID(112, 2, 4),
        cms.EventID(112, 2, 0),
        cms.EventID(112, 3, 0),
        cms.EventID(112, 3, 5),
        cms.EventID(112, 3, 0),
        cms.EventID(112, 0, 0),
        cms.EventID(113, 0, 0),
        cms.EventID(113, 1, 0),
        cms.EventID(113, 1, 0),
        cms.EventID(113, 2, 0),
        cms.EventID(113, 2, 0),
        cms.EventID(113, 3, 0),
        cms.EventID(113, 3, 0),
        cms.EventID(113, 0, 0),
        cms.EventID(114, 0, 0),
        cms.EventID(114, 1, 0),
        cms.EventID(114, 1, 0),
        cms.EventID(114, 2, 0),
        cms.EventID(114, 2, 0),
        cms.EventID(114, 3, 0),
        cms.EventID(114, 3, 0),
        cms.EventID(114, 0, 0),
        cms.EventID(115, 0, 0),
        cms.EventID(115, 1, 0),
        cms.EventID(115, 1, 0),
        cms.EventID(115, 2, 0),
        cms.EventID(115, 2, 0),
        cms.EventID(115, 3, 0),
        cms.EventID(115, 3, 0),
        cms.EventID(115, 0, 0),
        cms.EventID(116, 0, 0),
        cms.EventID(116, 1, 0),
        cms.EventID(116, 1, 0),
        cms.EventID(116, 2, 0),
        cms.EventID(116, 2, 0),
        cms.EventID(116, 3, 0),
        cms.EventID(116, 3, 0),
        cms.EventID(116, 0, 0),
        cms.EventID(117, 0, 0),
        cms.EventID(117, 1, 0),
        cms.EventID(117, 1, 0),
        cms.EventID(117, 2, 0),
        cms.EventID(117, 2, 0),
        cms.EventID(117, 3, 0),
        cms.EventID(117, 3, 0),
        cms.EventID(117, 0, 0),
        cms.EventID(118, 0, 0),
        cms.EventID(118, 1, 0),
        cms.EventID(118, 1, 0),
        cms.EventID(118, 2, 0),
        cms.EventID(118, 2, 0),
        cms.EventID(118, 3, 0),
        cms.EventID(118, 3, 0),
        cms.EventID(118, 0, 0),
        cms.EventID(119, 0, 0),
        cms.EventID(119, 1, 0),
        cms.EventID(119, 1, 0),
        cms.EventID(119, 2, 0),
        cms.EventID(119, 2, 0),
        cms.EventID(119, 3, 0),
        cms.EventID(119, 3, 0),
        cms.EventID(119, 0, 0)
    )
)

process.path1 = cms.Path(process.test)
