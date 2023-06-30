import networkx as nx
import matplotlib.pyplot as plt
import genetic_algorithm as ga
import instance_generator as ig
import pathfinder as pf
import time

N_CITIES = int(input("Enter the number of cities to consider: "))
N_VEHICLES = int(input("Enter the number of vehicles to consider: "))
POPULATION_SIZE = int(input("Enter the population size: "))
N_GENERATIONS = int(input("Enter the number of generations: "))
MUTATION_RATE = 0.01

# Generate a test graph and a random subgraph
graph, subgraphs = ig.generate_instance(N_CITIES, 0.4, 5, 8, N_VEHICLES)
graph_matrix = nx.adjacency_matrix(graph).todense().tolist()

k = 1
pos = nx.spring_layout(graph)
execution_time = 0
total_distance = 0
total_cities = 0

for subgraph in subgraphs:
    start_time = time.time()

    complete_subgraph = nx.transitive_closure(subgraph)

    subgraph_matrix = nx.adjacency_matrix(subgraph).todense().tolist()

    nx.set_edge_attributes(
        complete_subgraph,
        {
            e: {"weight": pf.shortest_distance(graph_matrix, e[0], e[1])}
            for e in complete_subgraph.edges
        },
    )

    complete_subgraph_matrix = nx.adjacency_matrix(complete_subgraph).todense().tolist()

    best_tour, best_distance = ga.genetic_algorithm(
        complete_subgraph_matrix, POPULATION_SIZE, N_GENERATIONS, MUTATION_RATE
    )

    # Indexed solution
    node_list = sorted(list(complete_subgraph))
    indexed_tour = [node_list[idx] for idx in best_tour]
    indexed_tour.append(indexed_tour[0])

    final_tour = indexed_tour.copy()

    # Replace inexistant edges in the tour with the shortest path
    for i in range(len(final_tour) - 1):
        if graph_matrix[final_tour[i]][final_tour[i + 1]] == 0:
            final_tour[i : i + 2] = pf.shortest_path(
                graph_matrix, final_tour[i], final_tour[i + 1]
            )

    execution_time += time.time() - start_time
    total_distance += best_distance
    total_cities += len(subgraph)

    print(
        "vehicle",
        k,
        ":",
        final_tour,
        "(",
        best_distance,
        ") --",
        execution_time,
        "seconds elapsed",
    )

    # Draw
    # Draw base graph
    colors = []

    graph_edge_labels = dict(
        [
            (
                (
                    u,
                    v,
                ),
                d["weight"],
            )
            for u, v, d in graph.edges(data=True)
        ]
    )

    for node in graph:
        if node in subgraph:
            colors.append("green")
        else:
            colors.append("blue")

    plt.figure(1)
    nx.draw(graph, pos, node_color=colors, with_labels=True)
    nx.draw_networkx_edge_labels(
        graph,
        pos,
        edge_labels=graph_edge_labels,
    )

    # Draw subgraph
    subgraph_edge_labels = dict(
        [
            (
                (
                    u,
                    v,
                ),
                d["weight"],
            )
            for u, v, d in subgraph.edges(data=True)
        ]
    )

    plt.figure(2)
    nx.draw(
        subgraph,
        pos,
        node_color=["green"] * len(subgraph),
        with_labels=True,
    )
    nx.draw_networkx_edge_labels(
        subgraph,
        pos,
        edge_labels=subgraph_edge_labels,
    )

    plt.show()

    k += 1
