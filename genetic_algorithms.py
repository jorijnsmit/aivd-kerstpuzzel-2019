import numpy as np

def redist_points(bid):
    """move single point to adjacent envelope"""
    env = np.random.randint(0, 10)
    if bid[env] == 0:
        redist_points(bid)
    bid[env] -= 1
    if np.random.randint(0,1) == 0:
        bid[(env + 9) % 10] += 1
    else:
        bid[(env + 1) % 10] += 1

def shift_all(bid):
    """shift all bids one envelope to the left or right"""
    if np.random.randint(0,1) == 0:
        t = bid[0]
        for i in range(9):
            bid[i] = bid[i+1]
        bid[9] = t
    else:
        t = bid[9]
        for i in range(9):
            bid[9-i] = bid[9-i-1]
        bid[0] = t

def swap_values(bid):
    """randomly swap two adjacent envelopes"""
    i = np.random.randint(0, 9)
    t = bid[i]
    bid[i] = bid[i+1]
    bid[i+1] = t


def mutate(bid, redist = 0.1, swap = 0.1, shift = 0.05):
    """mutate a list of bids using given thresholds"""
    if np.random.random() < redist:
        redist_points(bid)
    if np.random.random() < swap:
        swap_values(bid)
    if np.random.random() < shift:
        shift_all(bid)
    return bid

mutate([2, 2, 2, 2, 2, 2, 12, 22, 27, 27])
