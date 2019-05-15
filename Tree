import random
from operator import itemgetter


class KdNode:
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


def kdTree(point_list=None, dimensions=None, depth=0):
    if dimensions is None:
        dimensions = len(point_list[0])

    if not point_list:
        return None

    axis = depth % dimensions

    point_list.sort(key=itemgetter(axis))
    mid = len(point_list)//2


    coordinate = point_list[mid]
    if len(point_list) > 1:
        left = kdTree(point_list[:mid], dimensions, depth + 1)
        right = kdTree(point_list[mid+1:], dimensions, depth + 1)
        return KdNode(coordinate, left, right, axis, dimensions)
    else:
        return KdNode(coordinate, None, None, axis, dimensions)

def buildNetworkxGraph(current_node, graph, posx, posy, width):
    w = width / 2

    if current_node.left and current_node.left.data is not None:
        graph.add_node(current_node.left, pos=(posx - w, posy - 5),
                       label=getOffsettedLabel(current_node.left))  # "b'$"+str(current_node.left.data)+"$'"
        graph.add_edge(current_node, current_node.left)
        buildNetworkxGraph(current_node.left, graph, posx - w, posy - 5, w)

    if current_node.right and current_node.right.data is not None:
        graph.add_node(current_node.right, pos=(posx + w, posy - 5),
                       label=getOffsettedLabel(current_node.right))  # current_node.right.data
        graph.add_edge(current_node, current_node.right)
        buildNetworkxGraph(current_node.right, graph, posx + w, posy - 5, w)


def getOffsettedLabel(k_d_node):
    if k_d_node.axis == 0:
        return "         " + str(k_d_node.data)
    elif k_d_node.axis == 1:
        return str(k_d_node.data)
    elif k_d_node.axis == 2:
        return str(k_d_node.data) + "         "


def ShowNetworkxGraph(nodeTree):
    import networkx as nx
    import matplotlib.pyplot as plt

    G = nx.Graph()
    G.add_node(nodeTree, pos=(0, 0), label=getOffsettedLabel(nodeTree))

    buildNetworkxGraph(nodeTree, G, 0, 0, 10)
    # positions  = nx.drawing.nx_agraph.graphviz_layout(G, prog="dot")


    print("Drawing...")
    nx.draw(G, pos=nx.get_node_attributes(G, 'pos'), labels=nx.get_node_attributes(G, 'label'), with_labels=True)
    print("...done drawing")
    print("Showing...")
    plt.show()
    print("...done showing")




def main():
    p1 = (0.8, 4, 1)
    p2 = (3, 0.5, 2)
    p3 = (1, 2, 7)
    p4 = (9, 3, 4)
    p5 = (5, 1, 9)
    p6 = (3, 6, 9)
    p7 = (7, 5, 1)
    p8 = (2, 2, 7)
    p9 = (1, 2, 8)

    tree1 = kdTree([p1, p2, p3, p4, p5, p6, p7, p8, p9])
    ShowNetworkxGraph(tree1)


main()
