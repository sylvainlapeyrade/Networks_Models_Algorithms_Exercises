# Author: Sylvain Lapeyrade (sylla801)
# File: TSKS11-Lab4: Task 2-3

import numpy as np
from scipy import sparse
import pandas as pd
import matplotlib.pyplot as plt

# Link with the path of the txt files
link0 = './task2/mini-network.edgelist.txt'
link1 = './task2/poisson.edgelist.txt'
link2 = './task2/poisson-R.edgelist.txt'
link3 = './task2/collaboration.edgelist.txt'
link4 = './task2/collaboration-R.edgelist.txt'
link5 = './task3/n1.edgelist.txt'
link6 = './task3/n2.edgelist.txt'
link7 = './task3/n3.edgelist.txt'
link8 = './task3/n4.edgelist.txt'
link9 = './task3/n5.edgelist.txt'

link_name = link4  # Name of current path
link_file = open(link_name, 'r')

edgelist = np.loadtxt(link_file, dtype=int)  # Loads all links
nr_nodes = max(map(max, edgelist))+1  # Number of nodes
nr_edges = len(edgelist)  # Number of Edges


j = (edgelist[:, 0]).tolist()  # From Node Id
i = (edgelist[:, 1]).tolist()  # To Node Id

# Sparse matrix used for computation efficiency
sparse_matrix = sparse.csr_matrix(arg1=(np.ones(nr_edges), (i, j)),
                                  shape=(nr_nodes, nr_nodes))

# The network is undirected so we add the transpose of the matrix
network = sparse_matrix + sparse_matrix.transpose()

# Initinalize degree and knns with 0 vectors
degrees = np.zeros(shape=nr_nodes)
knns = np.zeros(shape=nr_nodes)

# Calculate the degree and the knn of each node
for node in range(nr_nodes):
    degrees[node] = np.sum(network[node, :])
    knn = np.sum([np.sum(network[neighbor, :])
                  for neighbor in network[:, node].nonzero()[0]])
    knns[node] = knn / degrees[node]

# Use DataFrame to link degree and knn (and do the mean)
data = pd.DataFrame({'degree': degrees, 'knn': knns})
means = data.groupby('degree').mean()

# *** Coefficient Correlation ***
# Initilise 2 vectors x, y with 0
x, y = np.zeros(shape=(nr_edges)), np.zeros(shape=(nr_edges))

# Assign those vectors with the node degree
for i, edge in enumerate(edgelist):
    x[i], y[i] = degrees[edge[0]], degrees[edge[1]]

# Substract x and y with their mean
xm, ym = x - x.mean(), y - y.mean()

# Pearson Correlation Coefficient implementation
r = np.add.reduce(xm * ym) / np.sqrt(np.sum(xm**2) * np.sum(ym**2))
r = max(min(r, 1.0), -1.0)  # In case abs(r) > 1

print('Network:', link_name)
print('Correlation Coefficient r=', r)

# Plot of the KNNs and their Degree
plt.ylabel("KNN")
plt.xlabel("Degree")
plt.plot(means.index, means['knn'])
plt.show()

# *** TASK 2 ***
# Poisson & Collaboration Graphs hae undergone re-wiring through
#  Degree Preserving Randomization to assess whether the variations
#  in the graphs could simply be artifacts of the graph's inherent structural
#  properties rather than properties unique to the nodes

# Poisson = -0.0028966
# Poisson rewired = -0.00329
# The poisson network was pretty balanced so
#  the rewiring doesnt affect it much
# => This is due to the graph

# Collaboration = 0.134
# Collaboration rewired = -0.005783
# The collaboration network on the other hand is more affected,
#  while there is still some peaks it is more evened out
# => This is due to the nodes


# *** TASK 3 ***
# The Correlation Coefficient are very similar (i.e the knn and Degree also).
#  We can asssume that under Degree Preserving Randomization rewiring
#  we would obtain more or less the sames graphs. So we can deduce that the
#  graphs  share same properies. (Scale free ?)
