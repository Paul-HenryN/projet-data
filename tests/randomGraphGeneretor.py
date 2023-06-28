import numpy as np
import networkx as nx
import random
import matplotlib.pyplot as plt

def graph_generetor():
    n = int(input("Entrez le nombre de villes : "))
    p = float(input("Entrez la probabilité d'existence d'une route : "))

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

    # Affichage de la matrice d'adjacence et du graphe
    print("Matrice d'adjacence :")
    print(adj_matrix)
    nx.draw(G, with_labels=True)
    plt.show()

    # Génération du sous-graphe
    subgraph_nodes = random.sample(sorted(G.nodes()), k=random.randint(1, len(G))) #génère une liste de nœuds aléatoires à partir du graphe G.
    subgraph = G.subgraph(subgraph_nodes)

    # Extraction de la matrice d'adjacence du sous-graphe à partir de la matrice d'adjacence du graphe général
    subgraph_adj_matrix = adj_matrix[np.ix_(subgraph_nodes, subgraph_nodes)]

    # Affichage du sous-graphe et de sa matrice d'adjacence
    print("Sous-graphe :")
    nx.draw(subgraph, with_labels=True)
    plt.show()

    print("Matrice d'adjacence du sous-graphe :")
    print(subgraph_adj_matrix)


graph_generetor()