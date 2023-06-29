import numpy as np
import networkx as nx
import random
import matplotlib.pyplot as plt

def graph_generetor():
    n = int(input("Enter the number of cities : "))
    p = float(input("Enter the probability of existence of a route : "))

    # Generation of the weighted random adjacency matrix
    adj_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(i + 1, n):
            if random.random() < p:
                weight = random.randint(1, 10)
                adj_matrix[i][j] = weight
                adj_matrix[j][i] = weight

    #Creating an empty graph
    G = nx.Graph()

    # Adding edges with weights from the adjacency matrix
    for i in range(n):
        for j in range(i + 1, n):
            if adj_matrix[i][j] != 0:
                G.add_edge(i, j, weight=adj_matrix[i][j])

    # Displaying the adjacency matrix and graph
    print("adjacency matrix :")
    print(adj_matrix)
    nx.draw(G, with_labels=True)
    plt.show()

    # Subgraph generation
    subgraph_nodes = random.sample(sorted(G.nodes()), k=random.randint(1, len(G))) #generates a list of random nodes from the graph G.
    subgraph = G.subgraph(subgraph_nodes)

    # Extracting the sub-graph adjacency matrix from the general graph adjacency matrix
    subgraph_adj_matrix = adj_matrix[np.ix_(subgraph_nodes, subgraph_nodes)]

    # Displaying the subgraph and its adjacency matrix
    print("subgraph:")
    nx.draw(subgraph, with_labels=True)
    plt.show()

    print("Subgraph adjacency matrix :")
    print(subgraph_adj_matrix)


graph_generetor()