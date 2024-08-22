import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


file_path = r'C:\Users\windows 10\Desktop\new\week_0\MoonLight_Energy_Solutions\data\benin-malanville.csv'
data = pd.read_csv(file_path)


data = data.dropna(subset=['WS', 'WD', 'WSstdev', 'WDstdev'])

data['WD_rad'] = np.deg2rad(data['WD'])

plt.figure(figsize=(10, 8))
ax = plt.subplot(111, polar=True)
ax.set_theta_direction(-1)  
ax.set_theta_offset(np.pi / 2)  
sc = ax.scatter(data['WD_rad'], data['WS'], c=data['WSstdev'], cmap='viridis', alpha=0.75)
plt.colorbar(sc, label='Wind Speed StdDev (WSstdev)')

plt.title('Wind Speed and Direction Distribution')
ax.set_xlabel('Wind Direction (Degrees)')
ax.set_ylabel('Wind Speed (m/s)')

ax.errorbar(data['WD_rad'], data['WS'], yerr=data['WDstdev'], fmt='o', color='black', alpha=0.3, capsize=2)

plt.show()
