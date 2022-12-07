import matplotlib.pyplot as plt
from matplotlib import rcParams
from collections import Counter
from numpy import argwhere
from numpy import ndarray


def plot_by_label(input_x, input_y, label, title):
    """convert label of clustering to lists and plot these lists
    :param title:   title of plot
    :param label:   list with clusters for each cell
    :param input_x: parameter for x-axis
    :type input_y:  parameter for y-axis
    """

    # crop x-values to same length as y-values
    input_x = input_x[input_y.index]

    # list with 12 visually distinguishable colors
    colors = [[0.12157, 0.46667, 0.70588], [1.0, 0.49804, 0.0549], [0.17255, 0.62745, 0.17255],
              [0.83922, 0.15294, 0.15686], [0.58039, 0.40392, 0.74118], [0.54902, 0.33725, 0.29412],
              [0.8902, 0.46667, 0.76078], [0.49804, 0.49804, 0.49804], [0.49804, 1.0, 0.0],
              [0.0, 1.0, 1.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0]]

    # determine number of different clusters
    clusters = len(Counter(label).keys())

    # plt.figure()
    plt.figure(figsize=[14.4 / 2.54, 10 / 2.54])
    rcParams.update({'font.size': 8.5, 'lines.linewidth': 1})

    # plot elements of same cluster in same color
    for cluster in range(clusters):
        indices = argwhere(label == cluster)
        for index in indices:
            if clusters <= 12:
                plt.plot(input_x, input_y.iloc[:, ndarray.item(index)], color=colors[cluster])
            # usage of color list limited to 12 clusters
            else:
                plt.plot(input_x, input_y.iloc[:, ndarray.item(index)])
    plt.grid(True)
    plt.title(title)
    plt.xlabel('Discharge Capacity in Ah')
    plt.ylabel('Q dU/dQ in V')
