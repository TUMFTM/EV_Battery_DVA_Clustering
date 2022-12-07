import pandas as pd
import numpy as np
from clustering_hierarchical import hierarchical


def cluster_extrema_stepwise(extrema_input):
    """Cluster every extremum by its own and merge label lists afterwards
    :type extrema_input: Pandas DataFrame with extrema for every cell; columns with x1, y1, x2, y2, ...
    """

    extrema_input.dropna(inplace=True)
    number_extrema = np.int(len(extrema_input.index) / 2)
    number_cells = len(extrema_input.columns)
    labels = pd.DataFrame(index=range(number_extrema), columns=range(number_cells))

    # scale data to [0, 1] in order to work with set distance threshold
    # scale x-axis (discharge capacity)
    min_Ah = np.min(np.min(extrema_input.iloc[0: 2 * number_extrema: 2, :]))
    max_Ah = np.max(np.max(extrema_input.iloc[0: 2 * number_extrema: 2, :]))
    extrema_input.iloc[0: 2 * number_extrema: 2, :] \
        = (extrema_input.iloc[0: 2 * number_extrema: 2, :] - min_Ah) / (max_Ah - min_Ah)
    # scale y-axis (dva)
    min_dva = np.min(np.min(extrema_input.iloc[1: 2*number_extrema+1: 2, :]))
    max_dva = np.max(np.max(extrema_input.iloc[1: 2*number_extrema+1: 2, :]))
    extrema_input.iloc[1: 2*number_extrema+1: 2, :] = \
        (extrema_input.iloc[1: 2*number_extrema+1: 2, :] - min_dva) / (max_dva - min_dva)

    # cluster cells for each extremum separately
    for extremum in range(0, 2 * number_extrema, 2):
        # generate list with x,y values of all cells for one extremum
        xy_extremum = pd.DataFrame(index=[0, 1], columns=range(number_cells))
        xy_extremum.iloc[0, :] = extrema_input.iloc[extremum, :]
        xy_extremum.iloc[1, :] = extrema_input.iloc[extremum+1, :]
        features = np.array(xy_extremum, dtype=float).T

        labels_extremum, silhouette = hierarchical(features)

        # store cluster results of each extremum in one general DataFrame
        labels.iloc[np.int(extremum / 2), :] = labels_extremum

    # determine global list of labels
    # if one extremum is above distance threshold this cell is handled as outlier
    output_labels = np.zeros([number_cells, 1], dtype=int)
    number_outlier = 1

    for cell in range(number_cells):
        if np.max(labels.iloc[:, cell]) != 0:
            output_labels[cell] = number_outlier
            number_outlier += 1

    # if only outliers offset cluster labels from 1,2,3,... to 0,1,2,...
    if min(output_labels[:, 0]) == 1:
        output_labels[:, 0] = output_labels[:, 0] - 1

    return output_labels[:, 0]
