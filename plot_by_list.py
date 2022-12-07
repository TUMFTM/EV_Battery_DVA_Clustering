import matplotlib.pyplot as plt
from matplotlib import rcParams


def plot_by_list(input_x, input_y, list1, list2, title):
    """plot input_x over input_y, seperated into two groups (e.g. by charge)"""

    input_x = input_x[input_y.index]

    plt.figure(figsize=[14.4 / 2.54, 10 / 2.54])
    rcParams.update({'font.size': 8.5, 'lines.linewidth': 1})
    for cell in list1:
        plt.plot(input_x, input_y.iloc[:, cell-1], color='blue')
    for cell in list2:
        plt.plot(input_x, input_y.iloc[:, cell-1], color='red')

    plt.grid(True)
    plt.title(title)
    plt.xlabel('Discharge Capacity in Ah')
    plt.ylabel('DVA in V')
