import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV file into a pandas DataFrame
data = pd.read_csv('/Users/benediktbreitschopf/Documents/Projects/MACode/Analysis/baseHeartRate1.csv')

# Assuming your CSV file has a 'Timestamp' column
timestamp_column = 'Timestamp'

# Time Series Plot
plt.figure(figsize=(10, 6))
plt.plot(data[timestamp_column], range(len(data)), marker='o')
plt.xlabel('Timestamp')
plt.ylabel('Observation Index')
plt.title('Heart Rate Time Series')
plt.show()

# Histogram
plt.figure(figsize=(10, 6))
plt.hist(data[timestamp_column], bins=20, alpha=0.7)
plt.xlabel('Timestamp')
plt.ylabel('Frequency')
plt.title('Heart Rate Timestamp Histogram')
plt.show()

# Density Plot
plt.figure(figsize=(10, 6))
sns.kdeplot(data[timestamp_column])
plt.xlabel('Timestamp')
plt.ylabel('Density')
plt.title('Heart Rate Timestamp Density Plot')
plt.show()
