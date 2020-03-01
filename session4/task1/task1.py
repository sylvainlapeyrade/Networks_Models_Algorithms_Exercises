#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 11:10:05 2018

Small world experiments

@author: Erik G. Larsson, 2018-2019
"""

import sys
sys.path.append("/courses/tsks11/ht2019/snap-4.1.0-4.1-centos6.5-x64-py2.6/")
import snap

# circle network
G1 = snap.GenSmallWorld(1000, 2, 0)
print snap.GetBfsEffDiam(G1, 50, False)

# Watt-Strogatz, 0.01
G2 = snap.GenSmallWorld(1000, 2, 0.001)
print snap.GetBfsEffDiam(G2, 50, False)

# Watt-Strogatz, 0.1
G3 = snap.GenSmallWorld(1000, 2, 0.1)
print snap.GetBfsEffDiam(G3, 50, False)

# Amazon network
G = snap.LoadEdgeList(
    snap.PUNGraph, "/courses/TSKS11/ht2019/data_and_fcns/session4/task1/amazon0302.txt", 0, 1)
# snap.PrintInfo(G, "amazon", "_amazon-info.txt", False)
print snap.GetBfsEffDiam(G, 50, False)
