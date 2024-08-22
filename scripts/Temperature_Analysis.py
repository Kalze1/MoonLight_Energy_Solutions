import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
file_path = r'C:\Users\windows 10\Desktop\new\week_0\MoonLight_Energy_Solutions\data\benin-malanville.csv'
data = pd.read_csv(file_path)

# Filter data to remove rows with missing values in key columns
data = data.dropna(subset=['RH', 'TModA', 'TModB', 'GHI', 'DNI', 'DHI'])

# Plot the relationship between RH and temperature (TModA and TModB)
plt.figure(figsize=(14, 6))

# Scatter plot for TModA
plt.subplot(1, 2, 1)
sns.scatterplot(x='RH', y='TModA', data=data, hue='GHI', palette='coolwarm', alpha=0.7)
plt.title('Relative Humidity vs TModA')
plt.xlabel('Relative Humidity (%)')
plt.ylabel('Temperature TModA (°C)')
plt.legend(title='GHI', loc='upper right')

# Scatter plot for TModB
plt.subplot(1, 2, 2)
sns.scatterplot(x='RH', y='TModB', data=data, hue='DNI', palette='coolwarm', alpha=0.7)
plt.title('Relative Humidity vs TModB')
plt.xlabel('Relative Humidity (%)')
plt.ylabel('Temperature TModB (°C)')
plt.legend(title='DNI', loc='upper right')

plt.tight_layout()
plt.show()

# Plot the relationship between RH and solar radiation (GHI, DNI, DHI)
plt.figure(figsize=(14, 6))

# Scatter plot for GHI
plt.subplot(1, 3, 1)
sns.scatterplot(x='RH', y='GHI', data=data, hue='TModA', palette='coolwarm', alpha=0.7)
plt.title('Relative Humidity vs GHI')
plt.xlabel('Relative Humidity (%)')
plt.ylabel('Global Horizontal Irradiance (GHI)')
plt.legend(title='TModA', loc='upper right')

# Scatter plot for DNI
plt.subplot(1, 3, 2)
sns.scatterplot(x='RH', y='DNI', data=data, hue='TModB', palette='coolwarm', alpha=0.7)
plt.title('Relative Humidity vs DNI')
plt.xlabel('Relative Humidity (%)')
plt.ylabel('Direct Normal Irradiance (DNI)')
plt.legend(title='TModB', loc='upper right')

# Scatter plot for DHI
plt.subplot(1, 3, 3)
sns.scatterplot(x='RH', y='DHI', data=data, hue='GHI', palette='coolwarm', alpha=0.7)
plt.title('Relative Humidity vs DHI')
plt.xlabel('Relative Humidity (%)')
plt.ylabel('Diffuse Horizontal Irradiance (DHI)')
plt.legend(title='GHI', loc='upper right')

plt.tight_layout()
plt.show()
