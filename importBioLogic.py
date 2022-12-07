import pandas as pd


def load_dataset_txt(path_to_file, number_cells):
    """
    load data from BioLogic measurement (converted to .txt within EC-Lab)
    in case of errors check number of header lines
    :type number_cells:     number of cells
    :type path_to_file:     path to BioLogic file (.txt)
    """

    # TODO: check number of header lines
    df = pd.read_csv(path_to_file, sep="\t", header=91, encoding='windows-1252')

    # rename the columns
    df = df.rename({'time/s': 'time', 'Estack/V': 'voltage_strand', 'I/mA': 'current', '(Q-Qo)/mA.h': 'Ah'},
                   axis=1, errors='ignore')

    for cell in range(1, number_cells + 1):
        df = df.rename({f'E{cell}/V': f'voltage_{cell}'}, axis=1, errors='ignore')

    # reset the index
    df.reset_index(inplace=True, drop=True)

    # replace commas with points and save data as float
    # convert current and discharge capacity (named Ah) from mAh to Ah
    df['time'] = df['time'].str.replace(',', '.').astype(float)
    df['voltage_strand'] = df['voltage_strand'].str.replace(',', '.').astype(float)
    df['current'] = df['current'].str.replace(',', '.').astype(float) / 1000
    df['Ah'] = df['Ah'].str.replace(',', '.').astype(float) / 1000

    for cell in range(1, number_cells + 1):
        df[f'voltage_{cell}'] = df[f'voltage_{cell}'].str.replace(',', '.').astype(float)

    return df
