import numpy as np
import sys
from pprint import pprint

TOTAL_HOUSE_NB = 100
NB_OF_ZONES = 10
HOUSE_PER_ZONE = TOTAL_HOUSE_NB / NB_OF_ZONES

np.set_printoptions(suppress=True, threshold=sys.maxsize)

class Solver(): 

    def __init__(self, original_list):
        self.original_list = original_list
        self.sorted_matrice = None
        self.minimum_spanning_tree = list()
    
    def chunks(self, lst, n):
        """Yield successive n-sized chunks from lst."""
        for i in range(0, len(lst), n):
            yield lst[i:i + n]

    def sort_and_cluster_list(self):
            self.sorted_matrice = sorted(self.original_list) # Sort positions from - to +
            self.sorted_matrice = list(self.chunks(self.sorted_matrice, int(HOUSE_PER_ZONE)))
            
    def convert_and_sort_positions_to_edges(self, zone):
        edges_list = list()
        for index, node in enumerate(zone):
            
            if index != HOUSE_PER_ZONE - 1:
                edges_list.append({
                    'vertices': [zone[index], zone[index + 1]],
                    'weight': abs(zone[index] - zone[index + 1])
                })

        edges_list = sorted(edges_list, key = lambda elem: elem['weight'])

        return edges_list


    def solve(self):
        """ returns a list that route the snowplow 
            to optimize waiting time
        """
        self.sort_and_cluster_list()

        visited_nodes = list()
        current_position = 0
        for index, zone in enumerate(self.sorted_matrice):
            # convert positions to nodes
            self.sorted_matrice[index] = self.convert_and_sort_positions_to_edges(zone)
            pprint(self.sorted_matrice[index])
            

        
if __name__ == '__main__':
    my_solver = Solver(np.random.normal(0, TOTAL_HOUSE_NB, TOTAL_HOUSE_NB).tolist())
    my_solver.solve()