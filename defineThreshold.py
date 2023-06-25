import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from scipy.signal import find_peaks
from dotenv import load_dotenv

load_dotenv()

# Read the pulse data from a CSV file
data = pd.read_csv(f"thresholdData{os.getenv('USER_ID')}.csv")

# Calculate the median of the pulse values
median_pulse = data["Value"].median()
peaks, _ = find_peaks(data["Value"])


# Example data
x = data["Timestamp"]
y = data["Value"]

# Find peaks with a minimum prominence
peaks, _ = find_peaks(y, prominence=8)
average_peak = y[peaks].mean()
suggested_treshold = (average_peak - median_pulse) * 0.6 + median_pulse

print(f"Median Pulse: {median_pulse}")
print(f"Average Peak: {average_peak}")
print(f"Suggested Treshold: {suggested_treshold}")


# Plot the data
plt.plot(x, y)
plt.plot(x, np.ones_like(y) * median_pulse, "g--")
plt.plot(x, np.ones_like(y) * average_peak, "c--")
plt.plot(x, np.ones_like(y) * suggested_treshold, "m-")
plt.plot(x[peaks], y[peaks], "ko")  # Mark the peaks with red circles
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Top Peaks in the Data")
plt.show()
