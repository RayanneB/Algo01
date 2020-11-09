import numpy as np
from greedy_snowplow import parcours


TOTAL_HOUSE_NB = 1000
NB_OF_ZONES = 2
HOUSE_PER_ZONE = int(TOTAL_HOUSE_NB / NB_OF_ZONES)


def chunk(positions):
    for i in range(0, len(positions), HOUSE_PER_ZONE):
        yield positions[i:i+HOUSE_PER_ZONE]


def find_next_tree(current_node, positions):
    next_node = None
    smallest_distance = None

    for position in positions:
        distance = abs(current_node[-1] - position[0])
        if (smallest_distance == None or distance < smallest_distance):
            smallest_distance = distance
            next_node = position
    return next_node


def gdt(positions):

    tmp = list(chunk(list(positions)))

    position = [0, 0]
    sorted = []
    total_distance = 0

    while tmp:
        next_node = find_next_tree(position, tmp)

        sorted += next_node

        total_distance += abs(position[-1] - next_node[0]) + \
            abs(next_node[-1] - next_node[0])

        tmp.remove(next_node)

    return sorted, total_distance


if __name__ == '__main__':
    houses = np.random.normal(0, TOTAL_HOUSE_NB, TOTAL_HOUSE_NB).tolist()

    sorted, distance = parcours(houses)
    sorted2, distance2 = gdt(houses)

    print("greedy\t", distance)
    print("Algo \t", distance2)

    print("L'algo a été", round(distance2 * 100 / distance), "% inférieur")
