# Author: Sylvain Lapeyrade (sylla801)
# File: TSKS11-Lab2: Task 2

# ***************************** TASK 2 *****************************
# Calculate the hub and authority centrality of all articles.
# Display the result in the same way as in the previous task.

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

mt_m = np.matmul(m.transpose(), m)  # M transposed * M
m_mt = np.matmul(m, m.transpose())  # M* M transposed

# eig: Compute the eigenvalues and right eigenvectors of a square array.
hub_eigenvalues, hub_eigenvectors = np.linalg.eig(mt_m)
# eigh: return the eigenvalues and eigenvectors of a complex Hermitian
#  (conjugate symmetric) or a real symmetric matrix.
auth_eigenvalues, auth_eigenvectors = np.linalg.eigh(m_mt)

# Max hub and auth eigenvalue
max_hub_eigenvalue = np.argmax(abs(hub_eigenvalues))
max_auth_eigenvalue = np.argmax(abs(auth_eigenvalues))

total_eigenvector_hub_max = sum(hub_eigenvectors[:, max_hub_eigenvalue])
total_eigenvector_auth_max = sum(auth_eigenvectors[:, max_auth_eigenvalue])

# Normalize both hub and auth authorities
for i in range(n):
    hub_eigenvectors[:, i] = abs(hub_eigenvectors[:, i]
                                 / total_eigenvector_hub_max)
    auth_eigenvectors[:, i] = abs(auth_eigenvectors[:, i]
                                  / total_eigenvector_auth_max)

# Get the index of the five maximum value
five_max_hub_arg = abs(
    hub_eigenvectors[:, max_hub_eigenvalue]).argsort()[-5:][::-1]
five_max_auth_arg = abs(
    auth_eigenvectors[:, max_auth_eigenvalue]).argsort()[-5:][::-1]

print("\n\nNetwork {}: \n".format(network_number))
print("Nodes with the highest Hub Centrality:")
for i in range(5):
    print(str(i + 1) + '.', "Hub centrality:{0:.6f}".format(
        round(abs(hub_eigenvectors[:, max_hub_eigenvalue]
                  [five_max_hub_arg[i]]), 6)),
          "| Authority centrality::{0:.6f}".format(
        round(abs(auth_eigenvectors[:, max_auth_eigenvalue]
                  [five_max_hub_arg[i]]), 6)),
          "| Title:", title_list[five_max_hub_arg[i]])

print("\nNodes with the highest Authority Centrality:")
for i in range(5):
    print(str(i + 1) + '.', "Authority centrality::{0:.6f}".format(
        round(abs(auth_eigenvectors[:, max_auth_eigenvalue]
                  [five_max_auth_arg[i]]), 6)),
          "| Hub centrality::{0:.6f}".format(
        round(abs(hub_eigenvectors[:, max_hub_eigenvalue]
                  [five_max_auth_arg[i]]), 6)),
          "| Title:", title_list[five_max_auth_arg[i]])
