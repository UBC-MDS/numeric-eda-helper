def get_correlations(input_features, threshold, consider_sign=False):
    """Calculates correlation between all feature pairs in the input data.
    Returns feature pairs having correlation higher than the threshold value.

    Parameters
    ----------
    input_features : pandas.DataFrame
        feature set used for EDA analysis
    threshold : float
        threshold for correlation above which feature pairs will be returned
    consider_sign : boolean (optional)
        determines whether correlation value has to be checked for magnitude
        only or for sign (positive/ negative) also

    Returns
    -------
    pandas.DataFrame
       dataframe containing feature1, feature2, and corresponding correlation.

    Examples
    -------
    >>> get_correlations(X, threshold=0.7)
    """