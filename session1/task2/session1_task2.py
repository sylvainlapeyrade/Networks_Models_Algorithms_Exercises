#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
TSKS11 Hands-on session 1

Erik G. Larsson 2018-2019
"""

from save_Gephi import saveGephi
import os
import snap
import sys
sys.path.append("../..")
sys.path.append("/courses/tsks11/ht2019/data_and_fcns/")
sys.path.append("/courses/tsks11/ht2019/snap-4.1.0-4.1-centos6.5-x64-py2.6/")

TPATH = "/courses/tsks11/ht2019/data_and_fcns/session1/"

# PNGraph, a directed graph;
# PUNGraph, an undirected graph;
# PNEANet, a directed network;

# Generate a complete graph with 5 nodes (K5) and look at it via Graphviz
G = snap.GenFull(GraphType=snap.PUNGraph, Nodes=5)
# for EI in G.Edges():
#    print "link from %d to %d" % (EI.GetSrcNId(), EI.GetDstNId())

# Saves Graph to the .DOT file format used by GraphViz
snap.SaveGViz(Graph=G, OutFNm="_undirected-completely-connected.dot",
              Desc="Undirected Completely Connected Network", NodeLabels=True)
# Draws undirected graphs using the generated .dot file
os.system("neato -Tpdf _undirected-completely-connected.dot >_undirected-completely-connected.pdf")

# Generate a star graph and visualize in Graphviz
G = snap.GenStar(GraphType=snap.PNGraph, Nodes=10, IsDir=True)
# for EI in G.Edges():
#    print "edge: (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId())

# Saves Graph to the .DOT file format used by GraphViz
snap.SaveGViz(Graph=G, OutFNm="_directed-star.dot", Desc="Directed Star Graph", NodeLabels=True)
# Draws undirected graphs using the generated .dot file
os.system("neato -Tpdf _directed-star.dot >_directed-star.pdf")

# Generate some Poisson random graphs and visualize with Gephi
G1 = snap.GenRndGnm(GraphType=snap.PUNGraph, Nodes=100, Edges=50)
G2 = snap.GenRndGnm(GraphType=snap.PUNGraph, Nodes=100, Edges=100)
G3 = snap.GenRndGnm(GraphType=snap.PUNGraph, Nodes=100, Edges=1000)

# save graphs generated as readable files by Gephi
saveGephi(G1, "_Poisson-1.NET")
saveGephi(G2, "_Poisson-2.NET")
saveGephi(G3, "_Poisson-3.NET")

# Generate one other Poisson random graph
G4 = snap.GenRndGnm(GraphType=snap.PUNGraph, Nodes=1000, Edges=10000)
# Plots the in-degree distribution of Graph
snap.PlotInDegDistr(G4, "_Poisson-4", "Poisson, degree distribution")

# Generate a scale-free network and visualize with Gephi
G1 = snap.GenPrefAttach(Nodes=10, NodeOutDeg=3)
G2 = snap.GenPrefAttach(Nodes=50, NodeOutDeg=5)
G3 = snap.GenPrefAttach(Nodes=100, NodeOutDeg=10)

# save graphs generated as readable files by Gephi
saveGephi(G1, "_Pref-attach-1.NET")
saveGephi(G2, "_Pref-attach-2.NET")
saveGephi(G3, "_Pref-attach-3.NET")
# Prints basic Graph statistics to standard to a file
snap.PrintInfo(Graph=G3, Desc="Python type PNGraph", OutFNm="_Pref-attach-3.info.txt",
 Fast=False)

# Generate one other Poisson random graph
G4 = snap.GenPrefAttach(Nodes=100000, NodeOutDeg=10)
# Plots the in-degree distribution of Graph
snap.PlotInDegDistr(Graph=G4, FNmPref="_Pref-attach-4",
                    DescStr="Preferential attachment 4, degree distribution")


# Examine the 88234-edge subnetwork of the Facebook graph
# http://snap.stanford.edu/data/ego-Facebook.html
# Loads a graph from a text file with 1 edge per line
G = snap.LoadEdgeList(GraphType=snap.PUNGraph, InFNm=TPATH + "facebook_combined.txt",
SrcColId=0, DstColId=1)
# Prints basic Graph statistics to standard to a file
snap.PrintInfo(Graph=G, Desc="facebook", OutFNm="_facebook-info.txt", Fast=False)

# Examine by some random sampling if the "small-world" property of Facebook seems to be true on this sub-network
# (Not much can be concluded from this actually, since the sub-network is just a small collection of ego-networks,
# so the point here is only to illustrate some SNAP functionality.)

for i in range(1, 25):
    # Returns an ID of a random node in the graph
    N1 = G.GetRndNId()
    N2 = G.GetRndNId()

    # Returns the length of the shortest path from a specified node to all other nodes in the network.
    L = snap.GetShortPath(Graph=G, SrcNId=N1, NIdToDistH=N2)
    print L

# Examine the Amazon product co-purchase network
# http://snap.stanford.edu/data/amazon0302.html
# Loads a graph from a text file with 1 edge per line
G = snap.LoadEdgeList(GraphType=snap.PUNGraph, OutFNm=TPATH + "amazon0302.txt",
 SrcColId=0, DstColId=1)
# Prints basic Graph statistics to standard to a file
snap.PrintInfo(Graph=G, Desc="amazon", OutFNm="_amazon0302-info.txt", Fast=False)
