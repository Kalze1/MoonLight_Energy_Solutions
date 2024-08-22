import pandas as pd
import matplotlib.pyplot as plt

file_path = r'C:\Users\windows 10\Desktop\new\week_0\MoonLight_Energy_Solutions\data\benin-malanville.csv'
data = pd.read_csv(file_path)

data = data.dropna(subset=['GHI', 'Tamb', 'WS', 'RH', 'BP'])

plt.figure(figsize=(12, 8))

bubble_size = data['RH'] * 10  
plt.scatter(data['GHI'], data['Tamb'], s=bubble_size, c=data['BP'], cmap='viridis', alpha=0.6, edgecolors="w", linewidth=0.5)

plt.title('Bubble Chart: GHI vs Tamb vs WS with RH as Bubble Size and BP as Color')
plt.xlabel('Global Horizontal Irradiance (GHI)')
plt.ylabel('Ambient Temperature (Tamb)')

plt.colorbar(label='Barometric Pressure (BP)')

plt.show()
