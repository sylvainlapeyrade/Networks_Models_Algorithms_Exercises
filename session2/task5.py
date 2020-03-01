# Author: Sylvain Lapeyrade (sylla801)
# File: TSKS11-Lab2: Task 5

# ***************************** TASK 5 *****************************
# Implement the iterative version of PageRank. Compare the result after
# one, two, five, tenand 100 iterations with the “exact” solution to the
# equation system obtained in Task 4. Show how the top 5 nodes evolve over
# the iterations and show how close the iterative solution is to the exact.
# (The latter is most easily shown by looking at the norm of the
#  difference of the exact ranking and the iterative solution.)

import matplotlib.pyplot as plt
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

alpha = 0.85  # 0.85 by default

# Exact value form task4
exact_value = [0.01700290420794845, 0.011259014797820661,
               0.010662220718435296, 0.007094378199663314,
               0.007037192819241108]

diff_value = []  # Difference between value exact and iteration PR

totals_colums = np.sum(m, axis=0)  # totals of the colums

for j in range(n):
    for i in range(n):
        if totals_colums[i] == 0:
            m[j][i] = 1/n
        else:
            m[j][i] /= totals_colums[i]  # Normalisation to obtain B

# Vector with only ones (3000, 1)
vector_I = np.ones((n, 1), dtype=int)

# Initial page rank score value (can be anything execpt full 0)
page_rank_score = vector_I
# page_rank_score = np.random.rand(3000, 1)

# Iteration PageRank formula for 100 iterations
for i in range(1, 101):
    page_rank_score = np.matmul(
        (alpha * m) + ((1 - alpha) / n) * (vector_I * vector_I.transpose()),
        page_rank_score)

    # Sum of all page rank scores
    total_page_rank = float(np.sum(page_rank_score, axis=0))

    for j in range(n):
        page_rank_score[j] /= total_page_rank  # Normalisation

    # Arguments of the fives largest PageRank score
    five_argmax_pagerank = page_rank_score.argsort(axis=None)[-6:][::-1]

    if (i == 1 or i == 2 or i == 5 or i == 10 or i == 100):
        print("\n\nNetwork {}: \n".format(network_number))
        print("Alpha = {}: \n".format(alpha))
        print("Iteration = {}: \n".format(i))
        print("Nodes with the highest PageRank Score:")
        for k in range(5):
            print(str(k + 1) + '.', "PageRank Score: {0:.6f}"
                  .format(round(float(page_rank_score[five_argmax_pagerank[k]]), 6)),
                  "| Title:", title_list[five_argmax_pagerank[k]])
    diff_value_k = 0
    for k in range(5):
        # Exact solution for Task 5
        diff_value_k += abs(abs(exact_value[k]) -
                            abs(float(page_rank_score[five_argmax_pagerank[k]])))

    diff_value.append(diff_value_k)

# Plotting the graph of the diffrenece between closed form & Iteration PR Score
x = diff_value
plt.plot(x)
plt.ylabel("Difference between closed form & Iteration PR Score")
plt.xlabel("Iteration")
plt.show()
