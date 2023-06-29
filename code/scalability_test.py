import instance_generator as ig
import networkx as nx
import pathfinder as pf
import time
import genetic_algorithm as ga

POPULATION_SIZE = 100
N_GENERATIONS = 100
MUTATION_RATE = 0.01


def solve(graph, subgraphs):
    graph_matrix = nx.adjacency_matrix(graph).todense().tolist()
    execution_time = 0

    k = 1

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


# 10 cities and 3 vehicles
graph1, subgraphs1 = ig.generate_instance(10, 0.4, 7, 9, 3)

# 80 cities and 10 vehicles
graph2, subgraphs2 = ig.generate_instance(80, 0.5, 40, 48, 10)

# 300 cities and 15 vehicles
graph3, subgraphs3 = ig.generate_instance(300, 0.4, 150, 250, 15)

print("---- 10 cities and 3 vehicles -----")
solve(graph1, subgraphs1)
print("\n---- 80 cities and 10 vehicles -----")
solve(graph2, subgraphs2)
print("\n---- 300 cities and 15 vehicles -----")
solve(graph3, subgraphs3)
