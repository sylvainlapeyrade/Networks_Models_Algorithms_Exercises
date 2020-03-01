# Author: Sylvain Lapeyrade (sylla801)
# File: TSKS11-Lab5

from print_graph import print_graph
import numpy as np
import scipy.sparse

file1 = 'karate-network.csv'
file2 = 'mini-example.csv'
file3 = 'neural-example.csv'

network = file1
# num_lines = sum(1 for line in open(file1))

f_list = []
t_list = []
data = []
np_matrix = np.zeros(shape=(34, 34))
with open(network) as f:
    for line in f.readlines():
        f, t = line.split(',')
        np_matrix[int(f) - 1, int(t) - 1] = 1
        f_list.append(int(f) - 1)
        t_list.append(int(t) - 1)
        data.append(int(1))

sp_matrix = scipy.sparse.csr_matrix(
    (np.asarray(data), (np.asarray(f_list), np.asarray(t_list))), dtype=int)

s = np.zeros(shape=sp_matrix.shape[0], dtype=int)
s[: len(s) // 2] = 1

# Since our matrix is symmetric (and our network undirected)
#  we use just the upper triangle
print_graph(scipy.sparse.triu(sp_matrix, format='csc'), s, 'test_sparse3.gv')
print_graph(np.triu(np_matrix), s, 'test_numpy3.gv')
