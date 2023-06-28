import numpy as np
import networkx as nx
import random
import matplotlib.pyplot as plt


def generate_graph(n, p):
    # Génération de la matrice d'adjacence aléatoire pondérée
    adj_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(i + 1, n):
            if random.random() < p:
                weight = random.randint(1, 10)
                adj_matrix[i][j] = weight
                adj_matrix[j][i] = weight

    # Création d'un graphe vide
    G = nx.Graph()

    # Ajout des arêtes avec les poids à partir de la matrice d'adjacence
    for i in range(n):
        for j in range(i + 1, n):
            if adj_matrix[i][j] != 0:
                G.add_edge(i, j, weight=adj_matrix[i][j])

    # Génération du sous-graphe
    subgraph_nodes = random.sample(
        sorted(G.nodes()), k=random.randint(2, len(G))
    )  # génère une liste de nœuds aléatoires à partir du graphe G.
    subgraph = G.subgraph(subgraph_nodes)

    # Extraction de la matrice d'adjacence du sous-graphe à partir de la matrice d'adjacence du graphe général
    subgraph_adj_matrix = adj_matrix[np.ix_(subgraph_nodes, subgraph_nodes)]

    print("Matrice d'adjacence du sous-graphe :")
    print(subgraph_adj_matrix)

    return G, subgraph
