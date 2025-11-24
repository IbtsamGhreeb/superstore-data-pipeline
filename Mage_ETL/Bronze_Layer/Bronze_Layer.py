"""
Bronze Layer Loader for Superstore Dataset
------------------------------------------
Loads the raw CSV from a ZIP file into a Pandas DataFrame.
Compatible with both Mage Cloud and local Docker.
"""

import zipfile
import pandas as pd

# Ensure compatibility with Mage Cloud or local environment
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

# Path to your ZIP file (update as needed)
ZIP_PATH = '/home/src/Data/Superstore.zip'


@data_loader
def load_bronze_data(*args, **kwargs):
    """
    Load the raw CSV from a ZIP file (Bronze layer).
    Returns:
        pd.DataFrame: Raw Superstore data
    """
    # Open the ZIP file
    with zipfile.ZipFile(ZIP_PATH, 'r') as z:
        # Find all CSV files
        csv_files = [f for f in z.namelist() if f.endswith('.csv')]
        if not csv_files:
            raise ValueError("No CSV found inside ZIP.")

        # Take the first CSV file
        csv_name = csv_files[0]

        # Load CSV into a DataFrame
        with z.open(csv_name) as f:
            df = pd.read_csv(f, encoding='latin1')

    return df


@test
def test_bronze_output(output, *args) -> None:
    """
    Simple tests for Bronze layer output.
    Ensures the DataFrame is not empty or None.
    """
    assert output is not None, "Bronze layer output is undefined"
    assert not output.empty, "CSV inside ZIP is empty"
