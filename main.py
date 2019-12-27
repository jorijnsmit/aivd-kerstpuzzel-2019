import numpy as np
import pandas as pd

from genetic_algorithms import mutate
from population import *


def run_tournament(bids):
    scores = [0 for i in range(len(bids))]
    for i in range(len(bids) - 1):
        for j in range(i + 1, len(bids) - 1):
            for e in range(10):
                if bids[i][e] > bids[j][e]:
                    scores[i] += e + 1
                elif bids[j][e] > bids[i][e]:
                    scores[j] += e + 1
    for i in range(len(bids) - 1):
        for j in range(i + 1, len(bids) - 1):
            if scores[i] < scores[j]:
                t = scores[i]
                scores[i] = scores[j]
                scores[j] = t
                t = bids[i]
                bids[i] = bids[j]
                bids[j] = t
    return bids[0], scores[0]

POPULATION = populate(1000)
CHAMPION = [], 0

for n in range(1000):
    print(f'{n}.', end='', flush=True)
    checksum(POPULATION)
    winner = run_tournament(POPULATION)
    if CHAMPION[-1] < winner[-1]:
        CHAMPION = winner
        print(f'\nnew champion in round {n}: {CHAMPION}')
    for i, _ in enumerate(POPULATION):
        POPULATION[i] = mutate(POPULATION[i], redist=0.05)
