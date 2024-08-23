import pandas as pd
import numpy as np

def detect_and_save_outliers(file_path: str, output_path: str, columns_to_analyze: list, significant_threshold: float = 3):
    # Load the data
    data = pd.read_csv(file_path)

    # Calculate z-scores for the specified columns
    z_scores = (data[columns_to_analyze] - data[columns_to_analyze].mean()) / data[columns_to_analyze].std()

    # Add z-scores to the data
    for col in columns_to_analyze:
        data[f'{col}_zscore'] = z_scores[col]

    # Identify outliers based on the significant threshold
    for col in columns_to_analyze:
        data[f'{col}_outlier'] = np.where(np.abs(data[f'{col}_zscore']) > significant_threshold, True, False)

    # Extract rows with any outliers
    outliers = data[data[[f'{col}_outlier' for col in columns_to_analyze]].any(axis=1)]
    
    # Print outliers
    print(outliers)

    # Save outliers to a CSV file
    outliers.to_csv(output_path, index=False)


