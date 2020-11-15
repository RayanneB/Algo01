import numpy as np

from greedy_parcours import greedy_parcours
from parcours import parcours

TOTAL_HOUSE_NB = 1000


def waiting_time(positions):
    time = list()
    distance = 0
    size = len(positions)
    for idx, elem in enumerate(positions):
        if idx < size - 1:
            time.append(distance)
            distance += abs(elem - positions[idx + 1])
            time.append(distance)

    return sum(time) / TOTAL_HOUSE_NB


def test_snowplow():

    house_map = list()

    for i in range(0, 10):
        houses = np.random.normal(0, TOTAL_HOUSE_NB, TOTAL_HOUSE_NB).tolist()
        house_map.append(houses)

    for houses in house_map:
        parcours_time = round(waiting_time(parcours(houses)))
        greedy_time = round(waiting_time(greedy_parcours(houses)))
        to_beat = round(greedy_time - (greedy_time * 9 / 100))

        print("Parcours =>", parcours_time)
        print("Greedy =>", greedy_time)
        if (parcours_time > to_beat):
            print("Failed :( =>", to_beat, end="\n\n")
        else:
            print("Win :) =>", to_beat, end="\n\n")


if __name__ == '__main__':
    test_snowplow()
