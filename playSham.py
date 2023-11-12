import serial.tools.list_ports
import os
import csv
import pygame
import time
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

serialInst.baudrate = 9600
serialInst.port = os.getenv("SERIAL_INST_PORT")
# serialInst.port = val
serialInst.open()

data = []

# Initialize Pygame
pygame.init()

# Load the heartbeat sound
heartbeat_sound = pygame.mixer.Sound(f"/Users/benediktbreitschopf/Documents/Projects/MACode/shamSound{os.getenv('USER_ID')}.mp3")
heartbeat_sound.play()

# Run the program for 8 minutes
end_time = time.time() + 8 * 60


while time.time() < end_time:
    if serialInst.in_waiting:
        packet = serialInst.readline()
        value = packet.decode("utf").rstrip("\n").rstrip("\r")
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        
        # Add the timestamp and value to the data array
        data.append([timestamp])
        print(timestamp)

# Clean up resources
serialInst.close()
pygame.quit()

# Save the data to a CSV file
filename = f"shamHeartRate{os.getenv('USER_ID')}.csv"
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Timestamp'])  # Write header
    writer.writerows(data)  # Write data rows

print(f"Data saved to {filename}.")