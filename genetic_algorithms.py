import numpy as np


def redist_points(bids):
    """move random amount of points to an envelope next to it"""
    envelope = np.random.randint(0, len(bids))
    if bids[envelope] > 0:
        to_redist = np.random.randint(1, bids[envelope] + 1)
        bids[envelope] -= to_redist
        if np.random.randint(0, 1) > 0:
            bids[envelope + 1] += to_redist
        else:
            bids[envelope - 1] += to_redist
    else:
        redist_points(bids)
    return bids


def redist_one_point(bids):
    """move random amount of points to an envelope next to it"""
    envelope = np.random.randint(0, len(bids))
    if bids[envelope] > 0:
        bids[envelope] -= 1
        if np.random.randint(0, 1) > 0:
            bids[envelope + 1] += 1
        else:
            bids[envelope - 1] += 1
    else:
        redist_one_point(bids)
    return bids


def shift_all(bids):
    """shift all bids one envelope to the left or right"""
    # todo
    return bids


def mutate(bids, redist1=0.05, redist=0.005, shift=0.0):
    """mutate a list of bids using given thresholds"""
    if np.random.random() < redist1:
        bids = redist_one_point(bids)
    if np.random.random() < redist:
        bids = redist_points(bids)
    if np.random.random() < shift:
        bids = shift_all(bids)
    return bids
