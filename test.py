import pandas as pd
import numpy as np
from scipy.signal import find_peaks, peak_prominences
import matplotlib.pyplot as plt

# Read the pulse data from a CSV file
filename = "dataCleaned.csv"
data = pd.read_csv(filename)

# Example data
x = data["Timestamp"]
y = data["Value"]

# Find all peaks
peaks, _ = find_peaks(y)

# Calculate peak prominences
prominences = peak_prominences(y, peaks)[0]
print(prominences)

# Sort peaks based on prominences
sorted_indices = np.argsort(prominences)[::-1]  # Descending order
top_peak_indices = sorted_indices[:3]  # Select the top 3 peaks

# Plot the data
plt.plot(x, y)
plt.plot(x[peaks[top_peak_indices]], y[peaks[top_peak_indices]], "ro")  # Mark the top peaks with red circles
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Top Peaks in the Data')
plt.show()