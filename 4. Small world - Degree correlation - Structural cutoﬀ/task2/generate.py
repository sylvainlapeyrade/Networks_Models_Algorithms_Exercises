#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
TSKS11 Hands-on session 4
Degree correlations

Erik G. Larsson, 2018-2019
"""

import sys
sys.path.append("/courses/tsks11/ht2019/snap-4.1.0-4.1-centos6.5-x64-py2.6/")
import snap
# sys.path.append("..")
sys.path.append("/courses/tsks11/ht2019/data_and_fcns/")
# import degreecorr
from degreecorr import calc_corr
from degreecorr import plot_knn
from degreecorr import plot_degreepairs

# Science collaboration network

#G = snap.LoadEdgeList(snap.PUNGraph, "collaboration.edgelist.txt", 0, 1)
G = snap.LoadEdgeList(snap.PUNGraph, "/courses/TSKS11/ht2019/data_and_fcns/session4/task2/collaboration.edgelist.txt", 0, 1)

# re-wire, but keep the degree sequence
Gr = snap.GenRewire(G, 100)
snap.SaveEdgeList(Gr,"collaboration-R.edgelist.txt")

# Poisson random network

G = snap.GenRndGnm(snap.PUNGraph, 500, 100000, False)
snap.SaveEdgeList(G,"poisson.edgelist.txt")

# re-wire, but keep the degree sequence
Gr = snap.GenRewire(G, 100)
snap.SaveEdgeList(Gr,"possion-R.edgelist.txt")
