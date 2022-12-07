import matplotlib.pyplot as plt
from matplotlib import rcParams


def plot_extrema(extrema_input):
    """plot extrema that are stored in Pandas DataFrame in x,y-pairs
    :type extrema_input: Pandas DataFrame with extrema for every cell; columns with x1, y1, x2, y2, ...
    """

    # column names
    labels = list(extrema_input.columns)

    # 12 visually distinguishable colors
    colors = [[0.12157, 0.46667, 0.70588], [1.0, 0.49804, 0.0549], [0.17255, 0.62745, 0.17255],
              [0.83922, 0.15294, 0.15686], [0.58039, 0.40392, 0.74118], [0.54902, 0.33725, 0.29412],
              [0.8902, 0.46667, 0.76078], [0.49804, 0.49804, 0.49804], [0.49804, 1.0, 0.0],
              [0.0, 1.0, 1.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0]]

    plt.figure(figsize=[14.4 / 2.54, 10 / 2.54])
    rcParams.update({'font.size': 8.5, 'lines.linewidth': 1.0})

    last_ind = extrema_input.index[-1]

    if len(extrema_input.columns) <= 12:
        for cell in range(len(extrema_input.columns)):
            plt.plot(extrema_input.iloc[0: last_ind: 2, cell], extrema_input.iloc[1: last_ind + 1: 2, cell],
                     '*', label=labels[cell], color=colors[cell])
    # can't use the color list if more than 12 cells
    else:
        for cell in range(len(extrema_input.columns)):
            plt.plot(extrema_input.iloc[0: last_ind: 2, cell], extrema_input.iloc[1: last_ind + 1: 2, cell],
                     '*', label=labels[cell])

    if len(labels) % 3 == 0:
        number_columns = 3
    else:
        number_columns = 2

    plt.legend(loc="best", ncol=number_columns, frameon=True)
    plt.grid(True)
    plt.title('Extrema')
    plt.xlabel('Discharge Capacity in Ah')
    plt.ylabel('Q dU/dQ in V')