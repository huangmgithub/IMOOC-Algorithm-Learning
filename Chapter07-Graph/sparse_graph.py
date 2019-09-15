from collections import defaultdict
import random
import sys

class Node:
    def __init__(self, key):
        self._id = key
        self._connectedTo = {} # key是node对象，value是两个对象之间边的权重
        self._ccid = 0 # 该节点所属的连通分量的id
        self._dist = sys.maxsize
        self._pred = None # 该节点的前继节点
        self._is_visited = False # 是否访问过

    def get_id(self):
        """
        获得节点id
        :return:
        """
        return self._id

    def get_ccid(self):
        """
        获得所属连通分量id
        :return:
        """
        return self._ccid

    def set_ccid(self, ccid):
        """
        设置所属连通分量id
        :param ccid:
        :return:
        """
        self._ccid = ccid

    def get_pred(self):
        """获得前继节点"""
        return self._pred

    def set_pred(self, pred):
        """
        设置前继节点
        :param pred:
        :return:
        """
        self._pred = pred

    def is_visited(self):
        """是否已访问"""
        return self._is_visited

    def set_visited(self, bool):
        """
        设置是否访问过
        :param bool:
        :return:
        """
        self._is_visited = bool

    def get_distance(self):
        """
        获得距离
        :return:
        """
        return self._dist

    def set_distance(self, dist):
        """
        设置距离
        :param dist:
        :return:
        """
        self._dist = dist

    def add_neighbor(self, node, weight=0):
        """
        增加邻节点
        :param node:
        :param weight:
        :return:
        """
        self._connectedTo[node] = weight

    def get_connectedTo(self):
        """
        获得连接节点
        :return:
        """
        return self._connectedTo.keys()

    def get_connectedTo_id(self):
        """
        获得连接节点的id
        :return:
        """
        id_list = []
        for i in self._connectedTo.keys():
            id_list.append(i.get_id())
        return sorted(id_list)

    def get_connected_id_and_weight(self):
        """
        获得连接节点的权重和id
        :return:
        """
        id_list = []
        for k in self._connectedTo.keys():
            id_list.append(k.get_id())
        weight_list = list(self._connectedTo.values())
        return {id:weight for id, weight in zip(id_list,weight_list)}

    def __str__(self):
        return str(self._id) + 'connectedTo' + str([x.id for x in self._connectedTo])

class SparseGraph:
    def __init__(self, directed=False, weighted=False):
        self.nodes_dict = {} # key是node的id， value是node
        self.num_nodes = 0 # 节点总数量
        self._directed = directed # 是否有向
        self._weight = weighted # 是否有权
        self._ccount = 0 # 连通分量的数量

    def add_node(self, key):
        """增加节点"""
        new_node = Node(key)
        self.nodes_dict[key] = new_node
        self.num_nodes += 1
        return new_node

    def get_node(self, key):
        """
        获得节点
        :param key:
        :return:
        """
        if key in self.nodes_dict:
            return self.nodes_dict[key]
        else:
            return None

    def is_contains(self, key):
        """
        是否包含指定节点
        :param key:
        :return:
        """
        return key in self.nodes_dict

    def add_edge(self, v, w, weight=0):
        """
        增加边
        :param v: id
        :param w: id
        :param weight:
        :return:
        """
        if v not in self.nodes_dict:
            self.add_node(v)
        if w not in self.nodes_dict:
            self.add_node(w)

        self.nodes_dict[v].add_neighbor(self.nodes_dict[w],weight)
        if not self._directed:
            self.nodes_dict[w].add_neighbor(self.nodes_dict[v], weight)

    def has_edge(self, v, w):
        """
        判断两节点是否连接
        :param v: id
        :param w: id
        :return:
        """
        if v not in self.nodes_dict or w not in self.nodes_dict:
            return False
        if w in self.nodes_dict[v].get_connectedTo_id() or v in self.nodes_dict[w].get_connectedTo_id():
            return True

    def get_all_nodes(self):
        """
        获得所有节点
        :return:
        """
        return list(self.nodes_dict.keys())

    def get_num_nodes(self):
        """
        获得节点总数量
        :return:
        """
        return self.num_nodes

    def is_connected(self, v, w):
        """
        是否在同一连通分量
        :param v:
        :param w:
        :return:
        """
        return self.nodes_dict[v].get_ccid() == self.nodes_dict[w].get_ccid()

    def get_ccount(self):
        """
        获得连通分量数量
        :return:
        """
        return self._ccount

    def set_ccount(self, ccount):
        """
        设置连通分量数量
        :param ccount:
        :return:
        """
        self._ccount = ccount

    def __iter__(self):
        return iter(self.nodes_dict.values())


if __name__ == "__main__":

    pass


    
    