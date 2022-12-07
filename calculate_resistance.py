import numpy as np


def calc_resistance(df, number_cells, capacity_cell):
    """calculate ohmic resistance by R=U/I after discharge pulse and remove pulse afterwards, reset discharge capacity
    :param capacity_cell:   cell capacity in Ah
    :param number_cells:    number of cells
    :type df:               dataframe with raw measurement data
    """

    resistance = []

    # extract indices of pulse
    index = df.index[abs(df.current) > 0.8 * capacity_cell]

    # check if pulse within measurement data
    if not np.any(index):
        return resistance, df

    # extract reference point before pulse and 10ms after pulse
    # sampling with 1000Hz during discharge, works also for 100Hz
    reference_index = index[0] - 1
    start_pulse_time = df.loc[index[0] - 1, 'time']
    measure_ohm_time = start_pulse_time + 0.010
    measure_ohm_index, = df.index[abs(measure_ohm_time - df.time) <= 3e-4]

    # extract pulse current in A
    discharge_current = np.mean(df.loc[index, 'current'])

    # calculate resistance in mOhm for every cell
    for cell in range(1, number_cells + 1):
        delta_voltage = df.loc[reference_index, f'voltage_{cell}'] - df.loc[measure_ohm_index, f'voltage_{cell}']
        resistance.append(delta_voltage / abs(discharge_current) * 1000)

    # set discharge capacity to zero (remove influence of pulse for DVA calculation)
    delta_capacity = df.loc[index[-1], 'Ah']
    df.Ah = abs(df.Ah) - abs(delta_capacity)

    # remove pulse from data
    # makes sure to remove full pulse even though current level has not reached its target for 'clean' DVA
    for counter in range(5):
        index = index.insert(0, index[0] - 1)
    df = df.drop(index)
    df.reset_index(inplace=True, drop=True)

    return resistance, df
