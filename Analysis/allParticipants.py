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

# List of colors for each participant
colors = ['blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan', 'magenta', 'yellow']

fig = plt.figure()
ax = plt.subplot(111)
for i, participant in enumerate(allParticipants):
    ax.plot(
        range(len(participant[2])),
        participant[2],
        label=f"Participant {i + 1}",
        color=colors[i],
    )

plt.title(f"Sham Heart Rate Sound - All Participants")
plt.xlabel("Duration (seconds)")
plt.ylabel("Heart Rate  \n (beats per minute averaged over 5 second intervals)")
plt.grid(True)

# Shrink current axis by 20%
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

# Put a legend to the right of the current axis
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

# Save or display the plot
plt.savefig(f"Sham Heart Rate Sound - All Participants.png")
plt.show()
