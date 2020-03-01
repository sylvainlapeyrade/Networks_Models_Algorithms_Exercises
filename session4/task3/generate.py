#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
TSKS11 Hands-on session 4
Degree correlations

Erik G. Larsson, 2018
"""

import snap
import sys
sys.path.append("..")
sys.path.append("/courses/TSKS11/ht2019/data_and_fcns/")
from degreecorr import plot_knn

G = snap.GenRndPowerLaw(100000,2.5)
snap.SaveEdgeList(G,"n1.edgelist.txt")

G = snap.GenRndPowerLaw(100000,2.5)
snap.SaveEdgeList(G,"n2.edgelist.txt")

G = snap.GenRndPowerLaw(100000,2.5)
snap.SaveEdgeList(G,"n3.edgelist.txt")

G = snap.GenRndPowerLaw(100000,2.5)
snap.SaveEdgeList(G,"n4.edgelist.txt")

G = snap.GenRndPowerLaw(100000,2.5)
snap.SaveEdgeList(G,"n5.edgelist.txt")

