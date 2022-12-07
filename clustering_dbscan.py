from sklearn.cluster import DBSCAN
from sklearn.metrics import silhouette_score
from collections import Counter
import numpy as np


def dbscan(input_data):
    """performs dbscan on input data
    :type input_data:   Pandas DataFrame with inputs
    """

    features = input_data.T

    labels = DBSCAN(eps=10, min_samples=2).fit_predict(features)
    # proven parameters for INR18650: eps=2.1, min_samples=3
    # proven parameters for coin cells: eps=10, min_samples=2

    # change labels for outlier to positive integer, every outlier has its own label
    outliers = np.argwhere(labels == -1)
    for outlier in outliers:
        labels[outlier] = max(labels) + 1

    if 1 < len(Counter(labels).keys()) < len(labels):
        silhouette = silhouette_score(features, labels)
    else:
        silhouette = np.NaN

    return labels, silhouette
