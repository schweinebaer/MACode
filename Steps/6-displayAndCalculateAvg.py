import pandas as pd
import matplotlib.pyplot as plt
import os
from dotenv import load_dotenv

load_dotenv()

# Load the CSV file into a DataFrame
df = pd.read_csv(f"avgData{os.getenv('USER_ID')}.csv", parse_dates=['Timestamp'])

# Calculate the time difference between consecutive timestamps and convert to seconds
df['time_diff'] = (df['Timestamp'] - df['Timestamp'].shift()).dt.total_seconds()

# Calculate the cumulative time difference from the start
df['cumulative_time'] = df['time_diff'].cumsum()

# Calculate the instantaneous Beats per Minute (BPM)
df['instant_bpm'] = 60 / df['time_diff']

# Define the rolling window size for the average (e.g., 30 seconds)
rolling_window = 60  # You can adjust this value as needed

# Calculate the rolling average of BPM
df['rolling_average_bpm'] = df['instant_bpm'].rolling(window=rolling_window).mean()

# Plot the rolling average BPM
plt.figure(figsize=(12, 6))
plt.plot(df['cumulative_time'], df['rolling_average_bpm'], label='Rolling Average BPM')
plt.xlabel('Duration (seconds)')
plt.ylabel('BPM')
plt.title('Rolling Average Heartbeat BPM')
plt.grid(True)
plt.legend()

# Calculate and print the overall average BPM
overall_avg_bpm = df['instant_bpm'].mean()
print(f"Overall Average BPM: {overall_avg_bpm:.2f}")

# Show the plot
plt.show()
