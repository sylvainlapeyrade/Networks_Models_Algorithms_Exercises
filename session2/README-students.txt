
--- Links ---
This file has the form
FromNode	ToNode
1		2
1		3
2		5
.		.
.		.

This file describes the entire network by listing all edges on
separate rows. In the example above, we see that node 1 points to
nodes 2 and 3. Going through the entire list of edges will give you
the network.

When loading the network, it is a good idea to work with sparse
matrices, as most of the elements in the adjacency matrix will be
zero. In Matlab/octave, the load command can be used to get the
data. You can then use the sparse command to construct the adjacency
matrix.

data = load('links.txt');
A = sparse(...)

Note that A is not symmetric. A, and A transpose are two different
networks. Be aware of what convention you use.


--- Titles --- 

In this file you find the titles of the wikipedia article
corresponding to the node number. Row x in this file is the title of
node x in the 'links' file. There is exactly ONE title per row.

Note: Be careful when loading this file, since some of the titles
include commas (,). Please make sure, if you read this file, that you
have as many titles as you have nodes.
