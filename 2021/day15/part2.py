#!/usr/bin/env python3

import networkx as nx
import numpy as np

chitons = np.genfromtxt('input.ex', delimiter=1, dtype=int)


def graphit(chitons):
    graph = nx.DiGraph()
    for x in range(len(chitons)):
        for y in range(len(chitons)):
            if x < len(chitons) - 1:
                graph.add_edge((x, y), (x + 1, y), weight=chitons[x + 1][y])
                graph.add_edge((x + 1, y), (x, y), weight=chitons[x][y])

            if y < len(chitons) - 1:
                graph.add_edge((x, y), (x, y + 1), weight=chitons[x][y + 1])
                graph.add_edge((x, y + 1), (x, y), weight=chitons[x][y])
    return graph


def get_path_sum(chitons, graph):
    path_sum = -chitons[0][0]
    for point in nx.shortest_path(graph, source=(0, 0), target=(len(chitons) - 1, len(chitons) - 1), weight='weight'):
        path_sum += chitons[point]
    return path_sum


extension = chitons.copy()

for i in range(4):
    extension += 1
    extension[np.where(extension == 10)] = 1
    chitons = np.concatenate((chitons, extension), axis=1)

extension = chitons.copy()

for i in range(4):
    extension += 1
    extension[np.where(extension == 10)] = 1
    chitons = np.concatenate((chitons, extension), axis=0)

chit_graph = graphit(chitons)

print(get_path_sum(chitons, chit_graph))
