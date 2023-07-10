# Author: Sylvain Lapeyrade (sylla801)
# File: TSKS11-Lab2: Task 1

# ***************************** TASK 1 *****************************
# Calculate the in and out degrees of all articles.
#  Show the results in two lists; one list shows the in and out
#  degrees of the five nodes with highest in-degree; one list shows
#  the in and out degrees of the five nodes with highest out-degree.

import random
import numpy as np

# Randomly select (at least) five of the 20 available networks
network_number = 5
networks = random.sample(range(1, 20), network_number)

title_file = []
link_file = []
networks = [1, 2, 3, 4, 5]  # Override the random choice

for i in range(network_number):
    title_file.append(open(
        '/courses/TSKS11/ht2019/data_and_fcns/session2/titles/{}.txt'
        .format(networks[i]), 'r'))
    link_file.append(open(
        '/courses/TSKS11/ht2019/data_and_fcns/session2/links/{}.txt'.
        format(networks[i]), 'r'))

    title_list = []
    titles = title_file[i].read().splitlines()  # Array of the titles
    for title in titles:
        title_list.append(title)

    degree = np.loadtxt(link_file[i], dtype=int)  # Loads all links
    n = max(map(max, degree))  # Number of nodes N

    m = np.zeros((n, n), dtype=float)  # Matrix M initialized with 0

    for j in range(len(degree)):  # Put 1 for every links
        m[degree[j][1] - 1][degree[j][0] - 1] = 1

    out_degree = np.sum(m, axis=0)  # Column
    in_degree = np.sum(m, axis=1)  # Row

    total_in_degree = sum(in_degree)
    total_out_degree = sum(out_degree)

    for j in range(n):
        in_degree[j] /= total_in_degree  # Normalize
        out_degree[j] /= total_out_degree  # Normalize

    # Get the index of the five maximum value
    five_argmax_in = in_degree.argsort()[-5:][::-1]
    five_argmax_out = out_degree.argsort()[-5:][::-1]

    print("\n\nNetwork {}: \n".format(networks[i]))
    print("Nodes with the highest In-Degree:")
    for i in range(5):
        print(str(i + 1) + '.', "in-degree:{0:.6f}"
              .format(round(in_degree[five_argmax_in[i]], 6)),
              "| out-degree:{0:.6f}".format(
            round(out_degree[five_argmax_in[i]], 6)),
            "| Title:", title_list[five_argmax_in[i]])

    print("\nNodes with the highest Out-Degree:")
    for i in range(5):
        print(str(i + 1) + '.', "out-degree:{0:.6f}"
              .format(round(out_degree[five_argmax_out[i]], 6)),
              "| in-degree:{0:.6f}".format(
            round(in_degree[five_argmax_out[i]], 6)),
            "| Title:", title_list[five_argmax_out[i]])
