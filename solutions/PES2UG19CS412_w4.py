import numpy as np


class KNN:
    """
    K Nearest Neighbours model
    Args:
        k_neigh: Number of neighbours to take for prediction
        weighted: Boolean flag to indicate if the nieghbours contribution
                  is weighted as an inverse of the distance measure
        p: Parameter of Minkowski distance
    """

    def __init__(self, k_neigh, weighted=False, p=2):

        self.weighted = weighted
        self.k_neigh = k_neigh
        self.p = p

    def fit(self, data, target):
        """
        Fit the model to the training dataset.
        Args:
            data: M x D Matrix( M data points with D attributes each)(float)
            target: Vector of length M (Target class for all the data points as int)
        Returns:
            The object itself
        """

        self.data = data
        self.target = target.astype(np.int64)

        return self

    def find_distance(self, x):
        """
        Find the Minkowski distance to all the points in the train dataset x
        Args:
            x: N x D Matrix (N inputs with D attributes each)(float)
        Returns:
            Distance between each input to every data point in the train dataset
            (N x M) Matrix (N Number of inputs, M number of samples in the train dataset)(float)
        """
        out = []
        #print("HERE")
        for curr_row in x:
                curr_list = []
                for row in self.data:
                        #print(row)
                        #print(curr_row)
                        val = 0.0;
                        for i,entry in enumerate(row):
                                #print(i)
                                val += pow(abs(entry-curr_row[i]),self.p)
                        val = pow(val, 1/self.p)
                        curr_list.append(val)
                out.append(curr_list)
        #print(out)
        out = np.array(out)
        return out

    def k_neighbours(self, x):
        """
        Find K nearest neighbours of each point in train dataset x
        Note that the point itself is not to be included in the set of k Nearest Neighbours
        Args:
            x: N x D Matrix( N inputs with D attributes each)(float)
        Returns:
            k nearest neighbours as a list of (neigh_dists, idx_of_neigh)
            neigh_dists -> N x k Matrix(float) - Dist of all input points to its k closest neighbours.
            idx_of_neigh -> N x k Matrix(int) - The (row index in the dataset) of the k closest neighbours of each input

            Note that each row of both neigh_dists and idx_of_neigh must be SORTED in increasing order of distance
        """
        distances = self.find_distance(x)
        #print(distances)
        indices = np.argsort(distances, axis = 1)
        idx_of_neigh = []
        neigh_dist = []
        for i in range(len(indices)):
                curr_neigh_id = []
                curr_neigh_dist = []
                for j in range(self.k_neigh):
                        curr_neigh_id.append(indices[i][j])
                        #print(indices[i][j])
                        curr_neigh_dist.append(distances[i][indices[i][j]])
                neigh_dist.append(curr_neigh_dist)
                idx_of_neigh.append(curr_neigh_id)
        return (neigh_dist,idx_of_neigh)

    def predict(self, x):
        """
        Predict the target value of the inputs.
        Args:
            x: N x D Matrix( N inputs with D attributes each)(float)
        Returns:
            pred: Vector of length N (Predicted target value for each input)(int)
        """
        pred = []
        neighbours = self.k_neighbours(x)
        #print(neighbours)
        for row in neighbours[1]:
                d = dict()
                #print(row)
                for ind in row:
                        #print(d[self.target[ind]])
                        if self.target[ind] in d:
                                d[self.target[ind]] = d[self.target[ind]] + 1
                        else: 
                                d[self.target[ind]] = 1
                #print(d)
                curr_key = self.target[row[0]]
                for key in d.keys():
                        if d[key] > d[curr_key]:
                                curr_key = key
                pred.append(curr_key)
                
        #print(np.array(pred))
        return np.array(pred)

    def evaluate(self, x, y):
        """
        Evaluate Model on test data using 
            classification: accuracy metric
        Args:
            x: Test data (N x D) matrix(float)
            y: True target of test data(int)
        Returns:
            accuracy : (float.)
        """
        pred = self.predict(x)
        #print(pred)
        #print(typeof y )
        right = np.sum(pred == y)
        #print(right, len(y))
        #print(right/total)             
        return (100*(right/len(y)))
