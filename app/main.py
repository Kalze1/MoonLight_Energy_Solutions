import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import zscore

def load_data(dataset_choice):
    if dataset_choice == "Dataset 1":
        file_path = r"data/benin-malanville.csv"
    elif dataset_choice == "Dataset 2":
        file_path = r"data/sierraleone-bumbuna.csv"
    elif dataset_choice == "Dataset 3":
        file_path = r"data/togo-dapaong_qc.csv"
    
    df = pd.read_csv(file_path)
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    return df




# Function to plot wind analysis using polar plots
def plot_wind_polar(df):
    # Filter out any rows with invalid or missing wind speed and direction data
    df = df.dropna(subset=['WS', 'WD', 'WSstdev', 'WDstdev'])

    # Convert wind direction from degrees to radians for polar plot
    df['WD_rad'] = np.deg2rad(df['WD'])

    # Polar plot for wind direction and speed
    plt.figure(figsize=(10, 8))
    ax = plt.subplot(111, polar=True)
    ax.set_theta_direction(-1)  # Set direction of the plot
    ax.set_theta_offset(np.pi / 2)  # Set offset so 0° is at the top

    # Plotting the wind speed as a function of wind direction
    sc = ax.scatter(df['WD_rad'], df['WS'], c=df['WSstdev'], cmap='viridis', alpha=0.75)
    plt.colorbar(sc, label='Wind Speed StdDev (WSstdev)')

    # Add labels and title
    plt.title('Wind Speed and Direction Distribution')
    plt.show()
    st.pyplot(plt)


def perform_summary_statistics(df):
    summary_stats = df.describe()
    st.write("Summary Statistics:")
    st.dataframe(summary_stats)

def perform_data_quality_check(df):
    missing_values = df.isnull().sum()
    st.write("Missing Values:")
    st.dataframe(missing_values)

    ghi_outliers = df[(df['GHI'] > 1000) | (df['GHI'] < 0)]
    dni_outliers = df[(df['DNI'] > 1000) | (df['DNI'] < 0)]
    dhi_outliers = df[(df['DHI'] > 500) | (df['DHI'] < 0)]

    st.write("Outliers:")
    st.dataframe(ghi_outliers)
    st.dataframe(dni_outliers)
    st.dataframe(dhi_outliers)

def plot_histograms(df):
    df = df.dropna(subset=['GHI', 'DNI', 'DHI', 'WS', 'TModA', 'TModB'])

    plt.figure(figsize=(15, 12))

    plt.subplot(2, 3, 1)
    sns.histplot(df['GHI'], bins=30, kde=True, color='blue')
    plt.title('Distribution of GHI')
    plt.xlabel('Global Horizontal Irradiance (GHI)')
    plt.ylabel('Frequency')

    plt.subplot(2, 3, 2)
    sns.histplot(df['DNI'], bins=30, kde=True, color='green')
    plt.title('Distribution of DNI')
    plt.xlabel('Direct Normal Irradiance (DNI)')
    plt.ylabel('Frequency')

    plt.subplot(2, 3, 3)
    sns.histplot(df['DHI'], bins=30, kde=True, color='red')
    plt.title('Distribution of DHI')
    plt.xlabel('Diffuse Horizontal Irradiance (DHI)')
    plt.ylabel('Frequency')

    plt.subplot(2, 3, 4)
    sns.histplot(df['WS'], bins=30, kde=True, color='purple')
    plt.title('Distribution of Wind Speed (WS)')
    plt.xlabel('Wind Speed (m/s)')
    plt.ylabel('Frequency')

    plt.subplot(2, 3, 5)
    sns.histplot(df['TModA'], bins=30, kde=True, color='orange')
    plt.title('Distribution of Temperature TModA')
    plt.xlabel('Temperature TModA (°C)')
    plt.ylabel('Frequency')

    plt.subplot(2, 3, 6)
    sns.histplot(df['TModB'], bins=30, kde=True, color='brown')
    plt.title('Distribution of Temperature TModB')
    plt.xlabel('Temperature TModB (°C)')
    plt.ylabel('Frequency')

    plt.tight_layout()
    st.pyplot(plt)


