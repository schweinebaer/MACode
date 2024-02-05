import pandas as pd
import matplotlib.pyplot as plt
import datetime
import matplotlib.dates as mdates


def averagePerParticipant(participantId):
    participantId = participantId

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
        timestampStartBase.second,
    )
    timestampStartRoundedUpBase = timestampStartRoundedUpBase + datetime.timedelta(
        seconds=1
    )

    timestampStartReal = real_datetime_objects[0]
    timestampStartRoundedUpReal = datetime.datetime(
        timestampStartReal.year,
        timestampStartReal.month,
        timestampStartReal.day,
        timestampStartReal.hour,
        timestampStartReal.minute,
        timestampStartReal.second,
    )
    timestampStartRoundedUpReal = timestampStartRoundedUpReal + datetime.timedelta(
        seconds=1
    )

    timestampStartSham = sham_datetime_objects[0]
    timestampStartRoundedUpSham = datetime.datetime(
        timestampStartSham.year,
        timestampStartSham.month,
        timestampStartSham.day,
        timestampStartSham.hour,
        timestampStartSham.minute,
        timestampStartSham.second,
    )
    timestampStartRoundedUpSham = timestampStartRoundedUpSham + datetime.timedelta(
        seconds=1
    )

    beatsBase = []
    for i in range(7 * 60):
        beatsPerSecond = []
        for datetime_object in base_datetime_objects:
            if datetime_object >= timestampStartRoundedUpBase + datetime.timedelta(
                seconds=i
            ):
                if datetime_object <= timestampStartRoundedUpBase + datetime.timedelta(
                    seconds=60 + i
                ):
                    beatsPerSecond.append(datetime_object)
        beatsBase.append(beatsPerSecond)

    beatsReal = []
    for i in range(7 * 60):
        beatsPerSecond = []
        for datetime_object in real_datetime_objects:
            if datetime_object >= timestampStartRoundedUpReal + datetime.timedelta(
                seconds=i
            ):
                if datetime_object <= timestampStartRoundedUpReal + datetime.timedelta(
                    seconds=60 + i
                ):
                    beatsPerSecond.append(datetime_object)
        beatsReal.append(beatsPerSecond)

    beatsSham = []
    for i in range(7 * 60):
        beatsPerSecond = []
        for datetime_object in sham_datetime_objects:
            if datetime_object >= timestampStartRoundedUpSham + datetime.timedelta(
                seconds=i
            ):
                if datetime_object <= timestampStartRoundedUpSham + datetime.timedelta(
                    seconds=60 + i
                ):
                    beatsPerSecond.append(datetime_object)
        beatsSham.append(beatsPerSecond)

    graphBeatsBase = []
    for beat in beatsBase:
        graphBeatsBase.append(len(beat))

    graphBeatsBaseAvg = []
    for i, graphBeatBase in enumerate(graphBeatsBase):
        if i < 2 or i >= len(graphBeatsBase) - 2:
            continue
        graphBeatsBaseAvg.append(
            (
                graphBeatsBase[i - 2]
                + graphBeatsBase[i - 1]
                + graphBeatBase
                + graphBeatsBase[i + 1]
                + graphBeatsBase[i + 2]
            )
            / 5
        )

    graphBeatsReal = []
    for beat in beatsReal:
        graphBeatsReal.append(len(beat))

    graphBeatsRealAvg = []
    for i, graphBeatReal in enumerate(graphBeatsReal):
        if i < 2 or i >= len(graphBeatsReal) - 2:
            continue
        graphBeatsRealAvg.append(
            (
                graphBeatsReal[i - 2]
                + graphBeatsReal[i - 1]
                + graphBeatReal
                + graphBeatsReal[i + 1]
                + graphBeatsReal[i + 2]
            )
            / 5
        )

    graphBeatsSham = []
    for beat in beatsSham:
        graphBeatsSham.append(len(beat))

    graphBeatsShamAvg = []
    for i, graphBeatSham in enumerate(graphBeatsSham):
        if i < 2 or i >= len(graphBeatsSham) - 2:
            continue
        graphBeatsShamAvg.append(
            (
                graphBeatsSham[i - 2]
                + graphBeatsSham[i - 1]
                + graphBeatSham
                + graphBeatsSham[i + 1]
                + graphBeatsSham[i + 2]
            )
            / 5
        )

    return graphBeatsBaseAvg, graphBeatsRealAvg, graphBeatsShamAvg


def plotGraph(base, real, sham, participantId):
    plt.figure(figsize=(10, 6))
    plt.plot(range(len(base)), base, label="No Sound", color="blue")
    plt.plot(range(len(real)), real, label="Real Sound", color="green")
    plt.plot(range(len(sham)), sham, label="Sham Sound", color="red")

    plt.title(f"Heart Rate - Participant {participantId}")
    plt.xlabel("Duration (seconds)")
    plt.ylabel("Heart Rate  \n (beats per minute averaged over 5 second intervals)")
    plt.grid(True)
    plt.legend()

    # Save or display the plot
    plt.savefig(f"Heart Rate - Participant {participantId}.png")
    plt.show()

# for i in range(13):
#     if i == 0 or i >= 13:
#         continue
#     participantId = i
#     base, real, sham = averagePerParticipant(participantId)
#     plotGraph(base, real, sham, participantId)

