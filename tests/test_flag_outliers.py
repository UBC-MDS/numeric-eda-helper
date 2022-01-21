from numeric_edahelper.flag_outliers import flag_outliers
import pandas as pd
import pytest

def test_flag_outliers():
    """
    Test the correct output of variables containing outliers from given df  
    """
    df = pd.DataFrame({'col1': [-100,-200, 1,2,3,4,5,6,7,8,9,10, 1000],
                    'col2': [1,2,3,4,5,6,7,8,9,10,11,12,13],
                    'col3': [-50, 1,2,3,4,5,6,7,8,9,10,11,50000]})
    output1 = flag_outliers(df, threshold=0.1)

    # Assert statements 
    assert len(output1) == 2, "Output should return 2 variables!"
    assert flag_outliers(df, 1.0) == {}, "Output should return an empty dictionary"
    assert output1 == {'col1': 0.23076923076923078, 'col3': 0.15384615384615385}, "Output is incorrect"
    assert type(output1) == dict, "The returned output datatype should be a dictionary"

    # Raise specific type errors
    with pytest.raises(TypeError):
        flag_outliers(12345)
    with pytest.raises(TypeError):
        flag_outliers(df, threshold=2)