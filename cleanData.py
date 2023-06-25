import pandas as pd
import numpy as np

# Read the data from the CSV file
filename = "data5.csv"
data = pd.read_csv(filename)

# Calculate Z-scores for the 'Value' column
z_scores = np.abs((data['Value'] - data['Value'].mean()) / data['Value'].std())

# Define a threshold value for outliers (e.g., Z-score > 3)
threshold = 3

# Filter the data to remove outliers
filtered_data = data[z_scores <= threshold]

# Create a new CSV file with the filtered data
new_filename = "dataCleaned.csv"
filtered_data.to_csv(new_filename, index=False)

print(f"Filtered data saved to {new_filename}.")