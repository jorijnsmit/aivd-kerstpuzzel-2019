import numpy as np
import pandas as pd

from genetic_algorithms import mutate

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
    for i in range(min(5, len(bids))):
        #print (bids[i], scores[i])
        winner = bids[0], scores[0]
    for i in range(len(bids)):
        bids[i] = mutate(bids[i])
    return bids, winner


def checksum(bids):
    df = pd.DataFrame(bids)
    assert df.sum(axis=1).max() == df.sum(axis=1).min() == 100
    assert len(df.columns) == 10
    assert df.min().min() >= 0
    return True

CHAMPION = [], 0
egbids = pd.read_csv('archetypes.csv', header=None).values.tolist()

for n in range(1000):
    checksum(egbids)
    egbids, winner = run_tournament(egbids)
    if CHAMPION[-1] < winner[-1]:
        CHAMPION = winner
        print(f'new champion: {CHAMPION}')
