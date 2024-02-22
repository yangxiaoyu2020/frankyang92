#!/usr/bin/python3.12
# _*_ coding: utf-8 _*_
#
# Copyright (C) 2024 - 2024 frank yang
#
# @Time    : 2024/2/18 19:23
# @Author  : frank yang
# @File    : opt_cut_gen.py
# @IDE     : PyCharm


import random

# Generate initial population
def generate_population(size, item_count):
    population = []
    for _ in range(size):
        individual = list(range(item_count))
        random.shuffle(individual)  # Shuffle items randomly
        population.append(individual)
    return population

# Fitness function
def fitness(individual, items, bin_capacity):
    remaining_capacity = bin_capacity
    for item_index in individual:
        item_size = items[item_index]
        if item_size > remaining_capacity:
            return 0  # Invalid solution, return fitness 0
        remaining_capacity -= item_size
    return 1 / (1 + remaining_capacity)  # Fitness is inversely proportional to remaining capacity

# Selection: Roulette wheel selection
# Selection: Roulette wheel selection
def roulette_wheel_selection(population, fitness_values):
    total_fitness = sum(fitness_values)
    if total_fitness == 0:
        return random.choice(population)
    pick = random.uniform(0, total_fitness)
    current = 0
    for i, individual in enumerate(population):
        current += fitness_values[i]
        if current > pick:
            return individual


# Crossover: Order crossover (OX)
def order_crossover(parent1, parent2):
    print("Parent 1:", parent1)
    print("Parent 2:", parent2)
    start = random.randint(0, len(parent1))
    end = random.randint(start, len(parent1))
    child = [None] * len(parent1)
    child[start:end] = parent1[start:end]
    remaining_items = [item for item in parent2 if item not in child]
    index = 0
    for i in range(len(parent1)):
        if child[i] is None:
            child[i] = remaining_items[index]
            index += 1
    return child


# Mutation: Swap mutation
def swap_mutation(individual):
    index1 = random.randint(0, len(individual) - 1)
    index2 = random.randint(0, len(individual) - 1)
    individual[index1], individual[index2] = individual[index2], individual[index1]
    return individual

# Genetic algorithm
def genetic_algorithm(items, bin_capacity, population_size, generations):
    population = generate_population(population_size, len(items))
    for _ in range(generations):
        fitness_values = [fitness(individual, items, bin_capacity) for individual in population]
        new_population = []
        for _ in range(population_size // 2):
            parent1 = roulette_wheel_selection(population, fitness_values)
            parent2 = roulette_wheel_selection(population, fitness_values)
            print("Parent 1:", parent1)
            print("Parent 2:", parent2)
            child1 = order_crossover(parent1, parent2)
            child2 = order_crossover(parent2, parent1)
            new_population.extend([child1, child2])
        for i in range(len(new_population)):
            if random.random() < mutation_rate:
                new_population[i] = swap_mutation(new_population[i])
        population = new_population
    best_individual = max(population, key=lambda x: fitness(x, items, bin_capacity))
    return best_individual


# Example usage
if __name__ == "__main__":
    items = [10, 20, 30, 40, 50]  # Item sizes
    bin_capacity = 100  # Capacity of the bin
    population_size = 100  # Size of the population
    generations = 100  # Number of generations
    mutation_rate = 0.1  # Mutation rate

    best_individual = genetic_algorithm(items, bin_capacity, population_size, generations)
    print("Best solution:", best_individual)
