import pandas as pd
import numpy as np

# Load the data
file_path = r'C:\Users\windows 10\Desktop\new\week_0\MoonLight_Energy_Solutions\data\benin-malanville.csv'
data = pd.read_csv(file_path)

# List of columns for which to calculate Z-scores
columns_to_analyze = ['GHI', 'DNI', 'DHI', 'WS', 'TModA', 'TModB']

# Calculate Z-scores for the selected columns
z_scores = (data[columns_to_analyze] - data[columns_to_analyze].mean()) / data[columns_to_analyze].std()

# Add Z-scores to the original DataFrame
for col in columns_to_analyze:
    data[f'{col}_zscore'] = z_scores[col]

# Flag data points with Z-scores that are significantly different from the mean
# Typically, Z-scores > 3 or < -3 are considered significant
significant_threshold = 3
for col in columns_to_analyze:
    data[f'{col}_outlier'] = np.where(np.abs(data[f'{col}_zscore']) > significant_threshold, True, False)

# Display the flagged data points
outliers = data[data[[f'{col}_outlier' for col in columns_to_analyze]].any(axis=1)]
print(outliers)

# Optionally, save the results to a new CSV file
outliers.to_csv(r'C:\Users\windows 10\Desktop\new\week_0\MoonLight_Energy_Solutions\data\outliers.csv', index=False)
