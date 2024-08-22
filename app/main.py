import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

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

if __name__ == "__main__":
    main()
