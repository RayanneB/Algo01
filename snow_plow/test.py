import numpy as np
from Solver import Solver


TOTAL_HOUSE_NB = 1000

NB_OF_ZONES = 10
HOUSE_PER_ZONE = TOTAL_HOUSE_NB / NB_OF_ZONES


def test_snowplow():
    my_solver = Solver()
    ngbrh = list()
    for x in range(1, 100, 1):
        ngbrh.append(np.random.normal(0, TOTAL_HOUSE_NB, TOTAL_HOUSE_NB).tolist())
    

    moy_1_list = list()
    moy_2_list = list()
    for elem in ngbrh:
        moy_1_list.append(my_solver.parcours(elem))
        moy_2_list.append(my_solver.greedy_parcours(elem))

    
    
    print(sum(moy_1_list) / 100)
    print(sum(moy_2_list) / 100)

    print('Score To beat')
    print((sum(moy_2_list) / 100) / 10 * 9)
        
    

if __name__ == '__main__':
    test_snowplow()
    