from Chapter07_Graph.generate_graph import build_graph_from_file
from Chapter07_Graph.sparse_graph import SparseGraph

class ShortestPath:
    def __init__(self, graph, start_node):
        self.graph = graph
        self.start_node = graph.nodes_dict[start_node]
        self.calc()

    def calc(self):
        self.start_node.set_distance(0)
        self.start_node.set_pred(None)
        queue = []
        queue.append(self.start_node)
        while len(queue) > 0:
            current_node = queue.pop(0)
            for node in current_node.get_connectedTo():
                if not node.is_visited():
                    node.set_distance(current_node.get_distance() + 1)
                    node.set_visited(True)
                    node.set_pred(current_node)
                    queue.append(node)

    def has_path(self, w):
        assert w >= 0 and w < len(self.graph.nodes_dict)
        return self.graph.nodes_dict[w].is_visited()

    def path(self, w):
        assert w >= 0 and w < len(self.graph.nodes_dict)
        if not self.has_path(w):
            return "Not such a path"
        path_list = [w]
        current_node = self.graph.nodes_dict[w]
        while current_node != self.start_node:
            current_node = current_node.get_pred()
            path_list.append(current_node.get_id())
        path_list.reverse()
        return path_list

    def show_path(self, w):
        assert w >= 0 and w < len(self.graph.nodes_dict)
        path_list = self.path(w)
        print(path_list)

if __name__ == "__main__":
    g = SparseGraph(directed=True)
    build_graph_from_file(g, "testG1.txt")
    s = ShortestPath(g, 5)
    s.show_path(6)
    s.show_path(7)