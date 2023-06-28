import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import random

graph = nx.complete_graph(10)
nx.set_edge_attributes(
    graph, {e: {"weight": random.randint(1, 10)} for e in graph.edges}
)

matrix = nx.adjacency_matrix(graph).todense()

# Définition du problème
distances = matrix
n = len(distances)  # Nombre de villes


def evaluate_tour(tour):
    total_distance = 0
    for i in range(n - 1):
        total_distance += distances[tour[i]][tour[i + 1]]
    total_distance += distances[tour[-1]][tour[0]]  # Retour à la première ville
    return total_distance


# Algorithme génétique
def initialize_population(population_size):
    population = []
    for _ in range(population_size):
        individual = list(range(n))
        random.shuffle(individual)  # Permute aléatoirement l'ordre
        population.append(individual)
    return population


def select_parents(population):
    fitness_values = []
    for individual in population:
        fitness_values.append(
            1 / evaluate_tour(individual)
        )  # Calcul de l'inverse de la distance parcourue
    sum_fitness = sum(fitness_values)
    probabilities = [fitness / sum_fitness for fitness in fitness_values]
    parents = random.choices(
        population, probabilities, k=2
    )  # Sélection de deux parents
    return parents


def crossover(parents):
    parent1, parent2 = parents
    child = [None] * n
    start, end = sorted(
        random.sample(range(n), 2)
    )  # Choix de deux points de coupure pour le croisement
    child[start:end] = parent1[start:end]
    remaining_cities = [city for city in parent2 if city not in child[start:end]]
    index = 0
    for i in range(n):
        if child[i] is None:
            child[i] = remaining_cities[index]
            index += 1
    return child


def mutate(individual, mutation_rate):
    for i in range(n):
        if random.random() < mutation_rate:  # Mutation avec une probabilité donnée
            j = random.randint(0, n - 1)
            individual[i], individual[j] = (
                individual[j],
                individual[i],
            )  # Permutation de deux villes
    return individual


def genetic_algorithm(population_size, generations, mutation_rate):
    population = initialize_population(population_size)
    best_individual = None
    best_fitness = float("inf")

    for _ in range(generations):
        new_population = []

        while len(new_population) < population_size:
            parents = select_parents(population)
            child = crossover(parents)
            child = mutate(child, mutation_rate)
            new_population.append(child)

        population = new_population

        for individual in population:
            fitness = evaluate_tour(individual)
            if fitness < best_fitness:
                best_fitness = fitness
                best_individual = individual

    return best_individual, best_fitness


# Exemple d'utilisation
population_size = 100
generations = 100
mutation_rate = 0.01

best_solution, best_distance = genetic_algorithm(
    population_size, generations, mutation_rate
)


print("Meilleure solution trouvé :", best_solution)
print("Distance parcourue :", best_distance)

nx.draw(graph, with_labels=True)
print(matrix)
plt.show()
