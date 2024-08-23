import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

def analyze_and_plot_correlation(file_path):
    """
    Reads a CSV file, performs data cleaning, and generates a heatmap and scatter matrix
    for solar radiation and wind conditions.

    Parameters:
    file_path (str): Path to the CSV file.

    Returns:
    None
    """
    try:
        # Read the CSV file
        data = pd.read_csv(file_path)
        
        # Filter out invalid values (GHI, DNI, DHI must be non-negative)
        data = data[(data['GHI'] >= 0) & (data['DNI'] >= 0) & (data['DHI'] >= 0)]

        # Calculate the correlation matrix for solar radiation components and temperature measures
        corr_matrix = data[['GHI', 'DNI', 'DHI', 'TModA', 'TModB']].corr()

        # Plot the correlation matrix using a heatmap
        plt.figure(figsize=(8, 6))
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
        plt.title('Correlation between Solar Radiation Components and Temperature Measures')
        plt.show()

        # Prepare data for scatter matrix (selecting columns related to wind conditions and solar irradiance)
        scatter_matrix_data = data[['GHI', 'DNI', 'DHI', 'WS', 'WSgust', 'WD']]

        # Plot the scatter matrix
        scatter_matrix(scatter_matrix_data, figsize=(12, 12), diagonal='kde')
        plt.suptitle('Scatter Matrix: Wind Conditions and Solar Irradiance')
        plt.show()

    except Exception as e:
        print(f"Error processing the file {file_path}: {e}")