# Function to plot correlation heatmap
def plot_correlation_heatmap(df):
    # Filter and calculate correlation
    df = df[(df['GHI'] >= 0) & (df['DNI'] >= 0) & (df['DHI'] >= 0)]
    corr_matrix = df[['GHI', 'DNI', 'DHI', 'TModA', 'TModB']].corr()

    # Plot heatmap
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
    plt.title('Correlation between Solar Radiation Components and Temperature Measures')
    st.pyplot(plt)


# Function to plot scatter matrix
def plot_scatter_matrix(df):
    scatter_matrix_data = df[['GHI', 'DNI', 'DHI', 'WS', 'WSgust', 'WD']]
    
    plt.figure(figsize=(12, 12))
    scatter_matrix(scatter_matrix_data, figsize=(12, 12), diagonal='kde')
    plt.suptitle('Scatter Matrix: Wind Conditions and Solar Irradiance')
    st.pyplot(plt)


# Function for Temperature Analysis
def plot_temperature_analysis(df):
    # Filter data to ensure no missing values in key columns
    df = df.dropna(subset=['RH', 'TModA', 'TModB', 'GHI', 'DNI', 'DHI'])

    # Plot the relationship between RH and temperature (TModA and TModB)
    plt.figure(figsize=(14, 6))

    # Scatter plot for TModA vs RH
    plt.subplot(1, 2, 1)
    sns.scatterplot(x='RH', y='TModA', data=df, hue='GHI', palette='coolwarm', alpha=0.7)
    plt.title('Relative Humidity vs TModA with GHI Hue')
    plt.xlabel('Relative Humidity (%)')
    plt.ylabel('Temperature TModA (°C)')
    plt.legend(title='GHI', loc='upper right')

    # Scatter plot for TModB vs RH
    plt.subplot(1, 2, 2)
    sns.scatterplot(x='RH', y='TModB', data=df, hue='DNI', palette='coolwarm', alpha=0.7)
    plt.title('Relative Humidity vs TModB with DNI Hue')
    plt.xlabel('Relative Humidity (%)')
    plt.ylabel('Temperature TModB (°C)')
    plt.legend(title='DNI', loc='upper right')

    plt.tight_layout()
    st.pyplot(plt)

    # Plot the relationship between RH and solar radiation (GHI, DNI, DHI)
    plt.figure(figsize=(14, 6))

    # Scatter plot for GHI vs RH
    plt.subplot(1, 3, 1)
    sns.scatterplot(x='RH', y='GHI', data=df, hue='TModA', palette='coolwarm', alpha=0.7)
    plt.title('Relative Humidity vs GHI')
    plt.xlabel('Relative Humidity (%)')
    plt.ylabel('Global Horizontal Irradiance (GHI)')

    # Scatter plot for DNI vs RH
    plt.subplot(1, 3, 2)
    sns.scatterplot(x='RH', y='DNI', data=df, hue='TModB', palette='coolwarm', alpha=0.7)
    plt.title('Relative Humidity vs DNI')
    plt.xlabel('Relative Humidity (%)')
    plt.ylabel('Direct Normal Irradiance (DNI)')

    # Scatter plot for DHI vs RH
    plt.subplot(1, 3, 3)
    sns.scatterplot(x='RH', y='DHI', data=df, hue='GHI', palette='coolwarm', alpha=0.7)
    plt.title('Relative Humidity vs DHI')
    plt.xlabel('Relative Humidity (%)')
    plt.ylabel('Diffuse Horizontal Irradiance (DHI)')

    plt.tight_layout()
    st.pyplot(plt)





