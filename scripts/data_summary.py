import pandas as pd

def generate_summary(file_path):
    """
    Reads a CSV file and returns summary statistics for numeric columns.
    
    Parameters:
    file_path (str): Path to the CSV file.

    Returns:
    pd.DataFrame: Summary statistics including mean, median, and standard deviation.
    """
    try:
        # Read the CSV file
        df = pd.read_csv(file_path)
        
        # Select numeric columns
        numeric_df = df.select_dtypes(include='number')
        
        # Generate summary statistics
        summary_stats = numeric_df.describe().transpose()
        
        # Add median and standard deviation
        summary_stats['median'] = numeric_df.median()
        summary_stats['std'] = numeric_df.std()
        
        return summary_stats
    
    except Exception as e:
        print(f"Error reading the file {file_path}: {e}")
        return None
