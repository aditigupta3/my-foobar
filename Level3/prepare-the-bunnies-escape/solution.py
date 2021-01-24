from collections import defaultdict
from copy import deepcopy


def solution(mat):
    """
    Function to get the length of the shortest path from top left to bottom right of 'mat' where we are allowed to
    remove 1 wall.
    Modelled this as a graph. The shortest path is determined. Then the shortest path is determined on removing 1
    wall at a time.
    :param mat:
    :return: shortest distance
    """
    g = create_graph(mat)
    start, end = 0, len(mat) * len(mat[0]) - 1
    shortest = g.find_distance(start, end)
    for j in range(len(mat)):
        for i in range(len(mat[0])):
            if mat[j][i] == 1:
                g_new = modify_graph(g, mat, i, j)
                distance = g_new.find_distance(start, end)
                if distance < shortest:
                    shortest = distance
    return shortest


def modify_graph(g, mat, i, j):
    """
    Function to modify graph
    :param g: given graph
    :param mat: matrix for the given graph
    :param i: column number
    :param j: row number
    :return: new graph
    """
    g_new = deepcopy(g)
    node_id = j * len(mat[0]) + i
    g_new.add_node(node_id)
    if i > 0:
        if mat[j][i - 1] == 0:
            g_new.add_edge(node_id, node_id - 1)
    if i < len(mat[0]) - 1:
        if mat[j][i + 1] == 0:
            g_new.add_edge(node_id, node_id + 1)
    if j > 0:
        if mat[j - 1][i] == 0:
            g_new.add_edge(node_id, node_id - len(mat[0]))
    if j < len(mat) - 1:
        if mat[j + 1][i] == 0:
            g_new.add_edge(node_id, node_id + len(mat[0]))
    return g_new


def create_graph(mat):
    """
    Function to convert 'mat' into a graph.
    :param mat:
    :return: the graph
    """
    g = Graph()
    for j in range(len(mat)):
        for i in range(len(mat[0])):
            node_id = j * len(mat[0]) + i
            if mat[j][i] == 0:
                g.add_node(node_id)
                if j < len(mat) - 1:
                    if mat[j + 1][i] == 0:
                        g.add_edge(node_id, node_id + len(mat[0]))
                if i < len(mat[0]) - 1:
                    if mat[j][i + 1] == 0:
                        g.add_edge(node_id, node_id + 1)
    return g


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_node(self, node):
        """
        Function to add a node to the graph
        :param node:
        :return:
        """
        if node not in self.graph.keys():
            self.graph[node] = list()

    def add_edge(self, node1, node2):
        """
        Function to add an edge between node1 and node2
        :param node1:
        :param node2:
        :return:
        """
        self.graph[node1].append(node2)
        self.graph[node2].append(node1)

    def find_distance(self, start, end):
        """
        Function to find the shortest distance between start and end using BFS.
        :param start:
        :param end:
        :return: shortest distance
        """
        visited = {k: False for k in self.graph.keys()}
        distance = {k: 1000 for k in self.graph.keys()}
        queue = list()
        queue.append(start)
        visited[start] = True
        distance[start] = 1
        while queue:
            s = queue.pop(0)
            dis_s = distance[s]
            for i in self.graph[s]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
                    distance[i] = dis_s + 1
                    if end == i:
                        break
        return distance[end]