import pandas as pd

def clean_and_save_data(input_file_path: str, output_file_path: str):
    # Load the data
    data = pd.read_csv(input_file_path)

    # Drop columns where all values are missing
    data = data.dropna(axis=1, how='all')

    # Interpolate missing values using linear method
    data.interpolate(method='linear', inplace=True)

    # Drop any remaining rows with missing values
    data.dropna(inplace=True)

    # Filter out rows where GHI, DNI, or DHI are negative
    data = data[(data['GHI'] >= 0) & (data['DNI'] >= 0) & (data['DHI'] >= 0)]

    # Reset index after cleaning
    data.reset_index(drop=True, inplace=True)

    # Print the first few rows of the cleaned data
    print(data.head())

    # Save the cleaned data to a new CSV file
    data.to_csv(output_file_path, index=False)


