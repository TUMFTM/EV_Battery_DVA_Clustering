import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import silhouette_score
from collections import Counter
from plot_dendrogram import plot_dendrogram


def hierarchical(features: np.array):
    """
    cluster input data hierarchically (agglomerative)
    affinity:   “euclidean”, “l1”, “l2”, “manhattan”, “cosine”, or “precomputed”
                If linkage is “ward”, only “euclidean” is accepted
    linkage:    ‘ward’ minimizes the variance of the clusters being merged
                ‘average’ uses the average of the distances of each observation of the two sets
                ‘complete’ or ‘maximum’ linkage uses the maximum distances between all observations of the two sets
                ‘single’ uses the minimum of the distances between all observations of the two sets
    distance_threshold: The linkage distance threshold above which, clusters will not be merged.
                        If not None, n_clusters must be None and compute_full_tree must be True
    :param features:    normalised features for clustering: list with x,y values of one extremum
    """

    # labels_legend = np.array(range(1, features.shape[0] + 1))
    # plt.figure(figsize=[14.4 / 2.54, 10 / 2.54])
    # rcParams.update({'font.size': 8.5})
    # plot_dendrogram(AgglomerativeClustering(n_clusters=None, affinity='euclidean', linkage='average',
    #                                         distance_threshold=0).fit(features), labels_legend)
    # plt.title('Dendrogram')
    # plt.xlabel('Cells')
    # plt.ylabel('Distance')

    labels_agg = AgglomerativeClustering(n_clusters=None, affinity='euclidean', linkage='average',
                                         distance_threshold=0.27, compute_full_tree=True).fit_predict(features)
    # # proven distance_threshold for INR18650: 0.065
    # # proven distance_threshold for coin cells: 0.27

    # make sure that main cluster has the index 0
    elements_cluster_0 = len(np.argwhere(labels_agg == 0))
    elements_cluster_1 = len(np.argwhere(labels_agg == 1))
    if elements_cluster_1 >= elements_cluster_0:
        for index, value in enumerate(labels_agg):
            if value == 1:
                labels_agg[index] = 0
            elif value == 0:
                labels_agg[index] = 1

    # compute silhouette score if number of found clusters is in valid range
    if 1 < len(Counter(labels_agg).keys()) < features.shape[0]:
        silhouette = silhouette_score(features, labels_agg)
    else:
        silhouette = np.NaN

    return labels_agg, silhouette
