import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plot_wind_distribution(file_path):
    """
    Plots a polar scatter plot of wind speed and direction distribution with standard deviation.

    Parameters:
    file_path (str): Path to the CSV file.

    Returns:
    None
    """
    try:
        # Read the CSV file
        data = pd.read_csv(file_path)

        # Drop rows with missing values in the relevant columns
        data = data.dropna(subset=['WS', 'WD', 'WSstdev', 'WDstdev'])

        # Convert wind direction from degrees to radians for the polar plot
        data['WD_rad'] = np.deg2rad(data['WD'])

        # Create the polar scatter plot
        plt.figure(figsize=(10, 8))
        ax = plt.subplot(111, polar=True)
        ax.set_theta_direction(-1)  # Set the direction to clockwise
        ax.set_theta_offset(np.pi / 2)  # Set zero degrees to the top

        # Scatter plot with color mapped to wind speed standard deviation
        sc = ax.scatter(data['WD_rad'], data['WS'], c=data['WSstdev'], cmap='viridis', alpha=0.75)
        plt.colorbar(sc, label='Wind Speed StdDev (WSstdev)')

        # Set the title and labels
        plt.title('Wind Speed and Direction Distribution')
        ax.set_xlabel('Wind Direction (Degrees)')
        ax.set_ylabel('Wind Speed (m/s)')

        # Plot error bars representing the standard deviation of wind direction
        ax.errorbar(data['WD_rad'], data['WS'], yerr=data['WDstdev'], fmt='o', color='black', alpha=0.3, capsize=2)

        # Show the plot
        plt.show()

    except Exception as e:
        print(f"Error processing the file {file_path}: {e}")

