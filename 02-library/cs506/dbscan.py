class DBC():

    def __init__(self, dataset, min_pts, epsilon):
        self.dataset = dataset
        self.min_pts = min_pts
        self.epsilon = epsilon


    def _get_epsilon_neighborhood(self, x):
        neighborhood = []
        for i, y in enumerate(self.dataset):
            if i == idx:
                continue
            if euclidean_dist(self.dataset[idx], y) <= self.epsilon:
                neighborhood.append(i)
        return neighborhood
        
    def _make_bfs_assignments(self, queue, assignment, assignments):
        #queue is the neighborhood
        while queue:
            nextP = queue.pop(0)
            if assignments[nextP] != 0:
                continue
            assignments[nextP] = assignment
            neighborhood_of_nextP = self._get_epsilon_neighborhood(nextP)
            if len(neighborhood) >= self.min_pts:
                #core point
                queue += neighborhood_of_nextP
        return assignments


    def dbscan(self):
        """
            returns a list of assignments. The index of the
            assignment should match the index of the data point
            in the dataset.
        """
        assignments = [0 for _ in range(len(self.dataset))]
        assignment = 1
        
        for i, x in enumerate((self.dataset)):
            if assignments[i] != 0:
                continue
            neighborhood = self._get_epsilon_neighborhood((i))

            if len(neighborhood) >= self.min_pts:
                assignments[i] = assignment
                assignments = self._make_bfs_assignments((neighborhood), assignment, assignments)
            assignment += 1
        return assignments