TOTAL_HOUSE_NB = 1000
NB_OF_ZONES = 10
HOUSE_PER_ZONE = int(TOTAL_HOUSE_NB / NB_OF_ZONES)


class Solver():
    """contains methods to solve snowplow problem and display result"""

    @staticmethod
    def chunks(lst, n):
        """Yield successive n-sized chunks from lst."""
        for i in range(0, len(lst), n):
            yield lst[i:i + n]

    def sort_and_cluster_list(self):
        """sort list from smaller to bigger value and chunks those into equal zone"""

        # Sort positions from - to +
        self.sorted_matrice = sorted(self.original_list)
        self.sorted_matrice = list(Solver.chunks(
            self.sorted_matrice, HOUSE_PER_ZONE))

    def get_smallest_tree(self):
        """weight tree and return index of the smallest"""
        self.weight_tree = list()

        for tree in self.sorted_matrice:
            limit = len(tree) - 1
            weight = 0
            for idx, node in enumerate(tree):
                if idx < limit:
                    weight += abs(tree[idx] - tree[idx + 1])
            self.weight_tree.append(
                weight + (abs(self.current_position - tree[0])))
        result_idx = self.weight_tree.index(min(self.weight_tree))
        return result_idx

    def parcourir(self, tree_idx):

        self.sorted_matrice[tree_idx].sort(
            key=lambda x: abs(x-self.current_position))

        #  remove already visited node from the current position to first node of tree_to_browse
        to_reach = self.sorted_matrice[tree_idx][-1]
        visited = list()
        for idx, tree in enumerate(self.sorted_matrice):
            self.sorted_matrice[idx].sort(
                key=lambda x: abs(x-self.current_position))
            for node in tree:
                if to_reach >= node > self.current_position or self.current_position > node >= to_reach:
                    visited.append(node)
            self.sorted_matrice[idx] = [x for x in tree if x not in visited]
        visited += self.sorted_matrice[tree_idx]
        self.sorted_matrice[tree_idx] = []
        self.visited_node += visited

        self.current_position = to_reach
        for idx, tree in enumerate(self.sorted_matrice):
            if not tree:
                del self.sorted_matrice[idx]

    def parcours(self, positions):
        """ returns a list that route the snowplow 
            to optimize waiting time
        """

        # Initializing data
        self.original_list = positions
        self.sorted_matrice = None
        self.weight_tree = list()

        self.visited_node = list()
        self.sort_and_cluster_list()
        self.current_position = 0

        while self.sorted_matrice:  # ITERATE THROUGH EVERY ZONE
            self.sorted_matrice.sort(
                key=lambda x: abs(x[0]-self.current_position))
            tree_idx = self.get_smallest_tree()
            self.parcourir(tree_idx)
        return self.visited_node


def parcours(positions):
    my_solver = Solver()
    return my_solver.parcours(positions)
