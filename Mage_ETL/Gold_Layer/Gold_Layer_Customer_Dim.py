@transformer
def dim_customers(df, *args, **kwargs):
    # group by customer_id to ensure true uniqueness
    dim_customers = (
        df.groupby('Customer ID')  # Group all rows with the same Customer ID
          .agg({
              'Customer Name': 'first',  # Take the first occurrence of the name
              'Segment': 'first',        # Take the first segment value
              'Region': 'first',         # Take the first region value
              'City': 'first',           # Take the first city value
              'State': 'first',          # Take the first state value
          })
          .reset_index()  # Convert 'Customer ID' from index back to a column
          .rename(columns={
              'Customer ID': 'customer_id',        # Standardize column name
              'Customer Name': 'customer_name'     # Standardize column name
          })
    )
    return dim_customers
