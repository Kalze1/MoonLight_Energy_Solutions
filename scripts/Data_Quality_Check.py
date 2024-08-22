import pandas as pd
import numpy as np


file_path = r'C:\Users\windows 10\Desktop\new\week_0\MoonLight_Energy_Solutions\data\benin-malanville.csv'
df = pd.read_csv(file_path)


missing_values = df.isnull().sum()


invalid_values = {
    'GHI': (df['GHI'] < 0).sum(),
    'DNI': (df['DNI'] < 0).sum(),
    'DHI': (df['DHI'] < 0).sum(),
}


def detect_outliers_iqr(data):
    Q1 = np.percentile(data, 25)
    Q3 = np.percentile(data, 75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = ((data < lower_bound) | (data > upper_bound)).sum()
    return outliers

outliers = {
    'ModA': detect_outliers_iqr(df['ModA']),
    'ModB': detect_outliers_iqr(df['ModB']),
    'WS': detect_outliers_iqr(df['WS']),
    'WSgust': detect_outliers_iqr(df['WSgust'])
}


print("Missing Values:")
print(missing_values)
print("\nInvalid (Negative) Values:")
print(invalid_values)
print("\nOutliers Detected:")
print(outliers)
