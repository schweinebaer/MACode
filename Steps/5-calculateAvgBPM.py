
import serial.tools.list_ports
import csv
import time
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

serialInst.baudrate = 9600
serialInst.port = os.getenv('SERIAL_INST_PORT')

serialInst.open()

data = []
bpm_values = []

# Run the program for 1 minutes
end_time = time.time() + 1 * 60


while time.time() < end_time:
    if serialInst.in_waiting:
        packet = serialInst.readline()
        value = packet.decode('utf').rstrip('\n').rstrip('\r')
       
        if value.isdigit():
            bpm_values.append(int(value))
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        
            # Add the timestamp and value to the data array
            data.append([timestamp, int(value)])

            print(data)
            
        # Calculate average BPM
        if bpm_values:
            average_bpm = sum(bpm_values) / len(bpm_values)
            print("Average BPM:", average_bpm)
        else:
            print("No BPM values were recorded.")
        

filename = f"avgData{os.getenv('USER_ID')}.csv"
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Timestamp', 'Value'])  # Write header
    writer.writerows(data)  # Write data rows

print(f"Data saved to {filename}.")
    


        


          


    
