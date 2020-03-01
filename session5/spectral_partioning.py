# Author: Sylvain Lapeyrade (sylla801)
# File: TSKS11-Lab5 Spectral partioning

import numpy as np
import csv
from scipy import sparse
from print_graph import print_graph

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

# Initialize degree with 0 vectors
degrees = np.zeros(shape=nr_nodes)

# Calculate the degree of each node
for node in range(nr_nodes):
    degrees[node] = np.sum(sparse_matrix[node, :])

# Laplacian matrix
laplacian_matrix = np.diag(degrees) - sparse_matrix

# Eigen values and vectors of the Laplacian matrix
eigenvalues, eigenvectors = np.linalg.eig(laplacian_matrix)

# Index of the second eigenvalue => Phi
phi = np.argsort(eigenvalues)[1]

# Node Group (Here n1 = n2)
node_group = nr_nodes / 2

# According to the formula from the Supplementary Materials
t1 = 2 * np.sqrt((node_group * node_group) / nr_nodes) * phi
t2 = (node_group - node_group) / nr_nodes * np.ones(shape=nr_nodes, dtype=int)
s = t1 + t2

s_sorted = np.argsort(s)

s2 = np.zeros(shape=nr_nodes, dtype=int)
s2[s_sorted[:int(node_group)]] = 1

group1 = np.zeros(shape=nr_nodes, dtype=int)
group2 = np.zeros(shape=nr_nodes, dtype=int)

group1[s2 == 1] = 1
group2[s2 == 0] = 1

print("Graph: {}\n".format(filepath))
print("Group1 length={}, Group2 length={} (total={})".format(
    len(group1[s2 == 1]), len(group2[s2 == 1]), nr_nodes))

# Initialize node states to 0
node_states = np.zeros(shape=sparse_matrix.shape[0], dtype=int)

# Assign  node_states
if len(group1) <= len(group2):
    for node in range(len(group1)):
        if group1[node] == 1:
            node_states[node] = 1
else:
    for node in range(len(group2)):
        if group2[node] == 1:
            node_states[node] = 1

# The matrix is symmetric so we can use the matrix upper triangle
print_graph(sparse.triu(A=sparse_matrix, format='csc'),
            node_states, filepath+'_spectral.gv')
