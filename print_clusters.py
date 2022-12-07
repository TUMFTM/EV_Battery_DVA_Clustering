import numpy as np


def print_info(label, silhouette_coeff, cluster_algorithm, resistance, remaining_cells, input_data):
    """print cluster number and ohmic resistance (if available) for every cell
    :param remaining_cells:     list with all remaining cells
    :param input_data:          input of clustering, used to extract correct cell names
    :param cluster_algorithm:   clustering algorithm as string
    :param silhouette_coeff:    silhouette coefficient describes quality of clustering
    :param resistance:          list with resistance for each cell
    :type label:                list with cluster label for each cell
    """

    print(f'\nCluster Algorithm: {cluster_algorithm}')

    print(f'Silhouette Coefficient: {silhouette_coeff:.3f}')

    cell_names = input_data.columns

    if not np.any(resistance):
        for cell in range(len(remaining_cells)):
            print(f'{cell_names[cell].title()}\tCluster Index: {label[cell]}')
    else:
        for cell in range(len(remaining_cells)):
            print(f'{cell_names[cell].title()}\t\tCluster Index: {label[cell]}'
                  f'\tOhmic Resistance: {resistance[remaining_cells[cell] - 1]:.4f} mOhm')

        # warn if one internal resistance is suspiciously high / low
        upper_resistance_deviation = (max(resistance) - np.median(resistance)) / np.median(resistance)
        lower_resistance_deviation = (np.median(resistance) - min(resistance)) / np.median(resistance)

        if upper_resistance_deviation >= 1.2:
            print('Caution: At least one Ohmic resistance is suspiciously high.')
        elif lower_resistance_deviation >= 0.2:
            print('Caution: At least one Ohmic resistance is suspiciously low.')
