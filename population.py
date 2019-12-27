import pandas as pd

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
