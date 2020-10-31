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



def parcours(positions):
    sorted = list()
    tmp = list(positions)
    total_distance = 0
    current_position = 0

    while(len(tmp) > 1):
        current_distance = None
        nearest_position = 0
        for j in range(len(tmp)):
            if j != current_position:
                distance = abs(tmp[j] - tmp[current_position])
                if current_distance == None or current_distance > distance:
                    current_distance = distance
                    nearest_position = tmp[j]

        sorted.append(tmp[current_position])
        tmp.pop(current_position)
        current_position = tmp.index(nearest_position)
        total_distance += current_distance

    return total_distance + abs(positions[0] - tmp[0])

if __name__ == '__main__':
    
    houses = np.random.normal(0, 10, 10).tolist()
    print(parcours(houses))
    print(greedy_parcours(houses))