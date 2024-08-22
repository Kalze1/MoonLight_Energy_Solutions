import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix


file_path = r'C:\Users\windows 10\Desktop\new\week_0\MoonLight_Energy_Solutions\data\benin-malanville.csv'
data = pd.read_csv(file_path)

data = data[(data['GHI'] >= 0) & (data['DNI'] >= 0) & (data['DHI'] >= 0)]

corr_matrix = data[['GHI', 'DNI', 'DHI', 'TModA', 'TModB']].corr()

plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation between Solar Radiation Components and Temperature Measures')
plt.show()

scatter_matrix_data = data[['GHI', 'DNI', 'DHI', 'WS', 'WSgust', 'WD']]

scatter_matrix(scatter_matrix_data, figsize=(12, 12), diagonal='kde')
plt.suptitle('Scatter Matrix: Wind Conditions and Solar Irradiance')
plt.show()
