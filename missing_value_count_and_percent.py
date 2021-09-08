def missing_value_count_and_percent(df):
    """
    Return the number and percent of missing values for each column. 

    Args:
        df (Dataframe): A dataframe with many columns
    
    Return:
        df (Dataframe): A dataframe with one column showing number of missing values, one column showing percentage of missing values with 4 digits
    
    """
    df = pd.concat({'num_missing_values':df.isnull().sum(), 'pct_missing_values':df.isnull().mean().round(4)}, axis=1)
)
    return df