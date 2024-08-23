import pandas as pd
import numpy as np

def data_quality_analysis(file_path):
    """
    Analyzes the data quality of a CSV file by detecting missing values, invalid (negative) values,
    and outliers using the IQR method.
    
    Parameters:
    file_path (str): Path to the CSV file.

    Returns:
    dict: A dictionary containing missing values, invalid values, and outliers for the dataset.
    """
    try:
        # Read the CSV file
        df = pd.read_csv(file_path)

        # Detect missing values
        missing_values = df.isnull().sum()

        # Detect invalid (negative) values in GHI, DNI, and DHI columns
        invalid_values = {
            'GHI': (df['GHI'] < 0).sum(),
            'DNI': (df['DNI'] < 0).sum(),
            'DHI': (df['DHI'] < 0).sum(),
        }

        # Function to detect outliers using the IQR method
        def detect_outliers_iqr(data):
            Q1 = np.percentile(data.dropna(), 25)  # Ignore NaN values
            Q3 = np.percentile(data.dropna(), 75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            outliers = ((data < lower_bound) | (data > upper_bound)).sum()
            return outliers

        # Detect outliers in specific columns
        outliers = {
            'ModA': detect_outliers_iqr(df['ModA']),
            'ModB': detect_outliers_iqr(df['ModB']),
            'WS': detect_outliers_iqr(df['WS']),
            'WSgust': detect_outliers_iqr(df['WSgust'])
        }

        # Combine results into a single dictionary
        results = {
            'missing_values': missing_values,
            'invalid_values': invalid_values,
            'outliers': outliers
        }

        return results

    except Exception as e:
        print(f"Error processing the file {file_path}: {e}")
        return None
