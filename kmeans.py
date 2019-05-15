import numpy as np, matplotlib.pyplot as plt
from operator import itemgetter
from math import sqrt
from copy import deepcopy
from random import random, randint, uniform

# k means
class k_means:
    def __init__(self, k = 4, tolerance = 0.001, iterations = 100):
        self.k = k
        self.tolerance = tolerance
        self.iterations = iterations

# kd tree nodes
class kd_node:
    def __init__(self, data, left=None, right=None, axis=None, dimension=None):
        self.data = data
        self.left = left
        self.right = right
        self.axis = axis
        self.dimension = dimension

        self.count = 1
        self.wgtCenter = data
        self.candidates = []

    def is_leaf(self):
        return self.count == 1

def kd_tree(point_list=None, dimensions=None, depth=0):
    if dimensions is None:
        dimensions = len(point_list[0])
    if not point_list:
        return None

    if dimensions != 2:
        axis = depth % dimensions

        point_list.sort(key=itemgetter(axis))
        mid = len(point_list)//2

        coordinate = point_list[mid]
        if len(point_list) > 1:
            left = kd_tree(point_list[:mid], dimensions, depth + 1)
            right = kd_tree(point_list[mid+1:], dimensions, depth + 1)
            return kd_node(coordinate, left, right, axis, dimensions)
        else:
            return kd_node(coordinate, None, None, axis, dimensions)
    else:
        dt = np.dtype('float')
        divided = []
        for i in range(4):
            start = i * (len(point_list) // 4)
            end = len(point_list) // 4 * (i + 1)
            number = random()

            center = np.array([number, number])

            division = np.array(point_list[start:end], dtype=dt)

            divided.append(division)
        divided = np.array(divided, dtype=dt)
        data = np.concatenate(divided, axis=0)
        clusters_k = 4
        n = data.shape[0]
        c = data.shape[1]

        mean = np.mean(data, axis=0)
        std = np.std(data, axis=0)
        medoids = np.random.randn(clusters_k, c) * std + mean

        medoids_old = np.zeros(medoids.shape)
        medoids_new = deepcopy(medoids)
        clusters = np.zeros(n)
        distances = np.zeros((n, clusters_k))

        e_distance = np.linalg.norm(medoids_new - medoids_old)
        while e_distance != 0:
            for i in range(clusters_k):
                distances[:, i] = np.linalg.norm(data - medoids[i], axis=1)
            clusters = np.argmin(distances, axis=1)

            medoids_old = deepcopy(medoids_new)
            for i in range(clusters_k):
                medoids_new[i] = np.mean(data[clusters == i], axis=0)
            e_distance = np.linalg.norm(medoids_new - medoids_old)
        for i in range(n):
            plt.scatter(data[i, 0], data[i, 1], s=6, c='blue')
        plt.scatter(medoids_new[:, 0], medoids_new[:, 1], marker='+', c="red", s=100)

def euclidean_distance(first, second):
    distance = 0
    for i in range(len(first)):
        distance += pow((first[i] - second[i]),2)
    return sqrt(distance)

def build_kd_graph(current_node, graph, posX, posY, width):
    w = width // 2

    if current_node.left and current_node.left.data is not None:
        graph.add_node(current_node.left, pos=(posX - w, posY - 10), label=current_node.left.data)
        graph.add_edge(current_node, current_node.left)
        build_kd_graph(current_node.left, graph, posX - w, posY - 10, w)

    if current_node.right and current_node.right.data is not None:
        graph.add_node(current_node.right, pos=(posX + w, posY - 10), label=current_node.right.data)
        graph.add_edge(current_node, current_node.right)
        build_kd_graph(current_node.right, graph, posX + w, posY - 10, w)

def show_graph(nodeTree, dimension):
    import networkx as nx
    import matplotlib.pyplot as plt

    if(dimension != 2):
        G = nx.Graph()
        G.add_node(nodeTree, pos=(0, 0), label=nodeTree.data)


        build_kd_graph(nodeTree, G, 0, 0, 100)
        # positions  = nx.drawing.nx_agraph.graphviz_layout(G, prog="dot")
        colors = []
        for node in G:
            colors.append('pink')
        nx.draw(G, pos=nx.get_node_attributes(G, 'pos'),
                labels=nx.get_node_attributes(G, 'label'),
                with_labels=True, node_color = colors,
                font_size=7, font_color='black'
                )

    plt.show()

def read_file(path):
    file = open(path, 'r').read().splitlines()
    coordinates = []
    n, k = [int(i) for i in file[0].split(" ")]
    for line in file[1:]:
        tuple = [float(x) for x in line.strip("()").split(",")]
        coordinates.append(tuple)
    return n, k, coordinates



