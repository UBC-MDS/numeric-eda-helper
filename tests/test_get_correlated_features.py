from numeric_edahelper.get_correlated_features import get_correlated_features
import pandas as pd
import pytest

def test_get_correlated_features():
    """
    Test the correct input, output and exeption handling for get_correlated_features() function
    """
    test_df = pd.DataFrame({"age": [23, 13, 7, 45], 
                  "height": [1.65, 1.23, 0.96, 1.55],
                  "income": [20, 120, 120, 25]})

    response = get_correlated_features(test_df, threshold=0.1)
    
    # Assert statements
    assert len(response) == 6, "Output should return 6 rows!"
    assert response.iloc[0]['correlation'] == 0.75, "Correlation between age and height should be 0.75"
    assert type(response) == pd.DataFrame, "The returned output datatype should be a pandas dataframe"

    # Raise specific type errors
    with pytest.raises(TypeError):
        get_correlated_features(['32', '45', 'a'])
    with pytest.raises(TypeError):
        get_correlated_features(test_df, threshold='a')