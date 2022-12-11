import numpy as np
import pandas as pd
from scipy.signal import find_peaks


def find_extrema(input_dva: pd.DataFrame, input_Ah: pd.Series, remaining_cells):
    """find peaks and valleys of dva signal for each cell, store x and y values to new Pandas DataFrame
    parameter to find peaks: prominence
    :param remaining_cells: list with all remaining cells
    :param input_Ah:        cumulative discharge capacity
    :type input_dva:        dva of all cells
    """

    output_extrema = pd.DataFrame(None)

    for cell in range(len(input_dva.columns)):
        # get indices of maxima
        peaks = find_peaks(input_dva.iloc[:, cell], prominence=0.03)
        # get indices of minima
        valleys = find_peaks(-input_dva.iloc[:, cell], prominence=0.03)
        # sorted list with both indices
        indices = np.concatenate([peaks[0], valleys[0]])
        indices.sort(axis=0)
        # add last index of signal as this one is not detected as peak
        indices = np.append(indices, len(input_dva.index) - 1)

        # build array with x,y values for every extremum
        extrema = np.zeros([2 * len(indices), 1])
        for extremum in range(0, 2 * len(indices) - 1, 2):
            extrema[extremum] = input_Ah[indices[np.int(extremum / 2)]]
            extrema[extremum + 1] = input_dva.iloc[indices[np.int(extremum / 2)], cell]

        output_extrema.loc[:, f'cell_{remaining_cells[cell]}'] = pd.Series(extrema[:, 0])

    return output_extrema
