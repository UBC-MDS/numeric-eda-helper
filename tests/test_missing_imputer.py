from numeric_edahelper.missing_imputer import missing_imputer
from pandas._testing import assert_frame_equal
import pandas as pd
import numpy as np
import pytest

def test_missing_imputer():
    """
    Test the correct output of pandas.DataFrame with missing values correspond to different methods(drop,mean,median)
    """
    df = pd.DataFrame({'col1': [1,2,3,4,5,6,np.nan,14],
                    'col2': [-10,-9,-8,-7,np.nan,-5,-4,1],
                    'col3': [np.nan,0.1,0.2,np.nan,0.3,np.nan,0.4,0.05],
                    'col4': [-100,-1000,-10000,2,4,6,8,10]})

    # Test with default arguments(method = "mean")
    expected_mean = pd.DataFrame({'col1': [1,2,3,4,5,6,5,14],
                    'col2': [-10,-9,-8,-7,-6,-5,-4,1],
                    'col3': [0.21,0.1,0.2,0.21,0.3,0.21,0.4,0.05],
                    'col4': [-100,-1000,-10000,2,4,6,8,10]}).reset_index(drop=True)

    actual_mean = missing_imputer(df)

    assert_frame_equal(actual_mean, expected_mean, check_dtype=False)

    # Test with arguments(method = "median")
    expected_median = pd.DataFrame({'col1': [1,2,3,4,5,6,4,14],
                    'col2': [-10,-9,-8,-7,-7,-5,-4,1],
                    'col3': [0.2,0.1,0.2,0.2,0.3,0.2,0.4,0.05],
                    'col4': [-100,-1000,-10000,2,4,6,8,10]}).reset_index(drop=True)

    actual_median = missing_imputer(df,method="median")

    assert_frame_equal(actual_median, expected_median, check_dtype=False)

    # Test with arguments(method = "drop")
    expected_drop = pd.DataFrame({'col1': [2,3,14],
                    'col2': [-9,-8,1],
                    'col3': [0.1,0.2,0.05],
                    'col4': [-1000,-10000,10]}).reset_index(drop=True)

    actual_drop = missing_imputer(df,method="drop")

    assert_frame_equal(actual_drop, expected_drop, check_dtype=False)

    # Test whether wrong input data type raises TypeError
    with pytest.raises(TypeError):
        missing_imputer([1,2,3])

    # Test whether non-numeric input of data raises TypeError
    non_numeric = pd.DataFrame({'col1': ['1',2,3,4,5,6,np.nan,14],
                    'col2': [-100,-1000,-10000,2,4,6,8,10]})
    with pytest.raises(TypeError):
        missing_imputer(non_numeric)

    # Test whether invaild input of method raises ValueError
    data_1 = pd.DataFrame({'a':[1,2,3],'b':[0,1,0]})
    with pytest.raises(ValueError):
        missing_imputer(data_1, method="med")
    