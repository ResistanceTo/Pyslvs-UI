# -*- coding: utf-8 -*-
##Pyslvs - Open Source Planar Linkage Mechanism Simulation and Dimensional Synthesis System.
##Copyright (C) 2016-2017 Yuan Chang [pyslvs@gmail.com]

"""
"graphics" module contains custom display widgets.
"""

from .color import (
    colorNum,
    colorName,
    colorIcons,
    colorQt
)
from .planarSolving import (
    slvsProcess,
    SlvsException
)
from .chart import dataChart
from .canvas import (
    BaseCanvas,
    distance_sorted,
    DynamicCanvas
)
from .nx_pydot import (
    graph,
    engine_picker,
    EngineList,
    EngineError
)

__all__ = [
    'colorNum',
    'colorName',
    'colorIcons',
    'colorQt',
    'slvsProcess',
    'SlvsException',
    'dataChart',
    'BaseCanvas',
    'distance_sorted',
    'DynamicCanvas',
    'graph',
    'engine_picker',
    'EngineList',
    'EngineError'
]
