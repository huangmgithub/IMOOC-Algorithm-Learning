from Chapter07_Graph.sparse_graph import SparseGraph
from Chapter07_Graph.generate_graph import build_graph_from_file

class Component:
    def __init__(self, graph):
        self._graph = graph
        self._result = 0
        self.calc()

    def calc(self):
        """
        dfs前处理
        :return:
        """
        for node in self._graph:
            node.set_visited(False)

        for node in self._graph:
            if not node.is_visited():
                self._dfs(node, self._graph.get_ccount())
                self._graph.set_ccount(self._graph.get_ccount() + 1)
                self._result += 1

    def _dfs(self, node, ccount):
        """
        dfs
        :param node:
        :param ccount:
        :return:
        """
        node.set_ccid(ccount)
        node.set_visited(True)
        for next_node in node.get_connectedTo():
            if not next_node.is_visited():
                self._dfs(next_node, ccount)


    def get_result(self):
        """
        获得连通分量结果
        :return:
        """
        return self._result

if __name__ == "__main__":
    g = SparseGraph()
    build_graph_from_file(g, "testG1.txt")
    component = Component(g)
    print(component.get_result())

