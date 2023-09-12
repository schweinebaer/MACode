import pandas as pd
import matplotlib.pyplot as plt

participantId = 2

# Load the CSV file into a Pandas DataFrame
dataBase = pd.read_csv(
    f"/Users/benediktbreitschopf/Documents/Projects/MACode/ParticipantsData/Participant{participantId}/baseHeartRate{participantId}.csv"
)
dataReal = pd.read_csv(
    f"/Users/benediktbreitschopf/Documents/Projects/MACode/ParticipantsData/Participant{participantId}/realHeartRate{participantId}.csv"
)
dataSham = pd.read_csv(
    f"/Users/benediktbreitschopf/Documents/Projects/MACode/ParticipantsData/Participant{participantId}/shamHeartRate{participantId}.csv"
)

# Extract the Timestamp column as an array
timestampsBase = dataBase["Timestamp"].values
timestampsReal = dataReal["Timestamp"].values
timestampsSham = dataSham["Timestamp"].values

# Convert timestamps to pandas DataFrames
df1 = pd.DataFrame({'Timestamp': pd.to_datetime(timestampsBase)})
df2 = pd.DataFrame({'Timestamp': pd.to_datetime(timestampsReal)})
df3 = pd.DataFrame({'Timestamp': pd.to_datetime(timestampsSham)})

# Calculate the time difference between consecutive timestamps
df1['TimeDiff'] = df1['Timestamp'].diff().dt.total_seconds()
df2['TimeDiff'] = df2['Timestamp'].diff().dt.total_seconds()
df3['TimeDiff'] = df3['Timestamp'].diff().dt.total_seconds()

# Calculate heart rate (beats per minute)
df1['HeartRate'] = 60 / df1['TimeDiff']
df2['HeartRate'] = 60 / df2['TimeDiff']
df3['HeartRate'] = 60 / df3['TimeDiff']

# Calculate rolling averages 
rolling_window = 50
df1['RollingAverage'] = df1['HeartRate'].rolling(rolling_window).mean()
df2['RollingAverage'] = df2['HeartRate'].rolling(rolling_window).mean()
df3['RollingAverage'] = df3['HeartRate'].rolling(rolling_window).mean()


# Align the two datasets by finding the maximum starting timestamp
max_start_time = max(df1['Timestamp'].min(), df2['Timestamp'].min(), df3['Timestamp'].min())
df1['Timestamp'] -= (df1['Timestamp'].min() - max_start_time)
df2['Timestamp'] -= (df2['Timestamp'].min() - max_start_time)
df3['Timestamp'] -= (df3['Timestamp'].min() - max_start_time)

# Calculate the duration from the starting point 
start_time = max(df1['Timestamp'].min(), df2['Timestamp'].min(),  df3['Timestamp'].min())
df1['Duration'] = (df1['Timestamp'] - start_time).apply(lambda x: x.total_seconds())
df2['Duration'] = (df2['Timestamp'] - start_time).apply(lambda x: x.total_seconds())
df3['Duration'] = (df3['Timestamp'] - start_time).apply(lambda x: x.total_seconds())

# Create a time series plot of rolling averages 
plt.figure(figsize=(10, 6))
plt.plot(df1['Duration'], df1['RollingAverage'], label='Rolling Average (Base)', color='blue')
plt.plot(df2['Duration'], df2['RollingAverage'], label='Rolling Average (Real)', color='green')
plt.plot(df3['Duration'], df3['RollingAverage'], label='Rolling Average (Sham)', color='red')

plt.title(f'Rolling Average Heart Rate Comparison Participant {participantId}')
plt.xlabel('Duration (seconds)')
plt.ylabel('Rolling Average Heart Rate (bpm)')
plt.grid(True)
plt.legend()

# Save or display the plot
plt.savefig(f'Rolling Average Comparison Participant {participantId}.png')
plt.show()

