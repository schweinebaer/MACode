import pandas as pd
import matplotlib.pyplot as plt
import datetime
import matplotlib.dates as mdates
from zScoreMethod import detect_outliers_z_score
from replaceWithMedian import replace_outliers_with_median


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

    graphBeatsBaseAfterOutlierDetectionAndReplacement = replace_outliers_with_median(
        graphBeatsBase, detect_outliers_z_score(graphBeatsBase, threshold=3)
    )
    print("Participant Base", participantId, ": ")
    print(
        sum(graphBeatsBaseAfterOutlierDetectionAndReplacement)
        / len(graphBeatsBaseAfterOutlierDetectionAndReplacement)
    )

    graphBeatsBaseAvg = []
    for i, graphBeatBase in enumerate(
        graphBeatsBaseAfterOutlierDetectionAndReplacement
    ):
        if i < 2 or i >= len(graphBeatsBaseAfterOutlierDetectionAndReplacement) - 2:
            continue
        graphBeatsBaseAvg.append(
            (
                graphBeatsBaseAfterOutlierDetectionAndReplacement[i - 2]
                + graphBeatsBaseAfterOutlierDetectionAndReplacement[i - 1]
                + graphBeatBase
                + graphBeatsBaseAfterOutlierDetectionAndReplacement[i + 1]
                + graphBeatsBaseAfterOutlierDetectionAndReplacement[i + 2]
            )
            / 5
        )

    graphBeatsReal = []
    for beat in beatsReal:
        graphBeatsReal.append(len(beat))

    graphBeatsRealAfterOutlierDetectionAndReplacement = replace_outliers_with_median(
        graphBeatsReal, detect_outliers_z_score(graphBeatsReal, threshold=3)
    )
    print("Participant Real", participantId, ": ")
    print(
        sum(graphBeatsRealAfterOutlierDetectionAndReplacement)
        / len(graphBeatsRealAfterOutlierDetectionAndReplacement)
    )

    graphBeatsRealAvg = []
    for i, graphBeatReal in enumerate(
        graphBeatsRealAfterOutlierDetectionAndReplacement
    ):
        if i < 2 or i >= len(graphBeatsRealAfterOutlierDetectionAndReplacement) - 2:
            continue
        graphBeatsRealAvg.append(
            (
                graphBeatsRealAfterOutlierDetectionAndReplacement[i - 2]
                + graphBeatsRealAfterOutlierDetectionAndReplacement[i - 1]
                + graphBeatReal
                + graphBeatsRealAfterOutlierDetectionAndReplacement[i + 1]
                + graphBeatsRealAfterOutlierDetectionAndReplacement[i + 2]
            )
            / 5
        )

    graphBeatsSham = []
    for beat in beatsSham:
        graphBeatsSham.append(len(beat))

    graphBeatsShamAfterOutlierDetectionAndReplacement = replace_outliers_with_median(
        graphBeatsSham, detect_outliers_z_score(graphBeatsSham, threshold=3)
    )

    print("Participant Sham", participantId, ": ")
    print(
        sum(graphBeatsShamAfterOutlierDetectionAndReplacement)
        / len(graphBeatsShamAfterOutlierDetectionAndReplacement)
    )

    graphBeatsShamAvg = []
    for i, graphBeatSham in enumerate(
        graphBeatsShamAfterOutlierDetectionAndReplacement
    ):
        if i < 2 or i >= len(graphBeatsShamAfterOutlierDetectionAndReplacement) - 2:
            continue
        graphBeatsShamAvg.append(
            (
                graphBeatsShamAfterOutlierDetectionAndReplacement[i - 2]
                + graphBeatsShamAfterOutlierDetectionAndReplacement[i - 1]
                + graphBeatSham
                + graphBeatsShamAfterOutlierDetectionAndReplacement[i + 1]
                + graphBeatsShamAfterOutlierDetectionAndReplacement[i + 2]
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
