

def remove_cells(data, cells_to_remove, number_cells):
    """removes cells from data, returns remaining number of cells and list with remaining cells
    :param number_cells:    number of all cells (inclusive the ones to be removed)
    :param cells_to_remove: list with integer cell numbers, between 1 and number_cells
    :type data:             DataFrame with measurement data
    """

    all_cells = [*range(1, number_cells + 1)]

    if max(cells_to_remove) > number_cells:
        raise IOError('Only cells within the range [1, number_cells] can be removed!')
    elif min(cells_to_remove) < 1:
        raise IOError('Use positive integers greater than 0 to address cells!')

    for cell in cells_to_remove:
        number_cells -= 1
        data.drop([f'voltage_{cell}_smooth'], axis=1, inplace=True, errors='ignore')

    remaining_cells = [cell for cell in all_cells if cell not in cells_to_remove]

    return data, number_cells, remaining_cells
