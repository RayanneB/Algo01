import numpy as np



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

    return visited_nodes, distance


def find_nearest(current_node, positions):
    nearest = None
    smallest_distance = None
    for position in positions:
        if (position == None or current_node != position):
            distance = abs(position - current_node)
            if smallest_distance == None or distance < smallest_distance:
                nearest = position
                smallest_distance = distance
    return nearest, smallest_distance


def parcours(positions):
    sorted = list()
    tmp = list([0] + positions)
    current_node = 0
    distance = 0
    while tmp:
        nearest_node, nearest_distance = find_nearest(current_node, tmp)
        if nearest_node == None:
            break
        else:
            distance += nearest_distance
            sorted.append(nearest_node)
            tmp.pop(tmp.index(current_node))
            current_node = nearest_node
    return distance


if __name__ == '__main__':
    houses = np.random.normal(0, 1000, 1000).tolist()
    sorted, distance = parcours(houses)
    sorted_2, distance_2 = greedy_parcours(houses)

    for nb in sorted:
        print(f"({nb})", end=" --> ")
    print("Travel time :", distance)
    print(f"Distance to beat : ", (distance / 10) * 9)