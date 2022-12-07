

def cut_signal(df, capacity):
    """cuts all signals within DataFrame df at specified discharge capacity (in Ah)"""

    df.drop(df.index[df.Ah >= capacity], inplace=True)

    return df
