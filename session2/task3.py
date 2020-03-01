# Author: Sylvain Lapeyrade (sylla801)
# File: TSKS11-Lab2: Task 3

# ***************************** TASK 3 *****************************
# Calculate the Katz Centrality of each article with
#  lamdba = 0.85 * (1/|lamdba_max|), where lamdba_max is the largest
#  eigenvalue of the adjacency matrix.
# List the top five articles and their Katz score.

import numpy as np

# The calculations being too expensive, only one file
#  will be dealt with at the same time

network_number = 1  # Number of the file wanted

title_file = open(
    '/courses/TSKS11/ht2019/data_and_fcns/session2/titles/{}.txt'
    .format(network_number), 'r')
link_file = open(
    '/courses/TSKS11/ht2019/data_and_fcns/session2/links/{}.txt'
    .format(network_number), 'r')

title_list = []
titles = title_file.read().splitlines()  # Array of the titles
for title in titles:
    title_list.append(title)

degree = np.loadtxt(link_file, dtype=int)  # Loads all links
n = max(map(max, degree))  # Number of nodes

m = np.zeros((n, n), dtype=float)  # Matrix M initialized with 0
for j in range(len(degree)):  # Put 1 for every links
    m[degree[j][1] - 1][degree[j][0] - 1] = 1

identity_matrix = np.identity(n)  # Identity Matrix 3000x3000

# Compute the eigenvalues of m.
katz_eigenvalues = np.linalg.eigvals(m)

# Vector with only ones (3000, 1)
vector_I = np.ones((n, 1), dtype=int)

alpha = 0.85 * (1 / max(abs(katz_eigenvalues)))  # Alpha as instrcuted

# Katz centrality formula
katz_centrality = (1 / n) * np.matmul(np.linalg.inv(
    identity_matrix - (alpha * m)), vector_I)

# Sum of all katz centrality
total_katz_centrality = float(np.sum(katz_centrality, axis=0))

for i in range(n):
    katz_centrality[i] /= total_katz_centrality  # Normalisation

# Arguments of the fives largest katz centrality
five_argmax_katz = katz_centrality.argsort(axis=None)[-5:][::-1]

print("\n\nNetwork {}: \n".format(network_number))
print("Nodes with the highest Katz Centrality:")
for i in range(5):
    print(str(i + 1) + '.', "Katz-Centrality: {0:.6f}"
          .format(round(float(katz_centrality[five_argmax_katz[i]]), 6)),
          "| Title:", title_list[five_argmax_katz[i]])
