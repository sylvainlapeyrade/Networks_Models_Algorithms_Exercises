# Author: Sylvain Lapeyrade (sylla801)
# File: TSKS11-Lab3 Task 1

import numpy as np
import csv
import matplotlib.pyplot as plt


# Files paths
file1 = 'G-degree-1.csv'  # Selected file

degree = []
coefficient = []
with open(file1) as csv_data_file:
    for row in csv.reader(csv_data_file):
        degree.append(float(row[0]))
        coefficient.append(float(row[1]))

# Plot the graph
plt.plot(degree, coefficient, 'bo')
plt.xlabel("degree")
plt.ylabel("local_clustering_coef")
plt.show()
