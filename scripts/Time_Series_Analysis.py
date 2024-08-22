import pandas as pd
import matplotlib.pyplot as plt


file_path = r'C:\Users\windows 10\Desktop\new\week_0\MoonLight_Energy_Solutions\data\benin-malanville.csv'
df = pd.read_csv(file_path)


df['Timestamp'] = pd.to_datetime(df['Timestamp'])
df.set_index('Timestamp', inplace=True)


plt.figure(figsize=(14, 8))


plt.subplot(2, 2, 1)
plt.plot(df.index, df['GHI'], label='GHI', color='blue')
plt.title('Global Horizontal Irradiance (GHI) over Time')
plt.xlabel('Time')
plt.ylabel('GHI (W/m²)')
plt.grid(True)


plt.subplot(2, 2, 2)
plt.plot(df.index, df['DNI'], label='DNI', color='orange')
plt.title('Direct Normal Irradiance (DNI) over Time')
plt.xlabel('Time')
plt.ylabel('DNI (W/m²)')
plt.grid(True)


plt.subplot(2, 2, 3)
plt.plot(df.index, df['DHI'], label='DHI', color='green')
plt.title('Diffuse Horizontal Irradiance (DHI) over Time')
plt.xlabel('Time')
plt.ylabel('DHI (W/m²)')
plt.grid(True)


plt.subplot(2, 2, 4)
plt.plot(df.index, df['Tamb'], label='Ambient Temperature (Tamb)', color='red')
plt.title('Ambient Temperature (Tamb) over Time')
plt.xlabel('Time')
plt.ylabel('Temperature (°C)')
plt.grid(True)


plt.tight_layout()


plt.show()
