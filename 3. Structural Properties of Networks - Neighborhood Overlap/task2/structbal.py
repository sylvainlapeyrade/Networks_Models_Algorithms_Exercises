#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
TSKS11 Hands-on session 3
Look at some triangles in a signed network and see if
 structural balance seems to hold 

Erik G. Larsson, 2018
"""

from random import randint
import sys
sys.path.append("/courses/tsks11/ht2019/snap-4.1.0-4.1-centos6.5-x64-py2.6/")
import snap


# Assign a value to each edge
def getsign(n1, n2):
    p = 0
    n = 0
    if Gp.IsEdge(n1, n2):  # If the edge is positive
        p = 1
    if Gn.IsEdge(n1, n2):  # If the edge is negative
        n = -1
    return p+n


G = snap.TUNGraph.New()  # all edges
Gp = snap.TUNGraph.New()  # positive edges
Gn = snap.TUNGraph.New()  # negative edges

#f = open('complete-graph-edges.txt')
#f = open('soc-sign-epinions.txt')
f = open('/courses/TSKS11/ht2019/data_and_fcns/session3/task2/soc-sign-epinions.txt')
i = 1
Nneglected = 0

for line in f:
    s = line
    if not s[0] == '#':
        x = s.split("\t")
        n1 = int(x[0])
        if not G.IsNode(n1):  # If the Node is not already in the graph
            G.AddNode(n1)  # Add the node to the Graph G
            Gp.AddNode(n1)  # Add the node to the Graph Go
            Gn.AddNode(n1)  # Add the node to the Graph Gn
        n2 = int(x[1])
        if not G.IsNode(n2):  # If the Node is not already in the graph
            G.AddNode(n2)  # Add the node to the Graph G
            Gp.AddNode(n2)  # Add the node to the Graph Go
            Gn.AddNode(n2)  # Add the node to the Graph Gn

        if (n1 == n2):
            continue

        sign = int(x[2])

        if G.IsEdge(n1, n2):  # If the edge between n1 and n2 is positive
            if Gp.IsEdge(n1, n2) and (sign == -1):
                # print n1, n2, "already exists with different sign"
                Nneglected = Nneglected+1
                Gp.DelEdge(n1, n2)

            if Gn.IsEdge(n1, n2) and (sign == 1):
                # print n1, n2, "already exists with different sign"
                Nneglected = Nneglected+1
                Gn.DelEdge(n1, n2)
        else:  # If the edge between n1 and n2 is negative
            G.AddEdge(n1, n2)
            if (sign == 1):  # if the sign is positive add to Gp else to Gn
                Gp.AddEdge(n1, n2)
            else:
                Gn.AddEdge(n1, n2)

            if (i % 50000 == 0):
                print i
                # print s

            # print n1, n2, sign
        i = i+1


snap.PrintInfo(G, "signed network", "", False)
snap.PrintInfo(Gp, "signed network", "", False)
snap.PrintInfo(Gn, "signed network", "", False)

print "total number of edges:", i-1
print "number of inconsistent edges:", Nneglected


# sample some random triangles
for i in range(1, 500):
    n1 = G.GetRndNId()  # Get a random node id
    n1i = G.GetNI(n1)  # Get a rondom node I
    if n1i.GetDeg() >= 2:  # If the node has at least two edges
        d = n1i.GetDeg()  # Get node I degree
        # Select two random different degree nodes
        i1 = randint(0, d-1)
        while 1 == 1:
            i2 = randint(0, d-1)
            if not i1 == i2:
                break

        n2 = n1i.GetNbrNId(i1)  # Select node 2 Id
        n3 = n1i.GetNbrNId(i2)  # Select node 3 Id
        if not G.IsEdge(n2, n3):  # If there is an edge between node 2 and 3
            continue

        s12 = getsign(n1, n2)  # Get sign between node 1 & 2
        s13 = getsign(n1, n3)  # Get sign between node 1 & 3
        s23 = getsign(n2, n3)  # Get sign between node 2 & 3

        print "========================="
        print "edge ", n1, " - ", n2, " has sign ", s12
        print "edge ", n1, " - ", n3, " has sign ", s13
        print "edge ", n2, " - ", n3, " has sign ", s23

        # If at least one edge == 0, the triangle is ignore
        if (s12*s13*s23 == 0):
            print"The triangle", n1, n2, n3,
            " contains at least one inconsistent edge, ignoring it."
            continue

        # If either all edges are positive or 2 negatives,
        #  the triangle is balanced otherwise it is unbalanced
        if (s12*s13*s23 == 1):
            print "The triangle", n1, n2, n3, "is strongly balanced."
        else:
            print "The triangle", n1, n2, n3, "is unbalanced."
