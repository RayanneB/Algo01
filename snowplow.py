import numpy as np 
import pprint

def parcours(positions):
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(positions)
    return list()


if __name__ == '__main__': 
    parcours(np.random.normal(0, 1000, 1000).tolist())