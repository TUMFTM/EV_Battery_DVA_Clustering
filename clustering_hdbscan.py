from hdbscan import HDBSCAN
from sklearn.metrics import silhouette_score
from collections import Counter
import numpy as np


def hdbscan(input_data):
    """performs hdbscan, i.e. dbscan with varying epsilon values
    >> only works with cosine similarity as input
    :type input_data:   Pandas DataFrame with inputs
    """

    features = input_data.T

    labels = HDBSCAN(min_cluster_size=2).fit_predict(features)

    # change labels for outlier to positive integer, every outlier has its own label
    outliers = np.argwhere(labels == -1)
    for outlier in outliers:
        labels[outlier] = max(labels) + 1

    if 1 < len(Counter(labels).keys()) < len(labels):
        silhouette = silhouette_score(features, labels)
    else:
        silhouette = np.NaN

    return labels, silhouette
