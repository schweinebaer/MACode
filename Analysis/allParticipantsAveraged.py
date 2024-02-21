import pandas as pd
import matplotlib.pyplot as plt
import datetime
import matplotlib.dates as mdates
from averagePerParticipant import averagePerParticipant

allParticipants = []
for i in range(13):
    if i == 0 or i >= 13:
        continue
    print(i)
    base, real, sham = averagePerParticipant(i)
    allParticipants.append([base, real, sham])

class Matrix(object):
    def __init__(self, rows, columns, default=0):
        self.m = []
        for i in range(rows):
            self.m.append([default for j in range(columns)])

    def __getitem__(self, index):
        return self.m[index]

mBase, mReal, mSham = Matrix(416, 12),Matrix(416, 12),Matrix(416, 12)

for i, participant in enumerate(allParticipants):
    heartRatesBase, heartRatesReal, hearRatesSham = participant
    for j, heartRateBase in enumerate(heartRatesBase):
        mBase[j][i] = heartRateBase
    for j, heartRateReal in enumerate(heartRatesReal):
        mReal[j][i] = heartRateReal
    for j, heartRateSham in enumerate(hearRatesSham):
        mSham[j][i] = heartRateSham

base, real, sham = [], [], []
for i in range(0, 416):
    base.append(mBase[i])
    real.append(mReal[i])
    sham.append(mSham[i])

for i, beats in enumerate(base):
    base[i] = sum(beats) / len(beats)
    
for i, beats in enumerate(real):
    real[i] = sum(beats) / len(beats)
    
for i, beats in enumerate(sham):
    sham[i] = sum(beats) / len(beats)

plt.figure(figsize=(10, 6))
plt.plot(range(len(base)), base, label="No Sound", color="blue")
plt.plot(range(len(real)), real, label="Real Sound", color="green")
plt.plot(range(len(sham)), sham, label="Sham Sound", color="red")

plt.title(f"Average Heart Rates - All Participants")
plt.xlabel("Duration (seconds)")
plt.ylabel("Heart Rate \n (beats per minute averaged over 5 second intervals)")
plt.grid(True)
plt.legend()

# Save or display the plot
plt.savefig(f"Average Heart Rates - All Participants.png")
plt.show()