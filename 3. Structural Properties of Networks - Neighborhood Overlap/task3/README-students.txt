This file gives a short introduction to the files in this task. To manage large, sparse matrices Matlab/Octave see the function 'sparse'.

The data files are located in /courses/TSKS11/ht2019/data_and_fcns/session3/task3/

### mutual-friends.txt ###
Format:
FromNodeId	ToNodeId		nr-of-mutual-friends
n1					nX					a
n1					nY					b
.						.						.
.						.						.
.						.						.


The file contains all edges in the network, one per line, and describes how the nodes are
 connected and the mutual friends between all connected nodes. Note that the youtube network
  is undirected, but this file describes each link once, (i.e. only n1-nX, not nX-n1). 

All nodes in this network are connected.


### affiliation.txt ###
Format:
GroupId		Member (NodeId)
g1		nX
g1		nY
g2		nZ
.		.
.		.
.		.

The file contains a number of affiliations, one per line, between groups 
and users (bipartite graph).
There is a link between group g and user u if user u is a member of group g.
 Note that there are users
 that are not members in any group. The NodeIds in both files are ''synchronized'',
  meaning that NodeId 2345 refers to the same node.

### The task ###
The task is specified in the lab instructions, but a few more details can be found here.

Each edge will have a corresponding tie strength and neighborhood overlap.
 How the neighborhood overlap is correlated to the tie strength.
 For each tie strength, you compute the average neighborhood overlap.
 Your plot should only have one value of neighborhood overlap (the average)
 for each tie strength. Many edges will have the same tie strength.

### Loading the data ###
The data is given in two columns separated by a whitespace. There are several way of
 loading this into Matlab/Octave (or any other language). This is one way of doing it:

data = load('mutual-friends.txt');

Once you have loaded the data, you can transform it to an adjacency matrix
 with the use of 'sparse'.

A = sparse(data(:,1),data(:,2),ones(nr_edges,1),nr_nodes,nr_nodes);

Note that this is the "onesided" adjacency matrix, to get one that is symmetric, you can use

A = sparse([data(:,1);data(:,2)],[data(:,2);data(:,1)],ones(2*nr_edges,1),nr_nodes,nr_nodes);

instead.

### How to handle the data ###
These data sets are large, and even if you use sparse matrices to make your code more effective,
 it is important to be careful with how you code. In particular, do not try to solve the
  lab with a double loop over all the nodes:
for nodes1 = 1:nr_nodes
	for nodes2 = 1:nr_nodes
		--do things here--
	endfor
endfor

Doing this will take a very, very long time and there are much more
 efficient ways to calculate what you need.

We strongly recommend that you use a small data set when trying out your functions. It is extemely 
inefficient to have to wait more than a few seconds when debugging. Keep it small in the beginning, and 
once you are confident your program works as it should, try it on the whole network. (It may still take 
some time to solve for the whole network. (As a reference the lab takes around
 100 seconds to solve on a single core on a reasonably fast laptop.)
