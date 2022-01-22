from numeric_edahelper.overview import overview
import pandas as pd
import numpy as np
import pytest

def test_overview():
    """Test the correct outputs of overview using various inputs.
    """
    np.random.seed(42)
    df = pd.DataFrame({'col1': np.random.randint(0,100,100),
                       'col2': np.random.randint(0,200,100),
                       'col3': np.random.randint(0,400,100)})
    test1 = overview(df, quiet=False)
    test2 = overview(df, quiet=True)

    # Assert statements
    assert test1.columns == df.columns, "Output column names should match input column names"
    assert len(overview(pd.DataFrame([0]))) == 4, "Output should return 4 rows for any length dataframe input"
    assert round(sum(test1['col1'])) == 990, "Values for column #1 are incorrect"
    assert 'mean_' in globals(), "Global variables not created"
    assert round(sum(mean_)) == 353, ""

    # Testing raises
    with pytest.raises(TypeError):
        overview(np.array9[0,2,3,1])

    with pytest.raises(TypeError):
        overview(df, quiet='true')
        overview(df, quiet=2)
    
    #create non numeric data
    df_nn = pd.DataFrame(['one','two',3])
    with pytest.raises(ValueError):
        overview(df_nn)