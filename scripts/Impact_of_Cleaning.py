import pandas as pd
import matplotlib.pyplot as plt

def analyze_and_plot(file_path: str):
    # Load data
    data = pd.read_csv(file_path)
    data['Timestamp'] = pd.to_datetime(data['Timestamp'])

    # Check for missing data
    missing_data = data.isnull().sum()
    print("Missing data summary:")
    print(missing_data)

    # Identify cleaning events
    cleaning_events = data[data['Cleaning'] > 0]
    if cleaning_events.empty:
        raise ValueError("No cleaning events found.")

    # Calculate mean readings before and after the first cleaning event
    before_cleaning = data[data['Timestamp'] < cleaning_events.iloc[0]['Timestamp']]
    after_cleaning = data[data['Timestamp'] >= cleaning_events.iloc[0]['Timestamp']]

    mean_before = before_cleaning[['ModA', 'ModB']].mean()
    mean_after = after_cleaning[['ModA', 'ModB']].mean()

    print("Mean sensor readings before cleaning:")
    print(mean_before)
    print("\nMean sensor readings after cleaning:")
    print(mean_after)

    # Plotting
    plt.figure(figsize=(14, 7))
    plt.plot(data['Timestamp'], data['ModA'], label='ModA', color='blue')
    plt.plot(data['Timestamp'], data['ModB'], label='ModB', color='orange')

    plt.scatter(cleaning_events['Timestamp'], cleaning_events['ModA'], 
                color='red', label='Cleaning Event', zorder=5)

    plt.xlabel('Timestamp')
    plt.ylabel('Sensor Readings')
    plt.title('Sensor Readings Over Time with Cleaning Events')
    plt.legend()
    plt.grid(True)
    plt.show()

