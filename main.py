import numpy as np
import pandas as pd

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
        print (bids[i], scores[i])

def checksum(bids):
    df = pd.DataFrame(bids)
    assert df.sum(axis=1).max() == df.sum(axis=1).min() == 100
    assert len(df.columns) == 10
    assert df.min().min() >= 0
    return True

egbids = []
egbids.append([10, 10, 10, 10, 10, 10, 10, 10, 10, 10])
egbids.append([1, 1, 3, 4, 7, 9, 13, 16, 21, 25])
egbids.append([2, 2, 2, 2, 2, 2, 12, 22, 27, 27])
egbids.append([0, 0, 0, 0, 0, 10, 20, 30, 40, 0])
egbids.append([1, 1, 1, 1, 1, 1, 6, 13, 25, 50])
egbids.append([0, 0, 0, 0, 0, 0, 25, 25, 25, 25])
egbids.append([1, 11, 11, 11, 11, 11, 11, 11, 11, 11])
egbids.append([25, 0, 0, 0, 0, 0, 0, 0, 25, 25, 25])
egbids.append([1, 3, 5, 7, 9, 11, 13, 15, 17, 19])

checksum(egbids)
run_tournament(egbids)
