import numpy as np
import sys
from pprint import pprint
from greedy_snowplow import parcours
from numpy.lib.npyio import save

TOTAL_HOUSE_NB = 1000
NB_OF_ZONES = 2
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


    def find_nearest_spanning_tree(self):
        saved_idx = 0
        tmp = abs(self.sorted_matrice[0][0]['vertices'][0] - self.current_position)
        
        for idx, elem in enumerate(self.sorted_matrice):
            distance = abs(elem[0]['vertices'][0] - self.current_position) 
            saved_idx = idx if distance < tmp   else saved_idx
            if saved_idx == idx:
                tmp = distance

        
        return saved_idx

        
    def parcours(self, tree_idx):
        # Add distance from current position to the first node of the spanning tree
        self.totaldistance += abs(self.current_position - self.sorted_matrice[tree_idx][0]['vertices'][0])
        self.current_position = self.sorted_matrice[tree_idx][0]['vertices'][0]
        
        for elem in self.sorted_matrice[tree_idx]:
            self.totaldistance += elem['weight']

        

    def solve(self):
        """ returns a list that route the snowplow 
            to optimize waiting time
        """
        self.sort_and_cluster_list()
        self.totaldistance = 0
        self.current_position = 0
        for index, zone in enumerate(self.sorted_matrice):
            # convert positions to nodes
            self.sorted_matrice[index] = self.convert_and_sort_positions_to_edges(zone)
        
        pprint(self.sorted_matrice[0])

        while self.sorted_matrice: # ITERATE THROUGH EVERY MST
            tree_idx = self.find_nearest_spanning_tree()
            self.parcours(tree_idx)
            self.sorted_matrice.pop(tree_idx)
        return self.totaldistance

                 

            

        
if __name__ == '__main__':
    houses = np.random.normal(0, TOTAL_HOUSE_NB, TOTAL_HOUSE_NB).tolist()
    my_solver = Solver(houses)
    print(f"Distance  obtenue avec notre algo {my_solver.solve()}")

    print(f"Distance à battre {(parcours(houses) / 9) * 10}")