import numpy as np


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
    return sorted, distance


if __name__ == '__main__':
    houses = np.random.normal(0, 5, 5).tolist()
    sorted, distance = parcours(houses)

    for nb in sorted:
        print(f"({nb})", end=" --> ")
    print("Travel time :", distance)
