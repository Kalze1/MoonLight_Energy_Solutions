import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_distributions(file_path: str):
    # Load the data
    data = pd.read_csv(file_path)

    # Filter data to remove rows with missing values in key columns
    data = data.dropna(subset=['GHI', 'DNI', 'DHI', 'WS', 'TModA', 'TModB'])

    # Create a figure with a specified size
    plt.figure(figsize=(15, 12))

    # Plot Distribution of GHI
    plt.subplot(2, 3, 1)
    sns.histplot(data['GHI'], bins=30, kde=True, color='blue')
    plt.title('Distribution of GHI')
    plt.xlabel('Global Horizontal Irradiance (GHI)')
    plt.ylabel('Frequency')

    # Plot Distribution of DNI
    plt.subplot(2, 3, 2)
    sns.histplot(data['DNI'], bins=30, kde=True, color='green')
    plt.title('Distribution of DNI')
    plt.xlabel('Direct Normal Irradiance (DNI)')
    plt.ylabel('Frequency')

    # Plot Distribution of DHI
    plt.subplot(2, 3, 3)
    sns.histplot(data['DHI'], bins=30, kde=True, color='red')
    plt.title('Distribution of DHI')
    plt.xlabel('Diffuse Horizontal Irradiance (DHI)')
    plt.ylabel('Frequency')

    # Plot Distribution of Wind Speed (WS)
    plt.subplot(2, 3, 4)
    sns.histplot(data['WS'], bins=30, kde=True, color='purple')
    plt.title('Distribution of Wind Speed (WS)')
    plt.xlabel('Wind Speed (m/s)')
    plt.ylabel('Frequency')

    # Plot Distribution of Temperature TModA
    plt.subplot(2, 3, 5)
    sns.histplot(data['TModA'], bins=30, kde=True, color='orange')
    plt.title('Distribution of Temperature TModA')
    plt.xlabel('Temperature TModA (°C)')
    plt.ylabel('Frequency')

    # Plot Distribution of Temperature TModB
    plt.subplot(2, 3, 6)
    sns.histplot(data['TModB'], bins=30, kde=True, color='brown')
    plt.title('Distribution of Temperature TModB')
    plt.xlabel('Temperature TModB (°C)')
    plt.ylabel('Frequency')

    # Adjust layout
    plt.tight_layout()

    # Display the plots
    plt.show()
