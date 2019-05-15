import random
from operator import itemgetter
from math import sqrt

class kd_node:
    def __init__(self, data, left=None, right=None, axis=None, dimension=None):
        # inicializacion parametros constructor
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

def euclidean_distance(first, second):
    distance = 0
    for i in range(len(first)):
        distance += pow((first[i] - second[i]),2)
    return sqrt(distance)

def build_graph(current_node, graph, posx, posy, width):
    w = width / 2

    if current_node.left and current_node.left.data is not None:
        graph.add_node(current_node.left, pos=(posx - w, posy - 10),
                       label=current_node.left.data)
        graph.add_edge(current_node, current_node.left)
        build_graph(current_node.left, graph, posx - w, posy - 10, w)

    if current_node.right and current_node.right.data is not None:
        graph.add_node(current_node.right, pos=(posx + w, posy - 10),
                       label=current_node.right.data)  # current_node.right.data
        graph.add_edge(current_node, current_node.right)
        build_graph(current_node.right, graph, posx + w, posy - 10, w)



def show_graph(nodeTree):
    import networkx as nx
    import matplotlib.pyplot as plt

    G = nx.Graph()
    G.add_node(nodeTree, pos=(0, 0), label=nodeTree.data)

    build_graph(nodeTree, G, 0, 0, 100)
    # positions  = nx.drawing.nx_agraph.graphviz_layout(G, prog="dot")
    colors = []
    for node in G:
        colors.append('pink')

    print("Drawing...")
    nx.draw(G, pos=nx.get_node_attributes(G, 'pos'),
            labels=nx.get_node_attributes(G, 'label'),
            with_labels=True, node_color = colors,
            font_size=7, font_color='black'
            )
    print("...done drawing")
    print("Showing...")
    plt.show()
    print("...done showing")


