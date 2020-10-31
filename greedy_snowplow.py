import math
import numpy as np

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

    return sorted, total_distance + abs(positions[0] - tmp[0])

if __name__ == '__main__':
    nbrs = np.random.normal(0, 1000, 1000).tolist()
    sorted, total = parcours(nbrs)
    print(sorted, total)
