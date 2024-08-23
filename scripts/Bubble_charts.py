import pandas as pd
import matplotlib.pyplot as plt

def plot_bubble_chart(file_path: str):
    # Load the data
    data = pd.read_csv(file_path)

    # Drop rows with missing values in the key columns
    data = data.dropna(subset=['GHI', 'Tamb', 'WS', 'RH', 'BP'])

    # Set up the figure
    plt.figure(figsize=(12, 8))

    # Define bubble size based on RH (Relative Humidity)
    bubble_size = data['RH'] * 10

    # Create the bubble chart
    plt.scatter(data['GHI'], data['Tamb'], s=bubble_size, c=data['BP'], cmap='viridis', 
                alpha=0.6, edgecolors="w", linewidth=0.5)

    # Set chart title and labels
    plt.title('Bubble Chart: GHI vs Tamb vs WS with RH as Bubble Size and BP as Color')
    plt.xlabel('Global Horizontal Irradiance (GHI)')
    plt.ylabel('Ambient Temperature (Tamb)')

    # Add color bar representing BP (Barometric Pressure)
    plt.colorbar(label='Barometric Pressure (BP)')

    # Show the plot
    plt.show()


