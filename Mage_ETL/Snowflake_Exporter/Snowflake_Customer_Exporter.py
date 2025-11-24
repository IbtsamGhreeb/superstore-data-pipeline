# gold_layer_export/export_to_snowflake.py

from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.snowflake import Snowflake
from pandas import DataFrame
from os import path

# Ensure data_exporter is imported for Mage
if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_snowflake(df: DataFrame, **kwargs) -> None:
    """
    Export a Gold layer table (e.g., DIM_CUSTOMER) to Snowflake.

    Notes:
    - This function replaces the table if it already exists making a full load.

    Docs: https://docs.mage.ai/design/data-loading#snowflake
    """

    # Target table and database/schema names
    table_name = 'DIM_CUSTOMER'          # Name of the table in Snowflake
    database = 'SNOWFLAKE_LEARNING_DB'   # Your database
    schema = 'PUBLIC'                     # Schema in the database

    # Path to your Mage I/O config file
    config_path = path.join(get_repo_path(), 'io_config.yaml')

    # Profile in the config file (e.g., 'default' or 'dev')
    config_profile = 'default'

    # Open a connection to Snowflake using the config file
    with Snowflake.with_config(ConfigFileLoader(config_path, config_profile)) as loader:
        # Export the DataFrame to Snowflake
        loader.export(
            df,
            table_name,
            database,
            schema,
            if_exists='replace',  #Full_Load
        )

    # Optional: print a confirmation
    print(f"{table_name} exported to Snowflake successfully.")
