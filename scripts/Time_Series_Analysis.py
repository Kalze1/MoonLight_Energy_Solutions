import pandas as pd
import matplotlib.pyplot as plt

def plot_solar_data(file_path):
    """
    Reads a CSV file and generates a 2x2 plot of solar data over time.
    
    Parameters:
    file_path (str): Path to the CSV file.
    
    Returns:
    None
    """
    try:
        # Read the CSV file
        df = pd.read_csv(file_path)
        
        # Convert the 'Timestamp' column to datetime and set it as the index
        df['Timestamp'] = pd.to_datetime(df['Timestamp'])
        df.set_index('Timestamp', inplace=True)

        # Plot the data
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

        # Show the plots
        plt.show()

    except Exception as e:
        print(f"Error processing the file {file_path}: {e}")
