def overview(input, verbose=False, quiet=False):
    """Gives a statistical overview of the input data.
    Returns a `pandas.DataFrame` of descriptive statistical values.
    
    Parameters
    ----------
    input : `pandas.DataFrame` or `np.array`
        Input data to be summarized.
    verbose : `bool`
        Boolean value corresponding to showing additional
        information (histogram, estimated distribution).
    quiet : `bool`
        Boolean value corresponding to showing output of 
        the function. Used for acquiring variables.
        
    Returns
    -------
    `pandas.DataFrame`
        DataFrame holding all calculated values.

    Examples
    --------
    >>> overview(dataframe, verbose=True, quiet=False)
    """