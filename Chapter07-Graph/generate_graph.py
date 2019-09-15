import re

def build_graph_from_file(graph, filename):
    graph_list = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            l = [int(x) for x in re.findall(r'\d+', line)]
            graph_list.append(l)

    for nodes in graph_list:
        graph.add_edge(nodes[0], nodes[1])

