import numpy as np
import pandas as pd


def calc_cos_sim(input_data, cells):
    """calculate cosine similarity
    :param cells: number of cells
    :type input_data: dva or ica as Pandas DataFrame
    """

    sim = pd.DataFrame(None, index=range(cells), columns=range(cells))

    for index1 in range(cells):
        for index2 in range(cells):
            sim.iat[index1, index2] = np.dot(input_data.iloc[:, index1], input_data.iloc[:, index2]) / (
                np.linalg.norm(input_data.iloc[:, index1]) * np.linalg.norm(input_data.iloc[:, index2]))

    print('Cosine Similarity')
    print(sim)

    return sim
