import math

import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns

def checksum(bids):
    df = pd.DataFrame(bids)
    assert df.sum(axis=1).max() == df.sum(axis=1).min() == 100
    assert len(df.columns) == 10
    assert df.min().min() >= 0
    return True


def populate(size=100):
    """initiate population of given size with archetypes"""
    pop = []
    for n in range(size // len(pd.read_csv('archetypes.csv', header=None).values.tolist())):
        pop.extend(pd.read_csv('archetypes.csv', header=None).values.tolist())
    return pop


###
# https://towardsdatascience.com/continuous-genetic-algorithm-from-scratch-with-python-ff29deedd099
###

def random_individual(n_genes, gene_sum):
    """create a random individual with n_genes carrying ints which sum to gene_sum"""
    # https://stackoverflow.com/questions/59148994/how-to-get-n-random-integer-numbers-whose-sum-is-equal-to-m
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


def selection(pop):
    """select the fittest half of the population and make sure it is an even number"""
    return pop.sort_values('fitness', ascending=False).head(math.ceil(len(pop.index) / 4) * 2)


def mutate_simple(indi):
    mutating_genes = np.random.randint(0, len(indi)), np.random.randint(0, len(indi))
    if indi[mutating_genes[0]] > 0 & indi[mutating_genes[1]] < 100:
        indi[mutating_genes[0]] -= 1
        indi[mutating_genes[1]] += 1
    else:
        mutate_simple(indi)
    assert indi.sum() == 100
    return indi
