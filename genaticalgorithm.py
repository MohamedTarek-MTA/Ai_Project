#genaticalgorithm.py
import random
import numpy as np


def genetic_algorithm(graph, population_size,mutation_rate, num_generations):
    population = [generate_individual(graph) for _ in range(population_size)]
    fitness_scores = [fitness_function(graph, individual) for individual in population]

    for _ in range(num_generations):
        new_population = []

        # Keep the best individual
        best_individual = population[np.argmax(fitness_scores)]
        new_population.append(best_individual)

        # Generate the rest of the population through crossover and mutation
        for _ in range(1, population_size):
            parent1 = select_parent(graph, population, fitness_scores)
            parent2 = select_parent(graph, population, fitness_scores)

            offspring = crossover(graph, parent1, parent2)
            offspring = mutate(graph, offspring,mutation_rate)

            new_population.append(offspring)

        population = new_population
        fitness_scores = [fitness_function(graph, individual) for individual in population]

    best_individual = population[np.argmax(fitness_scores)]
    return best_individual

def generate_individual(graph):
    chromosome = {}
    for node in graph.nodes:
        neighbors = list(graph.neighbors(node))
        neighbors_colors = set(chromosome.get(neighbor, 0) for neighbor in neighbors)
        available_colors = set(range(1, len(neighbors) + 2)) - neighbors_colors
        chromosome[node] = random.choice(list(available_colors))
    return chromosome

def fitness_function(graph, individual):
    score = 0
    for node in graph.nodes:
        neighbors_colors = [individual[neighbor] for neighbor in graph[node]]
        if individual[node] in neighbors_colors:
            score += 1
    return score


def select_parent(graph, population, fitness_scores):
    total_fitness = sum(fitness_scores)

    if total_fitness > 0:
        return population[random.choices(range(len(population)), weights=fitness_scores, k=1)[0]]
    else:
        # If total fitness is zero, choose a parent uniformly at random
        return random.choice(population)

def crossover(graph, parent1, parent2):
    crossover_point = random.choice(list(parent1.keys()))

    offspring = {}
    for node in graph.nodes:
        if node < crossover_point:
            offspring[node] = parent1[node]
        else:
            neighbors_colors = [offspring.get(neighbor, parent2[neighbor]) for neighbor in graph[node]]
            available_colors = [color for color in range(1, len(neighbors_colors) + 2) if color not in neighbors_colors]
            offspring[node] = random.choice(available_colors)

    return offspring

def mutate(graph, individual,mutation_rate):

    for node in individual.keys():
        if random.random() < mutation_rate:
            neighbors_colors = [individual[neighbor] for neighbor in graph[node]]
            available_colors = [color for color in range(1, len(neighbors_colors) + 2) if color not in neighbors_colors]
            individual[node] = random.choice(available_colors)

    return individual
def chromosome_to_graph(graph, chromosome):
    individual_graph = {}
    for node, color in chromosome.items():
        individual_graph[node] = [neighbor for neighbor in graph[node] if chromosome[neighbor] != color]
    return individual_graph



def chromatic_number(coloring):
    return len(set(coloring.values()))
