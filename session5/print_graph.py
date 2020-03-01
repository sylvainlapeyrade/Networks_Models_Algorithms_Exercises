# Author: Sylvain Lapeyrade (sylla801)
# File: TSKS11-Lab5: Function print Graph


# Function translated from Matlab to Python
def print_graph(adjacency_matrix, node_states, filename) -> None:
    """
    Generate a graphviz script that plots a graph.
    Input: Adjacency matrix, "node states" (could be partition identity,
     for example), and a filename to print to.
    The node state vector shall contain one element for each node
     and this element can be 0, 1, 2 or 3.


    :param adjacency_matrix: A `numpy.ndarray` or a `scipy.sparce matrix`
    :param node_states: A numpy.ndarray of shape N
    :param filename: A string which the resulting graphviz file should be
     called. For maximum compatibility make sure it ends on .gv otherwise
      the `plotallgraphs.sh` does not work without modification.
    """
    nr_nodes = adjacency_matrix.shape[0]
    labels = ['A', 'B', 'C', 'D']
    colors = ['red', 'blue', 'black', 'green']

    with open(filename, 'w') as file1:
        file1.write('graph G {\n')
        file1.write('graph [overlap=false, orientation=portrait,' +
                    'splines=true, remincross=true];\n')
        file1.write('node [color=grey, style=filled];\n')
        file1.write('node [fontname=\"Verdana\", size=\"30,30\"];\n')

        for current_node in range(0, nr_nodes):
            current_node_label = '"{}\\n{}" [color = {}] ;\n'.format(current_node + 1,
                                                                     labels[node_states[current_node]],
                                                                     colors[node_states[current_node]])
            file1.write(current_node_label)
            for friend in adjacency_matrix[:, current_node].nonzero()[0]:
                link = '"{}\\n{}" -- "{}\\n{}";\n'.format(current_node + 1,
                                                          labels[node_states[current_node]],
                                                          friend + 1,
                                                          labels[node_states[friend]])
                file1.write(link)

        file1.write('}')
