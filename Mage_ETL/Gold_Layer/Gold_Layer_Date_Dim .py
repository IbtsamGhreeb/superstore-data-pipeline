# gold_layer_dates_dim/dim_dates.py

import pandas as pd

# Ensure transformer is imported for Mage AI
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer

@transformer
def dim_dates(df, *args, **kwargs):
    """
    Create the Dates dimension table (Gold layer).

    Args:
        df (pd.DataFrame): Input Silver layer data

    Returns:
        pd.DataFrame: Dimension table with unique dates and year/month/quarter/day columns
    """
    # Check if 'Order Date' exists in the input DataFrame
    if 'Order Date' not in df.columns:
        raise ValueError("Input DataFrame is missing 'Order Date' column.")

    # Convert 'Order Date' to datetime and drop duplicates
    dates = pd.to_datetime(df['Order Date'], errors='coerce').drop_duplicates()

    # Build the Dates dimension table
    dim_dates = pd.DataFrame({
        'order_date': dates,
        'year': dates.dt.year,
        'month': dates.dt.month,
        'quarter': dates.dt.quarter,
        'day': dates.dt.day
    }).reset_index(drop=True)

    return dim_dates
