# Author: Sylvain Lapeyrade (sylla801)
# File: TSKS11-Lab2: Task 4

# ***************************** TASK 4 *****************************
# Calculate the Google PageRank score of each article in your network
# with parameter alpha = 0.85. List the top five articles and their
# PageRank score. Use the version of PageRank explained in the lecture
# notes. Also try some other values of alpha and comment on the result.

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

totals_colums = np.sum(m, axis=0)  # totals of the colums
for i in range(n):
    if totals_colums[i] == 0:  # If a column total is 0
        totals_colums[i] = 1/n  # it is replaced by 1/n

for j in range(n):
    for i in range(n):
        m[j][i] /= totals_colums[i]  # Normalisation to obtain B

# Vector with only ones (3000, 1)
vector_I = np.ones((n, 1), dtype=int)

identity_matrix = np.identity(n)  # Identity Matrix 3000x3000

alpha = 0.85  # 0.85 by default

# Close formed PageRank formula
page_rank_score = (1 / n) * \
    np.matmul(np.linalg.inv(identity_matrix - (alpha * m)), vector_I)

# Sum of all page rank scores
total_page_rank = float(np.sum(page_rank_score, axis=0))

for i in range(n):
    page_rank_score[i] /= total_page_rank  # Normalisation

# Arguments of the fives largest PageRank score
five_argmax_pagerank = page_rank_score.argsort(axis=None)[-5:][::-1]

print("\n\nNetwork {}: \n".format(network_number))
print("Alpha = {}: \n".format(alpha))
print("Nodes with the highest PageRank Score:")
for i in range(5):
    print(str(i + 1) + '.', "PageRank Score: {0:.6f}"
          .format(round(float(page_rank_score[five_argmax_pagerank[i]]), 6)),
          "| Title:", title_list[five_argmax_pagerank[i]])

# Exact solution for Task 5
for i in range(5):
    print("Exact values", i+1, ":",
          float(page_rank_score[five_argmax_pagerank[i]]))
