if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
import pandas as pd

@transformer
def dim_products(df, *args, **kwargs):
    # Group by Product ID to enforce one unique row per product
    dim_products = (
        df.groupby('Product ID')
          .agg({
              'Product Name': 'first',
              'Category': 'first',
              'Sub-Category': 'first'
          })
          .reset_index()
          .rename(columns={
              'Product ID': 'product_id',
              'Product Name': 'product_name',
              'Sub-Category': 'sub_category'
          })
    )
    return dim_products
