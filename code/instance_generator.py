import numpy as np
import networkx as nx
import random
import matplotlib.pyplot as plt


def generate_adj_matrix(n, p):
    adj_matrix = np.zeros((n, n))

    for i in range(n):
        for j in range(i + 1, n):
            if random.random() < p:
                weight = random.randint(1, 10)
                adj_matrix[i][j] = weight
                adj_matrix[j][i] = weight

    return adj_matrix


def generate_instance(n, p, min, max, n_vehicles):
    # Génération de la matrice d'adjacence aléatoire pondérée
    adj_matrix = np.zeros((n, n))
    is_valid = False

    while not is_valid:
        adj_matrix = generate_adj_matrix(n, p)
        is_valid = True

        for i in range(n):
            if sum(adj_matrix[i]) == 0:
                is_valid = False
                break

    # Création d'un graphe vide
    G = nx.from_numpy_array(adj_matrix)

    subgraphs = []

    for _ in range(n_vehicles):
        # Génération du sous-graphe
        subgraph_nodes = random.sample(
            sorted(G.nodes()), k=random.randint(min, max)
        )  # génère une liste de nœuds aléatoires à partir du graphe G.
        subgraph = G.subgraph(subgraph_nodes)
        subgraphs.append(subgraph)

    return G, subgraphs
