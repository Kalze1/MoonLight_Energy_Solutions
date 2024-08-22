import pandas as pd

file_path = r'C:\Users\windows 10\Desktop\new\week_0\MoonLight_Energy_Solutions\data\benin-malanville.csv'
data = pd.read_csv(file_path)

data = data.dropna(axis=1, how='all')

data.interpolate(method='linear', inplace=True)

data.dropna(inplace=True)

data = data[(data['GHI'] >= 0) & (data['DNI'] >= 0) & (data['DHI'] >= 0)]

data.reset_index(drop=True, inplace=True)

print(data.head())

cleaned_file_path = r'C:\Users\windows 10\Desktop\new\week_0\MoonLight_Energy_Solutions\data\cleaned_benin-malanville.csv'
data.to_csv(cleaned_file_path, index=False)
