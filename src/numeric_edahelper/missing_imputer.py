import pandas as pd
import numpy as np


def missing_imputer(data, method="mean"):

    """
    Impute the missing values using the method selected
    Parameters
    ----------
    data : pandas.DataFrame
        A Pandas Dataframe for which the missing values need to be replaced or dropped
    method : str, default = "mean"
        The method used for imputing numerical missing values
        Options: "drop", "mean", "median"
    
    Returns
    -------
    pandas.DataFrame
        An imputed dataframe
    Examples
    --------
    >>> missing_imputer(df, method="median")
    """