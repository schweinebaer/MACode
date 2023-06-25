import pandas as pd
import matplotlib.pyplot as plt
import os
from dotenv import load_dotenv

load_dotenv()

data = pd.read_csv(f"thresholdData{os.getenv('USER_ID')}.csv")

# Convert the ´timestamp column to datetime type
data['Timestamp'] = pd.to_datetime(data['Timestamp'])

# Plot the line graph
plt.plot(data['Timestamp'], data['Value'])
plt.xlabel('Timestamp')
plt.ylabel('Value')
plt.title(f"Data from thresholdData{os.getenv('USER_ID')}.csv")
plt.xticks(rotation=45)
plt.show()