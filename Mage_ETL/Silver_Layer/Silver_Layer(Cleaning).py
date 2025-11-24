if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
import pandas as pd

@transformer
def clean_data(df, *args, **kwargs):
    """
    Silver layer: Clean and standardize raw CSV data for the new dataset.
    """

    # 1️⃣ Remove unnecessary columns
    # Drop Row ID and Country since they are either redundant or same value
    df = df.drop(['Unnamed: 0','Row ID', 'Country'], axis=1, errors='ignore')

    # 2️⃣ Drop duplicate rows
    df = df.drop_duplicates().reset_index(drop=True)

    # 3️⃣ Fix date columns
    for date_col in ['Order Date', 'Ship Date']:
        if date_col in df.columns:
            df[date_col] = pd.to_datetime(df[date_col], errors='coerce')

    # 4️⃣ Convert numeric columns
    for num_col in ['Sales', 'Quantity', 'Profit', 'Discount']:
        if num_col in df.columns:
            df[num_col] = pd.to_numeric(df[num_col], errors='coerce')

    # 5️⃣ Trim string columns
    for str_col in ['Customer ID', 'Product ID', 'Ship Mode', 'Region']:
        if str_col in df.columns:
            df[str_col] = df[str_col].astype(str).str.strip()

    # 6️⃣ Drop rows where key fields are missing
    key_fields = ['Order ID', 'Customer ID', 'Product ID', 'Order Date']
    df = df.dropna(subset=[col for col in key_fields if col in df.columns])

    return df
