import random


# Calculate the cost of a tour
def cost(matrix, tour):
    n = len(matrix)

    total_distance = 0
    for i in range(n - 1):
        total_distance += matrix[tour[i]][tour[i + 1]]
    total_distance += matrix[tour[-1]][tour[0]]  # Retour à la première ville
    return total_distance


# Initialize a random population of solutions
def initialize_population(matrix, population_size):
    population = []
    for _ in range(population_size):
        individual = list(range(len(matrix)))
        random.shuffle(individual)

        while cost(matrix, individual) == 0:
            random.shuffle(individual)

        population.append(individual)
    return population


# Selection
def selection(matrix, population):
    fitness_values = []
    for individual in population:
        fitness_values.append(1 / cost(matrix, individual))
    sum_fitness = sum(fitness_values)
    probabilities = [fitness / sum_fitness for fitness in fitness_values]
    parents = random.choices(population, probabilities, k=2)
    return parents


def crossover(matrix, parents):
    n = len(matrix)
    parent1, parent2 = parents
    child = [None] * n
    start, end = sorted(random.sample(range(n), 2))
    child[start:end] = parent1[start:end]
    remaining_cities = [city for city in parent2 if city not in child[start:end]]
    index = 0
    for i in range(n):
        if child[i] is None:
            child[i] = remaining_cities[index]
            index += 1
    return child


def mutate(matrix, individual, mutation_rate):
    n = len(matrix)
    for i in range(n):
        if random.random() < mutation_rate:
            j = random.randint(0, n - 1)
            individual[i], individual[j] = (
                individual[j],
                individual[i],
            )
    return individual


def genetic_algorithm(matrix, population_size, generations, mutation_rate):
    population = initialize_population(matrix, population_size)
    best_individual = None
    best_fitness = float("inf")

    for _ in range(generations):
        new_population = []

        while len(new_population) < population_size:
            parents = selection(matrix, population)
            child = crossover(matrix, parents)
            child = mutate(matrix, child, mutation_rate)
            new_population.append(child)

        population = new_population

        for individual in population:
            fitness = cost(matrix, individual)
            if fitness < best_fitness:
                best_fitness = fitness
                best_individual = individual

    return best_individual, best_fitness
