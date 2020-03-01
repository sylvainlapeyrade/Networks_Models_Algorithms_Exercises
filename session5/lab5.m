% Author: Sylvain Lapeyrade (sylla801)
% File: TSKS11-Lab5

% Graphs are directed
network_name = './karate-network.csv';
network_name2 = './mini-example.csv';
network_name3 = './neural-example.csv';

network = load(network_name);

nr_nodes = max([network(:,1); network(:,2)]);
nr_edges = length(network(:,1));
adj_mat = sparse(network(:,2), network(:,1), ones(nr_edges, 1), nr_nodes, nr_nodes);

partition1 = network(1:nr_edges/2, :);
partition2 = network((nr_edges/2)+1:nr_edges, :);

% print_graph(adj_mat_directed, )