# Function for Z-Score Analysis
def plot_zscore_analysis(df):
    # List of columns for which to calculate Z-scores
    columns_to_analyze = ['GHI', 'DNI', 'DHI', 'WS', 'TModA', 'TModB']

    # Calculate Z-scores for the selected columns
    z_scores = df[columns_to_analyze].apply(zscore)

    # Add Z-scores to the original DataFrame
    for col in columns_to_analyze:
        df[f'{col}_zscore'] = z_scores[col]

    # Flag data points with Z-scores that are significantly different from the mean
    significant_threshold = 3
    outliers = df[(z_scores.abs() > significant_threshold).any(axis=1)]

    st.write("Outliers flagged by Z-Score Analysis:")
    st.dataframe(outliers)

    # Optionally, you can visualize these outliers
    plt.figure(figsize=(14, 7))
    for i, col in enumerate(columns_to_analyze, 1):
        plt.subplot(2, 3, i)
        sns.scatterplot(data=df, x='Timestamp', y=col, hue=f'{col}_zscore', palette='coolwarm')
        plt.axhline(y=df[col].mean(), color='gray', linestyle='--')
        plt.title(f'{col} vs Time with Z-Score Hue')

    plt.tight_layout()
    st.pyplot(plt)


# Function for Bubble Chart Visualization
def plot_bubble_chart(df):
    # Filter data to ensure no missing values in key columns
    df = df.dropna(subset=['GHI', 'Tamb', 'WS', 'RH', 'BP'])

    plt.figure(figsize=(10, 8))

    # Bubble chart: GHI vs Tamb vs WS, with bubble size representing RH and color representing BP
    bubble_size = df['RH'] * 10  # Scale RH for better visibility in bubble size
    plt.scatter(df['GHI'], df['Tamb'], s=bubble_size, c=df['BP'], cmap='viridis', alpha=0.6, edgecolors="w", linewidth=0.5)

    # Add labels and title
    plt.title('Bubble Chart: GHI vs Tamb vs WS with RH as Bubble Size and BP as Color')
    plt.xlabel('Global Horizontal Irradiance (GHI)')
    plt.ylabel('Ambient Temperature (Tamb)')

    # Add a color bar for BP
    plt.colorbar(label='Barometric Pressure (BP)')

    st.pyplot(plt)


def main():
    st.title("Data Analysis Dashboard")

    # Sidebar options
    st.sidebar.title("Dashboard Configuration")
    project_name = st.sidebar.text_input("Project Name", value="Solar and Weather Data Dashboard")
    dataset_choice = st.sidebar.radio("Select Dataset", ["Dataset 1", "Dataset 2", "Dataset 3"])

    st.sidebar.write("Select Analysis Options:")
    summary_stats = st.sidebar.checkbox("Summary Statistics")
    data_quality_check = st.sidebar.checkbox("Data Quality Check")
    plot_hist = st.sidebar.checkbox("Histograms")
    correlation_heatmap = st.sidebar.checkbox("Correlation Heatmap")
    scatter_matrix_plot = st.sidebar.checkbox("Scatter Matrix")
    wind_analysis_polar = st.sidebar.checkbox("Wind Analysis (Polar Plot)")
    temperature_analysis = st.sidebar.checkbox("Temperature Analysis (RH vs Temp & Solar Radiation)")
    zscore_analysis = st.sidebar.checkbox("Z-Score Analysis")
    bubble_chart = st.sidebar.checkbox("Bubble Chart Analysis")

    # Load data
    df = load_data(dataset_choice)

    # Perform selected analyses
    if summary_stats:
        perform_summary_statistics(df)
    
    if data_quality_check:
        perform_data_quality_check(df)
    
    if plot_hist:
        st.subheader("Histograms of Key Variables")
        plot_histograms(df)
    
    if correlation_heatmap:
        st.subheader("Correlation Heatmap")
        plot_correlation_heatmap(df)
    
    if scatter_matrix_plot:
        st.subheader("Scatter Matrix")
        plot_scatter_matrix(df)
    
    if wind_analysis_polar:
        st.subheader("Wind Analysis (Polar Plot)")
        plot_wind_polar(df)

    if temperature_analysis:
        st.subheader("Temperature Analysis: RH vs Temp & Solar Radiation")
        plot_temperature_analysis(df)

    if zscore_analysis:
        st.subheader("Z-Score Analysis: Flagging Significant Outliers")
        plot_zscore_analysis(df)

    if bubble_chart:
        st.subheader("Bubble Chart: GHI vs Tamb vs WS with RH & BP")
        plot_bubble_chart(df)

if __name__ == "__main__":
    main()
