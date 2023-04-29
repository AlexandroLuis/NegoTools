from sklearn.metrics import silhouette_score
from sklearn.cluster import KMeans

class kmeans():
    def __init__(self, dataset, nr_means, max_iter):
        self.dataset = dataset
        self.nr_means = nr_means
        self.max_iter = max_iter
        
    def run(self):
        start = 2
        end = self.nr_means
        
        nr_clusters = 0
        result = self.dataset
        best_silhouette = -9999

        try:
            for n_clusters in range(start, end):
                kMeans = KMeans(n_clusters = n_clusters, init='k-means++', max_iter=self.max_iter, n_init=1)
                labels = kMeans.fit_predict(self.dataset)

                silhouette_avg = round(silhouette_score(self.dataset, labels, random_state=1), 3)

                if silhouette_avg > best_silhouette:
                    best_silhouette = silhouette_avg
                    result = labels
                    nr_clusters = n_clusters
        except Exception as e:
            raise ValueError(f"wrong params at {e}")

        return result, nr_clusters