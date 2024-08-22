import pandas as pd
import numpy as np

file_path = r'C:\Users\windows 10\Desktop\new\week_0\MoonLight_Energy_Solutions\data\benin-malanville.csv'
data = pd.read_csv(file_path)

columns_to_analyze = ['GHI', 'DNI', 'DHI', 'WS', 'TModA', 'TModB']

z_scores = (data[columns_to_analyze] - data[columns_to_analyze].mean()) / data[columns_to_analyze].std()

for col in columns_to_analyze:
    data[f'{col}_zscore'] = z_scores[col]

significant_threshold = 3
for col in columns_to_analyze:
    data[f'{col}_outlier'] = np.where(np.abs(data[f'{col}_zscore']) > significant_threshold, True, False)

outliers = data[data[[f'{col}_outlier' for col in columns_to_analyze]].any(axis=1)]
print(outliers)

outliers.to_csv(r'C:\Users\windows 10\Desktop\new\week_0\MoonLight_Energy_Solutions\data\outliers.csv', index=False)
