import pandas as pd
from scipy.signal import savgol_filter


def prep_signals(df, number_cells, capacity_cell):
    """preprocess signal: extract DVA interval and smooth signals
    :param capacity_cell:   capacity of used cells in Ah
    :param df:              contains raw measurement data
    :param number_cells:    number of cells
    """

    data = pd.DataFrame(None)

    # extract indices of DVA (optional pulse removed in calc_resistance)
    index = df.index[abs(df.current) > 0.035 * capacity_cell]

    # extract signals
    data.loc[:, 'time'] = pd.Series(df.time[index])
    data.loc[:, 'current'] = pd.Series(df.current[index])
    data.loc[:, 'Ah'] = pd.Series(abs(df.Ah[index]))
    for cell in range(1, number_cells + 1):
        data.loc[:, f'voltage_{cell}'] = pd.Series(df.loc[index, f'voltage_{cell}'])

    # reset the index
    data.reset_index(inplace=True, drop=True)

    # calculate window size (odd value)
    ws_factor = 0.04 * (index[-1] - index[0])
    ws = round((ws_factor - 1) / 2) * 2 + 1

    # smooth current and voltages
    data.loc[:, 'current_smooth'] = pd.Series(savgol_filter(data.loc[:, 'current'], ws, 2))
    for cell in range(1, number_cells + 1):
        data.loc[:, f'voltage_{cell}_smooth'] = pd.Series(savgol_filter(data.loc[:, f'voltage_{cell}'], ws, 2))

    # smoothing of Ah not necessary

    # remove unfiltered signals
    data.drop(['current'], axis=1, inplace=True, errors='ignore')
    for cell in range(1, number_cells + 1):
        data.drop(f'voltage_{cell}', axis=1, inplace=True, errors='ignore')

    return data
