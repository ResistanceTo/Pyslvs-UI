# -*- coding: utf-8 -*-
##Pyslvs - Open Source Planar Linkage Mechanism Simulation and Dimensional Synthesis System.
##Copyright (C) 2016-2017 Yuan Chang [pyslvs@gmail.com]

"""
"synthesis" module contains synthesis functional interfaces.
"""

#['SynthesisCollections']
from .Collections import *
#['NumberAndTypeSynthesis']
from .NumberAndTypeSynthesis import *
#['DimensionalSynthesis']
from .DimensionalSynthesis import *

__all__ = ['NumberAndTypeSynthesis', 'SynthesisCollections', 'DimensionalSynthesis']
