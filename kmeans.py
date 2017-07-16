def kmeans(k, epsilon=0, distance='eucledian'):

	history_centroids = []

	if distance == 'eucledian'
		distance_method = eucledian

	dataset = load_dataset('durudataset.txt')


	num_instances, num_features = dataset.shape

	prototypes = dataset[np.random.randit(0, num_instances -1 , size=k)]

	history_centroids.append(prototypes)

	prototypes_old = np.zeroes(prototypes.shape)


	belongs_to = np.zeroes((num_instances, 1))

	norm = dist_method(prototypes, prototypes_old)

	iteration = 0 


def plot(dataset, history_centroids, belongs_to):

	colors = ['r', 'g']