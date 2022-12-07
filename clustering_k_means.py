import scipy.cluster.vq as scv
from sklearn.metrics import silhouette_score
from collections import Counter
from numpy import NaN


def kmeans(input_data):
    """cluster input_data with k-means
    :type input_data: data as Pandas DataFrame
    """

    features = input_data.T
    # normalize data
    whitened = scv.whiten(features)

    centroid, labels = scv.kmeans2(whitened, 2)

    if len(Counter(labels).keys()) > 1:
        silhouette = silhouette_score(features, labels)
    else:
        silhouette = NaN

    return labels, silhouette
