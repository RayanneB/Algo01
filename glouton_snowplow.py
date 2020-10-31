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

    while positions:
        if current_position != 0:
            visited_nodes.append(current_position) 
            positions.remove(current_position)
        next_node = find_closest(current_position, positions)
        if next_node is None:
            break
        current_position = next_node

    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(visited_nodes)
    return visited_nodes


if __name__ == '__main__': 
    greedy_parcours(np.random.normal(0, 1000, 1000).tolist())