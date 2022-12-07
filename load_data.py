import pandas as pd


def load_dataset(path_to_file, number_cells):
    """Load Dataset and rename columns, from Thomas Kröger, modified
    :param number_cells: number of cells
    :type path_to_file:  path to the txt-datafile
    """

    # read the .txt data
    df = pd.read_csv(path_to_file, sep="\t", header=12, encoding='windows-1252')
    df.drop(['DataSet', 't-Set[h]', 'Time[h]', 'State', 't-Step[h]', 'Cyc-Count',
             'Ah-Step', 'Ah-Set', 'Wh[Wh]', 'T1[°C]', 'Command', 'Line', 'Ah-Charge', 'Ah-Discharge',
             'Ah-Ch-Set', 'Ah-Dis-Set', 'Wh-Step', 'T2[°C]', 'T_12s_PT100_001[°C]', 'T_12s_PT100_002[°C]',
             'T_12s_PT100_003[°C]', 'T_12s_PT100_004[°C]', 'T_12s_PT100_005[°C]', 'T_12s_PT100_006[°C]'],
            axis=1, inplace=True, errors='ignore')

    # rename the columns
    df = df.rename({'~Time[s]': 'time', 'U[V]': 'voltage_strand', 'I[A]': 'current', 'Ah[Ah]': 'Ah'},
                   axis=1, errors='ignore')

    for cell in range(1, number_cells + 1):
        if cell <= 9:
            df = df.rename({f'U_12s_00{cell}[V]': f'voltage_{cell}'}, axis=1, errors='ignore')
        else:
            df = df.rename({f'U_12s_0{cell}[V]': f'voltage_{cell}'}, axis=1, errors='ignore')

    # reset the index
    df.reset_index(inplace=True, drop=True)

    return df
