
Data analysis:

Use analysis.cpp to compute some basic metrics of the graph G.edges (first copy the graph of interest to G.edges)

Output files are
* G-clustering.csv: comma-separated file with clustering coefficients per node
* G-degree.csv: comma-separated file with degree distribution and cumulative degree distribution

analyze_all.sh: simple shell script that analyzes all graphs

# If you want to run the analyze script, run the following commands in the terminal
$make
$chmod +x analyze_all.sh
$./analyze_all.sh

Running the above analysis is not necessary to solve the lab, but might be helpful.

If you have trouble opening/handeling the larger networks in Gephi,
make sure you don't have any other tabs open in Gephi. If things are
still slow, please use the computers in the lab.

===

Data generation: use synth_data.cpp

*********************************************************************************************************

Small world: 
-Short average distance (path length)
-High clustering coefficients (on high <c>)
