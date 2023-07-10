import matplotlib.pyplot as plt
import pandas as pd
import math

df = pd.read_csv('./session1/task1/X-centrality.csv')

betweenness = df["Betweenness"]
clustCoeff = df["ClustCoeff"]

for i in range(betweenness.size):
    betweenness[i] += 1

plt.plot(betweenness, clustCoeff)
plt.xscale('log', basex=10)
plt.xlabel('Clustering Coefficient')
plt.ylabel('Betweenness centrality (logarithmic scale)')
plt.title('Betweenness centrality against clustering coefficient')
# plt.legend()
plt.show()
