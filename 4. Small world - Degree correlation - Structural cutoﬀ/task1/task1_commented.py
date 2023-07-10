#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 11:10:05 2018

Small world experiments

@author: Erik G. Larsson, 2018-2019
"""

import sys
import snap
sys.path.append("/courses/tsks11/ht2019/snap-4.1.0-4.1-centos6.5-x64-py2.6/")


# circle network

# Generates and returns a random small-world graph using the Watts-Strogatz model.
#  We assume a circle where each node creates links to NodeOutDeg other nodes.
G1 = snap.GenSmallWorld(nodes=1000, nodeOutDeg=2, rewireProb=0)

# Returns approximate Effective Diameter(90-th percentile of the distribution of shortest
#  path lengths) of a graph(by performing BFS from NTestNodes random starting nodes).
print snap.GetBfsEffDiam(Graph=G1, NTestNodes=50, IsDir=False)

# Watt-Strogatz, 0.01
G2 = snap.GenSmallWorld(Nodes=1000, NodeOutDeg=2, RewireProb=0.01)
print snap.GetBfsEffDiam(Graph=G2, NTestNodes=50, IsDir=False)

# Watt-Strogatz, 0.1
G3 = snap.GenSmallWorld(Nodes=1000, NodeOutDeg=2, RewireProb=0.01)
print snap.GetBfsEffDiam(Graph=G3, NTestNodes=50, IsDir=False)

# Amazon network
# Loads a (directed, undirected or multi) graph from a text file InFNm
#  with 1 edge per line (whitespace separated columns, int node ids).
G = snap.LoadEdgeList(GraphType=snap.PUNGraph,
                      InFNm="/courses/TSKS11/ht2019/data_and_fcns/session4/task1/amazon0302.txt",
                      SrcColId=0, DstColId=1)

# Prints basic Graph statistics to standard output or to a file named OutFNm.
# Additional extensive computationally expensive statistics are computed when Fast=False.
# snap.PrintInfo(G, "amazon", "_amazon-info.txt", False)
print snap.GetBfsEffDiam(Graph=G, NTestNodes=50, IsDir=False)

# A Watts Strogatz model is a random graph generation model that produces graphs
#  with small-world properties, including short average path lengths and high clustering
#
# Diameters
# - Circle network with node degree 4 => 224.75
# - Watts-Strogatz network based on a circle network with node degree 4,
#    and re-wiring probability 0.01 => 36.919109027
# - Watts-Strogatz network based on a circle network with node degree 4,
#    and re-wiring probability 0.1 => 11.0697258641
# - The Amazon co-purchasing network (from the SNAP datasets) => 10.7011804232
