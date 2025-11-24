if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
import pandas as pd

@transformer
def fact_sales(df, *args, **kwargs):
    fact_cols = [
        'Order ID', 'Order Date', 'Ship Date', 'Ship Mode',
        'Customer ID', 'Product ID', 
        'Sales', 'Quantity', 'Discount', 'Profit'
    ]
    existing = [c for c in fact_cols if c in df.columns]

    fact_sales = (
        df[existing]
        .copy()
        .rename(columns={
            'Order ID': 'order_id',
            'Order Date': 'order_date',
            'Ship Date': 'ship_date',
            'Ship Mode': 'ship_mode',
            'Customer ID': 'customer_id',
            'Product ID': 'product_id'
        })
    )

    return fact_sales
