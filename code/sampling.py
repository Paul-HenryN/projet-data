import networkx as nx
import matplotlib.pyplot as plt
import genetic_algorithm as ga
import instance_generator as ig
import pathfinder as pf
import time
import random
import create_excel_file as xls
import math

n_sample = int(input("How many records ? "))
MUTATION_RATE = 0.01
sample_data = []


for i in range(n_sample):
    N_CITIES = random.randint(5, 20)
    N_VEHICLES = random.randint(1, 10)
    POPULATION_SIZE = random.randint(30, 100)
    N_GENERATIONS = random.randint(30, 100)

    min_subgraph_size = int(N_CITIES / 2)
    max_subgraph_size = int(N_CITIES - 1)

    # Generate a test graph and a random subgraph
    graph, subgraphs = ig.generate_instance(
        N_CITIES, 0.7, min_subgraph_size, max_subgraph_size, N_VEHICLES
    )

    pos = nx.spring_layout(graph)

    graph_matrix = nx.adjacency_matrix(graph).todense().tolist()

    k = 1
    pos = nx.spring_layout(graph)
    execution_time = 0
    total_distance = 0
    total_cities = 0

    print(f"--- Record {i + 1} ----")

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

        complete_subgraph_matrix = (
            nx.adjacency_matrix(complete_subgraph).todense().tolist()
        )

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

        k += 1

    sample_data.append(
        [
            N_VEHICLES,
            N_GENERATIONS,
            total_cities,
            total_distance,
            round(execution_time, 2),
        ]
    )

xls.create_excel_file(sample_data, "sample.xlsx")
