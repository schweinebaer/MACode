import pandas as pd
import matplotlib.pyplot as plt
import datetime
import matplotlib.dates as mdates

participantId = 11

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
base_datetime_objects = [
    datetime.datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S.%f")
    for timestamp in timestampsBase
]
real_datetime_objects = [
    datetime.datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S.%f")
    for timestamp in timestampsReal
]
sham_datetime_objects = [
    datetime.datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S.%f")
    for timestamp in timestampsSham
]



timestampStartBase = base_datetime_objects[0]
timestampStartRoundedUpBase = datetime.datetime(
    timestampStartBase.year,
    timestampStartBase.month,
    timestampStartBase.day,
    timestampStartBase.hour,
    timestampStartBase.minute,
    timestampStartBase.second + 1,
)
timestampStartReal= real_datetime_objects[0]
timestampStartRoundedUpReal = datetime.datetime(
    timestampStartReal.year,
    timestampStartReal.month,
    timestampStartReal.day,
    timestampStartReal.hour,
    timestampStartReal.minute,
    timestampStartReal.second + 1,
)
timestampStartSham = sham_datetime_objects[0]
timestampStartRoundedUpSham = datetime.datetime(
    timestampStartSham.year,
    timestampStartSham.month,
    timestampStartSham.day,
    timestampStartSham.hour,
    timestampStartSham.minute,
    timestampStartSham.second + 1,
)

beatsBase = []
for i in range(7 * 60):
    beatsPerSecond = []
    for datetime_object in base_datetime_objects:
        if datetime_object >= timestampStartRoundedUpBase + datetime.timedelta(seconds=i):
            if datetime_object <= timestampStartRoundedUpBase + datetime.timedelta(
                seconds=60 + i
            ):
                beatsPerSecond.append(datetime_object)
    beatsBase.append(beatsPerSecond)

beatsReal = []
for i in range(7 * 60):
    beatsPerSecond = []
    for datetime_object in real_datetime_objects:
        if datetime_object >= timestampStartRoundedUpReal + datetime.timedelta(seconds=i):
            if datetime_object <= timestampStartRoundedUpReal + datetime.timedelta(
                seconds=60 + i
            ):
                beatsPerSecond.append(datetime_object)
    beatsReal.append(beatsPerSecond)

beatsSham = []
for i in range(7 * 60):
    beatsPerSecond = []
    for datetime_object in sham_datetime_objects:
        if datetime_object >= timestampStartRoundedUpSham + datetime.timedelta(seconds=i):
            if datetime_object <= timestampStartRoundedUpSham + datetime.timedelta(
                seconds=60 + i
            ):
                beatsPerSecond.append(datetime_object)
    beatsSham.append(beatsPerSecond)


graphBeatsBase = []
for beat in beatsBase:
    graphBeatsBase.append(len(beat))

graphBeatsReal = []
for beat in beatsReal:
    graphBeatsReal.append(len(beat))

graphBeatsSham = []
for beat in beatsSham:
    graphBeatsSham.append(len(beat))



plt.figure(figsize=(10, 6))
plt.plot(range(len(graphBeatsBase)), graphBeatsBase, label='No Sound', color='blue')
plt.plot(range(len(graphBeatsReal)), graphBeatsReal, label='Real Sound', color='green')
plt.plot(range(len(graphBeatsSham)), graphBeatsSham, label='Sham Sound', color='red')

plt.title(f'Rolling Average Heart Rate Comparison Participant {participantId}')
plt.xlabel('Duration (seconds)')
plt.ylabel('Rolling Average Heart Rate (bpm)')
plt.grid(True)
plt.legend()

# Save or display the plot
plt.savefig(f'Rolling Average Comparison Participant {participantId}.png')
plt.show()