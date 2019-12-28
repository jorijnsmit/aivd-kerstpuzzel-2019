# thanks to
# https://towardsdatascience.com/continuous-genetic-algorithm-from-scratch-with-python-ff29deedd099

import numpy as np
import matplotlib.pylab as plt
import seaborn as sns

from genetic_algorithms import mutate

def random_individual(n_genes, gene_sum):
    """create a random individual with n_genes carrying ints which sum to gene_sum"""
    # https://stackoverflow.com/questions/59148994/
    individual = np.random.multinomial(gene_sum, np.ones(n_genes) / n_genes)
    return individual


def random_population(size, n_genes, gene_sum):
    """create a population of size consisting of random individuals"""
    return [random_individual(n_genes, gene_sum) for x in range(size)]


def plot_individual(indi):
    """plot a bar chart of an individual"""
    sns.barplot(np.arange(len(indi)), indi)
    plt.show()


def calc_fitness(individual, population):
    """calculate the fitness of an individual relative to the rest of the population"""
    worth = np.arange(1, 11)
    fitness = 0
    # we ignore the fact that one of the contestants will be the individual itself
    # since fitness gained from that will be 0 anyway
    for contestant in population:
        fitness += ((individual > contestant) * worth).sum()
    return fitness


def selection(population):
    """select the fittest half of the population by advancing
    only individuals that perform above the mean"""
    # still some bug that sometimes makes the selection too small
    divider = len(population) // 2
    fitness = []
    selected = []
    for individual in population:
        fitness.append(calc_fitness(individual, population))
    fit_mean = np.array(fitness).mean()
    for i, _ in enumerate(population):
        if fitness[i] >= fit_mean:
            selected.append(population[i])
    return selected[:divider]


def evolve(population, generations):
    """evolve a population over given amount of generations"""
    for g in range(generations):
        selected = selection(population)
        print(f'{g}\t{selected[0]}')
        #plot_individual(df.iloc[0, :10])
        mutators = []
        for individual in selected:
            mutators.append(mutate(individual, redist=0.5))
        selected.extend(mutators)
        population = selected
    return population
