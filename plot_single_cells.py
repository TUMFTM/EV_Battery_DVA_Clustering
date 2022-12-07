from matplotlib import rcParams
import matplotlib.pyplot as plt


def plot(input_x, input_y, title):
    """plot cell dva
    :param title:   series with elements as x-axis
    :param input_y: dataframe with elements to plot
    :type input_x:  title of plot as string
    """

    # crop x-axis according to length of y-elements
    input_x = input_x[input_y.index]
    # get labels for legend
    labels = list(input_y.columns)
    # list with 12 visually distinguishable colors
    colors = [[0.12157, 0.46667, 0.70588], [1.0, 0.49804, 0.0549], [0.17255, 0.62745, 0.17255],
              [0.83922, 0.15294, 0.15686], [0.58039, 0.40392, 0.74118], [0.54902, 0.33725, 0.29412],
              [0.8902, 0.46667, 0.76078], [0.49804, 0.49804, 0.49804], [0.49804, 1.0, 0.0],
              [0.0, 1.0, 1.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0]]

    plt.figure(figsize=[14.4 / 2.54, 10 / 2.54])
    rcParams.update({'font.size': 8.5, 'lines.linewidth': 1.0})

    for cell in range(len(labels)):
        if len(labels) <= 12:
            plt.plot(input_x, input_y.iloc[:, cell], label=labels[cell], color=colors[cell])
        # usage of color list limited to 12 cells
        else:
            plt.plot(input_x, input_y.iloc[:, cell], label=labels[cell])

    if len(labels) % 3 == 0:
        number_columns = 3
    else:
        number_columns = 2

    plt.legend(loc="best", ncol=number_columns, frameon=True)
    plt.grid(True)
    plt.title(title)
    plt.xlabel('Discharge Capacity in Ah')
    plt.ylabel('Q dU/dQ in V')
