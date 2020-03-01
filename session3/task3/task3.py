# Author: Sylvain Lapeyrade (sylla801)
# File: TSKS11-Lab3: Task 3

import numpy as np
from scipy.sparse import csr_matrix
import matplotlib.pyplot as plt

# ***** PATH TO THE DATA FILES *****
data_location = "/courses/TSKS11/ht2019/data_and_fcns/session3/task3/"
data_location = "./"

mutual_friends = open(data_location + 'mutual-friends.txt', 'r')
affiliation = open(data_location + 'affiliation.txt', 'r')

mini_mutual_friends = open(data_location + 'mini-mutual-friends.txt', 'r')
mini_affiliation = open(data_location + 'mini-affiliation.txt', 'r')

# Loading the data in arrays
mutual_friends_data = np.loadtxt(mutual_friends, dtype=int)
affiliation_data = np.loadtxt(affiliation, dtype=int)

nr_nodes = max(map(max, mutual_friends_data))  # Number of nodes
nr_edges = len(mutual_friends_data[:, 0])  # Number of edges

j = (mutual_friends_data[:, 0] - 1).tolist()  # From Node Id
i = (mutual_friends_data[:, 1] - 1).tolist()  # To Node Id
s = mutual_friends_data[:, 2].tolist()  # Number of mutual friends


# Sparse matrix used for computation efficiency
adj_mat_directed = csr_matrix(arg1=(np.ones(nr_edges), (i, j)),
                              shape=(nr_nodes, nr_nodes))

# The network is undirected so we do step 3
adj_mat = adj_mat_directed + adj_mat_directed.transpose()


# ***** NEIGHBORHOOD OVERLAP *****
# Init 2 vectors with 0
neighborhood_overlap = np.zeros(shape=nr_edges)
sum_nodes_neigbors = np.zeros(shape=nr_nodes)

# Assign with sum of the nodes neighbors
for node in range(nr_nodes):
    sum_nodes_neigbors[node] = np.sum(adj_mat[node])

# Assign neighborhood overlap
for edge in range(nr_edges):
    neighborhood_overlap[edge] = s[edge] / (sum_nodes_neigbors[i[edge]] +
                                            sum_nodes_neigbors[j[edge]] - s[edge])

# ***** TIE STRENGTH *****
nr_affiliation = len(affiliation_data)  # Number of affiliation
nr_group = max(affiliation_data[:, 0])  # Number of group


group = (affiliation_data[:, 0] - 1).tolist()
node = (affiliation_data[:, 1] - 1).tolist()

# Sparse matrix used for computation efficiency
affiliation_mat = csr_matrix(arg1=(np.ones(nr_affiliation), (node, group)),
                             shape=(nr_nodes, nr_group))

tie_strength_vector = np.zeros(shape=nr_edges)
for edge in range(nr_edges):
    a = affiliation_mat[j[edge]] + affiliation_mat[i[edge]]
    a[a > 1] = 1
    tie_strength_vector[edge] = np.sum(a)

# Multiply affiliation matrix with its transposed
# tie_strength = np.matmul(affiliation_mat, affiliation_mat.transpose())

# Init correlation with 0 vector
correlation = np.zeros(shape=(int(np.max(tie_strength_vector)), nr_edges))

# For each edge assign correlation
for edge in range(nr_edges):
    correlation[int(tie_strength_vector[edge])-1] = neighborhood_overlap[edge]

# Assign corellation average for each tiestrength
correlation_avg = []
for tiestrength in range(len(correlation)):
    if np.count_nonzero(correlation[tiestrength]) > 0:
        correlation_avg.append(
            correlation[tiestrength][correlation[tiestrength] != 0].mean())

# Assign the Cumulative percentage of tie strength and the neighborhood overlap
cumulated_correlation_avg = 0
x, y = [], []
for i in range(len(correlation_avg)):
    cumulated_correlation_avg += correlation_avg[i]
    x.append(cumulated_correlation_avg / sum(correlation_avg))
    y.append(correlation_avg[i])

# Plot the graph
plt.plot(x, y, 'bo')
plt.xlabel("Cumulative percentage of tie strength")
plt.ylabel("Neighborhood overlap")
plt.show()
