import numpy as np
from Solver import Solver


TOTAL_HOUSE_NB = 1000
NB_OF_ZONES = 10
HOUSE_PER_ZONE = TOTAL_HOUSE_NB / NB_OF_ZONES


def test_snowplow():
    my_solver = Solver()
    ngbrh = list()
    for x in range(1, 10, 1):
        ngbrh.append(np.random.normal(0, TOTAL_HOUSE_NB, TOTAL_HOUSE_NB).tolist())
    

    for elem in ngbrh:
        print("---------------------------------------------------")
        my_solver.parcours(elem)
        print("MY ALGO ")
        print("GREEDY")
        my_solver.greedy_parcours(elem)
        print("---------------------------------------------------")
        
    

if __name__ == '__main__':
    test_snowplow()
    