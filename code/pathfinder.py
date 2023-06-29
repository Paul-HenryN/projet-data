import heapq
import numpy as np


def dijkstra(adj_matrix, start):
    """
    Computes the shortest paths from a given start node to all other nodes in a graph represented by an adjacency matrix
    using Dijkstra's algorithm.

    Arguments:
    adj_matrix -- a numpy array representing the adjacency matrix of the graph
    start -- the starting node

    Returns:
    A dictionary containing the shortest distance to each node from the start node, and the path to each node as a list of nodes.
    """
    num_nodes = len(adj_matrix)
    distances = {node: float("inf") for node in range(num_nodes)}
    distances[start] = 0
    queue = [(0, start)]
    path = {start: []}

    while queue:
        (current_distance, current_node) = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor in range(num_nodes):
            weight = adj_matrix[current_node][neighbor]

            if weight > 0:
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    path[neighbor] = path[current_node] + [current_node]
                    heapq.heappush(queue, (distance, neighbor))

    for node in range(num_nodes):
        path[node] = path[node] + [node]

    return distances, path


def shortest_distance(adj_matrix, nodeA, nodeB):
    distances, path = dijkstra(adj_matrix, nodeA)
    return distances[nodeB]


def shortest_path(adj_matrix, nodeA, nodeB):
    distances, path = dijkstra(adj_matrix, nodeA)
    return path[nodeB]
