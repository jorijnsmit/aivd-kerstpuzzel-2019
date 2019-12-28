import numpy as np

<<<<<<< HEAD
def redist_points(bid):
    """move single point to adjacent envelope"""
    env = np.random.randint(0, 10)
    if bid[env] == 0:
        redist_points(bid)
    bid[env] -= 1
    if np.random.random > 0.5:
        bid[(env + 9) % 10] += 1
=======

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
>>>>>>> 947b4c67b89b96d86167574fb642c42907404594
    else:
        bid[(env + 1) % 10] += 1

<<<<<<< HEAD
def shift_all(bid):
=======

def redist_one_point(bids):
    """move one point to an envelope next to it"""
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
>>>>>>> 947b4c67b89b96d86167574fb642c42907404594
    """shift all bids one envelope to the left or right"""
    if np.random.random > 0.5:
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
    int i = np.random.randint(0, 9)
    t = bid[i]
    bid[i] = bid[i+1]
    bid[i+1] = t


<<<<<<< HEAD
def mutate(bid, redist = 0.1, swap = 0.05, shift = 0.01):
    """mutate a list of bids using given thresholds"""
    if np.random.random() > redist:
        redist_points(bid)
    if np.random.random() > swap:
        swap_values(bid)
    if np.random.random() > shift:
        shift_all(bid)
=======

def mutate(bids, redist1=0.05, redist=0.005, shift=0.0):
    """mutate a list of bids using given thresholds"""
    if np.random.random() < redist1:
        bids = redist_one_point(bids)
    if np.random.random() < redist:
        bids = redist_points(bids)
    if np.random.random() < shift:
        bids = shift_all(bids)
>>>>>>> 947b4c67b89b96d86167574fb642c42907404594
    return bids
