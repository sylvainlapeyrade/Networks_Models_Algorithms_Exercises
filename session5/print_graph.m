% Generate a graphviz script that plots a graph.
% Input: Adjacency matrix, "node states" (could be partition identity, for example), and a filename to print to.
% The node state vector shall contain one element for each node and this element can be 0, 1, 2 or 3.

% adjacency_matrix[NxN matrix]: an adjacency matrix describing the network
% node_states[Nx1 vector]: a vector with elements in {0,1,2,3}  
% filename[string]: name of the file to print to, should have extension .gv for 'plotallgraphs.sh' to work without modification

function print_graph(adjacency_matrix,node_states,filename)

nr_nodes=size(adjacency_matrix,1);
labels ={'A','B','C','D'};
colors={'red','blue','black','green'};

file1=fopen(filename,'w');
fprintf(file1,'graph G {\n');
%fprintf(file1,['label=\"' graph_label '";']);
%fprintf(file1,'graph  [overlap=false, orientation=portrait,splines=true,remincross=true];\n');
%fprintf(file1,'node [color=grey, style=filled];\n');
%fprintf(file1,'node [fontname=\"Verdana\", size=\"30,30\"];\n');

%'Define' all nodes
for current_node=1:nr_nodes
    current_node_label = ['"' num2str(current_node) '\n' labels{node_states(current_node)+1}  '"'  ' [color = ' colors{node_states(current_node)+1} ']'];
    fprintf(file1,'%s ; \n',current_node_label);
end

% Connect the nodes
for to_node=1:nr_nodes
    for from_node=to_node+1:nr_nodes
        if adjacency_matrix(to_node,from_node)
            label1 = ['"' num2str(to_node) '\n' labels{node_states(to_node)+1} '"'];
            label2 = ['"' num2str(from_node) '\n' labels{node_states(from_node)+1} '"'];
            fprintf(file1,'%s -- %s ; \n',label1,label2);
        end
    end
end
fprintf(file1,'}');
fclose(file1);

return

