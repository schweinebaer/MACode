import pandas as pd
import numpy as np
import os

# Read the data from the CSV file
data = pd.read_csv(f"thresholdData{os.getenv('USER_ID')}.csv")

# Calculate Z-scores for the 'Value' column
z_scores = np.abs((data['Value'] - data['Value'].mean()) / data['Value'].std())

# Define a threshold value for outliers (e.g., Z-score > 3)
threshold = 3

# Filter the data to remove outliers
filtered_data = data[z_scores <= threshold]

# Create a new CSV file with the filtered data
new_filename = f"thresholdData{os.getenv('USER_ID')}.csv"
filtered_data.to_csv(new_filename, index=False)

print(f"Filtered data saved to {new_filename}.")