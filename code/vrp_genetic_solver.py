import networkx as nx
import matplotlib.pyplot as plt
import random

# Global variables
global matrix
global n_bits
global n_pop

random.seed(a=3)


# Calculates the cost of a candidate solution
def cost(candidate_solution):
    matrix_size = len(matrix)
    cost = 0
    row = 0

    for row in range(matrix_size):
        for col in range(matrix_size):
            cost += candidate_solution[row * matrix_size + col] * matrix[row][col]

    return cost


graph = nx.complete_graph(3)
nx.set_edge_attributes(
    graph, {e: {"weight": random.randint(1, 10)} for e in graph.edges}
)
matrix = nx.adjacency_matrix(graph).todense()

n_bits = len(matrix) ** 2
n_pop = 10
n_iter = 10

# initial population of random bitstring
initial_population = [
    [random.randint(0, 1) for i in range(n_bits)] for j in range(n_pop)
]

print(matrix)
print(initial_population[1])
print(cost(initial_population[1]))

# iterate over generations
for gen in range(n_iter):
    pass
