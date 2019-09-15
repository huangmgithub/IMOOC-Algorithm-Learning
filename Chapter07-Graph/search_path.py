from Chapter07_Graph.generate_graph import build_graph_from_file
from Chapter07_Graph.sparse_graph import SparseGraph

class SearchPath:
    def __init__(self, graph, start_node):
        self.graph = graph
        self.start_node = graph.nodes_dict[start_node]
        self.path_list = []
        self.calc()

    def calc(self):
        """
        dfs前处理
        :return:
        """
        for node in self.graph:
            node.set_visited(False)
            node.set_pred(None) # 前继节点
        self._dfs(self.start_node)

    def _dfs(self, start_node):
        """
        dfs
        :param start_node:
        :return:
        """
        start_node.set_visited(True)
        for next_node in start_node.get_connectedTo():
            if not next_node.is_visited():
                next_node.set_pred(start_node)
                self._dfs(next_node)

    def has_path(self, w):
        """
        起始节点与w是否存在一条路径
        :param w: id
        :return:
        """
        return self.graph.nodes_dict[w].is_visited()

    def path(self, w):
        """
        获得开始节点到w节点的路径
        :param w:
        :return:
        """
        if not self.has_path(w):
            return "Not such a path"
        self.path_list = [w]
        current_node = self.graph.nodes_dict[w]
        while current_node != self.start_node:
            current_node = current_node.get_pred()
            self.path_list.append(current_node.get_id)
        self.path_list.reverse()
        return self.path_list

    def show_path(self, w):
        self.path_list = []
        self.path(w)
        if self.path_list:
            print(self.path_list)

if __name__ == "__main__":
    g = SparseGraph(directed=True)
    build_graph_from_file(g, "testG1.txt")
    s = SearchPath(g, 5)
    s.show_path(6)
    s.show_path(7)




