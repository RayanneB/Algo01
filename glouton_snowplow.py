import numpy as np
import pprint
from copy import deepcopy


def find_closest(current_position, positions):
    """
        Find the closest position from param:current_position,
        and return it with it's index
    """
    if not positions:
        return None
    positions = np.asarray(positions)
    idx = (np.abs(positions - current_position)).argmin()
    return positions[idx]


def greedy_parcours(positions):
    """ returns a list that route the snowplow 
        to the closest house each time
        greedy algorythm
    """
    visited_nodes = list()
    current_position = 0
    distance = 0
    while positions:
        if current_position != 0:
            visited_nodes.append(current_position)
            positions.remove(current_position)
        next_node = find_closest(current_position, positions)
        if next_node is None:
            break
        distance = distance + abs(next_node - current_position)
        current_position = next_node

    return distance


if __name__ == '__main__':

    houses = np.random.normal(0, 10, 10).tolist()

    print(greedy_parcours(houses))
