import pandas as pd
from scipy.signal import savgol_filter
import matplotlib.pyplot as plt
from scipy import interpolate


def calc_dva(data, remaining_cells):
    """calculates differential voltage analysis for every cell
    :type data:             smoothed signals, cropped to DVA
    :param remaining_cells: list of all remaining cells
    """

    dva = pd.DataFrame(None)

    # compute capacity difference quotient
    Ah_step_length = 0.02
    delta_Ah = max(data.Ah) * Ah_step_length

    # split dataset
    split = round(Ah_step_length/2 * len(data.index))

    # calculate window size (30% smaller than ws for voltage smoothing)
    ws_factor = 0.04 * len(data.index)
    ws_full = round((ws_factor - 1) / 2) * 2 + 1
    ws = round((0.7 * ws_full) / 2) * 2 + 1

    # calculate DVA
    for cell in remaining_cells:

        ocv = data.loc[:, f'voltage_{cell}_smooth']

        ocv_shift_forward = \
            interpolate.interp1d(data.Ah, data.loc[:, f'voltage_{cell}_smooth'],
                                 'linear', bounds_error=False, fill_value="extrapolate")(data.Ah + delta_Ah)
        ocv_shift_reverse = \
            interpolate.interp1d(data.Ah, data.loc[:, f'voltage_{cell}_smooth'],
                                 'linear', bounds_error=False, fill_value="extrapolate")(data.Ah - delta_Ah)

        dva_forward = (ocv_shift_forward - ocv) / delta_Ah * (-1) * max(data.Ah)
        dva_reverse = -(ocv_shift_reverse - ocv) / delta_Ah * (-1) * max(data.Ah)

        dva_full = pd.concat([pd.Series(dva_reverse[split:2*split]),
                              pd.Series(dva_forward[0:len(data.index)-split])])

        dva_full_smooth = savgol_filter(dva_full, ws, 2)

        dva.loc[:, f'cell_{cell}'] = dva_full_smooth

    # reset the index
    dva.reset_index(inplace=True, drop=True)

    return dva
