import pandas as pd
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def calculateRMSSD(participantId):
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
    timestampsBase = dataBase[
        "Timestamp"
    ].values  # Convert timestamp strings to datetime objects
    timestampsReal = dataReal[
        "Timestamp"
    ].values  # Convert timestamp strings to datetime objects
    timestampsSham = dataSham[
        "Timestamp"
    ].values  # Convert timestamp strings to datetime objects

    # Convert timestamps to datetime objects
    base_heartbeats_datetime = [
        datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S.%f")
        for timestamp in timestampsBase
    ]
    real_heartbeats_datetime = [
        datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S.%f")
        for timestamp in timestampsReal
    ]
    sham_heartbeats_datetime = [
        datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S.%f")
        for timestamp in timestampsSham
    ]

    # Calculate RR intervals in milliseconds
    rr_intervals_base = np.diff(
        [ts.timestamp() * 1000 for ts in base_heartbeats_datetime]
    )
    rr_intervals_real = np.diff(
        [ts.timestamp() * 1000 for ts in real_heartbeats_datetime]
    )
    rr_intervals_sham = np.diff(
        [ts.timestamp() * 1000 for ts in sham_heartbeats_datetime]
    )

    # Calculate RMSSD
    rmssdBase = np.sqrt(np.mean(np.square(np.diff(rr_intervals_base))))
    rmssdReal = np.sqrt(np.mean(np.square(np.diff(rr_intervals_real))))
    rmssdSham = np.sqrt(np.mean(np.square(np.diff(rr_intervals_sham))))
    print("Participant ")
    print(participantId)
    print(": ")
    print([rmssdBase, rmssdReal, rmssdSham])

    return [rmssdBase, rmssdReal, rmssdSham]


hrv_data = []
for i in range(13):
    if i == 0:
        continue
    hrv_data.append(calculateRMSSD(i))

hrv_base_data, hrv_real_data, hrv_sham_data = [], [], []
for i, data in enumerate(hrv_data):
    hrv_base_data.append(data[0])
    hrv_real_data.append(data[1])
    hrv_sham_data.append(data[2])

data = [hrv_base_data, hrv_real_data, hrv_sham_data]
print(data)

plt.figure(figsize=(8, 6))  # Adjust figure size
plt.boxplot(data, patch_artist=True)
plt.ylabel("Heart Rate Variability (HRV)")  # Y-axis label
plt.title("RMSSD Heart Rate Variability (HRV) - All Participants")  # Title
plt.xticks([1, 2, 3], ["No Sound", "Real Sound", "Sham Sound"])  # Adjust x-axis ticks
plt.grid(True)  # Add grid for better readability
plt.tight_layout()  # Adjust layout to prevent overlapping elements
plt.savefig("Boxplot_HRV.png", dpi=300)  # Save figure as PNG with high resolution
plt.show()
