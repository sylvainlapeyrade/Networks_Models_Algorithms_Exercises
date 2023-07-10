# Author: Sylvain Lapeyrade (sylla801)
# File: TSKS11-Lab5 Kernighan-Lin partioning

import numpy as np
import csv
from scipy import sparse
from print_graph import print_graph
import random


# Files paths
file1 = 'karate-network'
file2 = 'mini-example'
file3 = 'neural-example'

filepath = file1  # Selected file

i = []
j = []
edges = []
with open(filepath+'.csv') as csv_data_file:
    for row in csv.reader(csv_data_file):
        i.append(int(row[0]) - 1)
        j.append(int(row[1]) - 1)
        edges.append((int(row[0]) - 1, int(row[1]) - 1))


nr_nodes = max(i)+1  # Number of nodes
nr_edges = len(i)  # Number of Edges

# Sparse matrix used for computation efficiency
sparse_matrix = sparse.csr_matrix(arg1=(np.ones(nr_edges), (i, j)),
                                  shape=(nr_nodes, nr_nodes)).toarray()

# Listing vertices
v = list(range(nr_nodes))

# Dividing nodes in random n1 n2 groups
random.shuffle(v)
cut = int(nr_nodes/2)
n1, n2 = np.sort(v[:cut]), np.sort(v[cut:])
pairs = len(n1)*len(n2)


def cut_size(n1, n2):
    r_old = 0
    for i in n1:
        for j in n2:
            if sparse_matrix[i][j] == 1:
                r_old = r_old + 1
    return (r_old)


def best_swap(n1, n2):
    # Will check change in delR for all pairs and will swap pair with optimal cut size
    # And return best partition and its cut size
    mark = []
    partition = []
    cut_s = []
    while(len(mark) != pairs-1):
        r_best, ij, part = [], [], []
        r_old = cut_size(n1, n2)
        for i in range(len(n1)):
            for j in range(len(n2)):
                if ([n1[i], n2[j]] not in mark and ([n2[j], n1[i]] not in mark)):
                    n11, n22 = n1.copy(), n2.copy()
                    n11[i] = n2[j]
                    n22[j] = n1[i]
                    del_R = r_old - cut_size(n11, n22)  # Change in cut size
                    r_best.append(del_R)
                    part.append([n11, n22])
                    ij.append([n11[i], n22[j]])

        a = np.argmax(r_best)
        c_part = part[a]
        partition.append(c_part)
        mark.append(ij[a])
        cut_s.append(cut_size(c_part[0], c_part[1]))
        n1, n2 = c_part[0], c_part[1]
    return(cut_s[np.argmin(cut_s)], partition[np.argmin(cut_s)])


def kernighan_lin(n1, n2):
    cs = []
    for i in range(1):  # Iterations
        cutsize, partition = best_swap(n1, n2)
        n1 = partition[0]
        n2 = partition[1]
        cs.append(cutsize)
        if len(cs) >= 10:  # Checking if cut size is converging
            ts = cs[-5:]
            if (ts[0] == ts[1] == ts[2] == ts[3] == ts[4]):
                break
    return(cutsize, partition)


c, p = kernighan_lin(n1, n2)
group1, group2 = np.sort(p[0]), np.sort(p[1])
print("\nCut size is : {}".format(c))
print("Partition 1 : {}".format(group1))
print("Partition 2 : {}".format(group2))

# Initialize node states to 0
node_states = np.zeros(shape=sparse_matrix.shape[0], dtype=int)

# Assign  node_states
if len(group1) >= len(group2):
    for node in group1:
        node_states[node] = 1
else:
    for node in group2:
        node_states[node] = 1

# The matrix is symmetric so we can use the matrix upper triangle
print_graph(sparse.triu(A=sparse_matrix, format='csc'),
            node_states, filepath+'_kl.gv')
