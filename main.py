# run main script to cluster cells
import matplotlib.pyplot as plt
import time
import numpy as np

from load_data import load_dataset
from importBioLogic import load_dataset_txt
from calculate_resistance import calc_resistance
from cut_off import cut_signal
from preprocess_signals import prep_signals
from remove_cells_from_data import remove_cells
from calculate_dva import calc_dva
from find_extrema import find_extrema
from plot_extrema import plot_extrema
from clustering_extrema_stepwise import cluster_extrema_stepwise
from print_clusters import print_info
from plot_by_label import plot_by_label
from plot_single_cells import plot


if __name__ == '__main__':

    # TODO: enter number of cells
    number_cells = 4  # 12
    # TODO: enter cell capacity in Ah
    capacity_cell = 4.490e-3  # 3.4

    start_time = time.time()

    # TODO: choose file (.txt) with discharge and pulse (optional), no charge phase allowed
    data_path = 'input/Test1_03_MB.txt'

    # TODO: choose measurement equipment:
    #  option 1: 'BaSyTec'
    #  option 2: 'BioLogic'
    equipment = 'BioLogic'

    # TODO: check cluster parameter in clustering_hierarchical

    if equipment == 'BaSyTec':
        data_file = load_dataset(data_path, number_cells)
    elif equipment == 'BioLogic':
        data_file = load_dataset_txt(data_path, number_cells)
    else:
        raise IOError('Invalid equipment!')

    resistance, data_file = calc_resistance(data_file, number_cells, capacity_cell)

    # TODO (optional): specify cut-off discharge capacity (in Ah, >0)
    cut_off_capacity = capacity_cell / 2
    if cut_off_capacity:
        data_file = cut_signal(data_file, capacity=cut_off_capacity)

    data = prep_signals(data_file, number_cells, capacity_cell)

    # TODO (optional): insert list with cells to exclude (integers, number_cells adapted automatically)
    cells_to_remove = []
    if cells_to_remove:
        data, number_cells, remaining_cells = remove_cells(data, cells_to_remove, number_cells)
    else:
        remaining_cells = [*range(1, number_cells + 1)]

    if number_cells < 2:
        raise IOError('Number of cells has to be at least two!')

    dva = calc_dva(data, remaining_cells)
    # plot(data.Ah, dva, 'DVA by cell')

    extrema_dva = find_extrema(dva, data.Ah, remaining_cells)
    # plot_extrema(extrema_dva)

    labels_stepwise = cluster_extrema_stepwise(extrema_dva)
    print_info(labels_stepwise, np.NaN, 'Stepwise Hierarchical', resistance, remaining_cells, dva)
    plot_by_label(data.Ah, dva, labels_stepwise, 'Plot by Cluster (Stepwise Hierarchical)')

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f'Elapsed Time:\t{elapsed_time:.3f} seconds')

    plt.show()
