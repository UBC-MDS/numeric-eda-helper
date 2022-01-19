
def flag_outliers(df, threshold):
    """Highlights and presents numeric variables (columns) in a dataframe for EDA
    which contain a high percentage 
    of outliers as defined by IQR in statistics

    Parameters
    ----------
    df : pandas.DataFrame
        dataset used for EDA analysis
    threshold : float (optional)
        minimum percentage threshold for the proportion of outliers, above which will have variables flagged

    Returns
    -------
    dict
       a dictionary containing the name of variables with high outliers and its respective percentage of outliers 
    
    Examples
    -------
    >>> flag_outliers(df, threshold=0.2)
    """