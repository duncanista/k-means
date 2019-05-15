from kmeans import *

dimension, iterations, coordinates = read_file("input.txt")
tree = kd_tree(coordinates)
show_graph(tree, dimension)