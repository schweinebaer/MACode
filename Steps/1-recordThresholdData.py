
import serial.tools.list_ports
import csv
import time
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

serialInst.baudrate = 9600
serialInst.port = os.getenv('SERIAL_INST_PORT')
serialInst.open()

data = []

# Run the program for 1 minutes
end_time = time.time() + 1 * 20


while time.time() < end_time:
    if serialInst.in_waiting:
        packet = serialInst.readline()
        value = packet.decode('utf').rstrip('\n').rstrip('\r')
       
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        
        # Add the timestamp and value to the data array
        data.append([timestamp, value])

        print(data)
      
    
# Save the data to a CSV file
filename = f"thresholdData{os.getenv('USER_ID')}.csv"
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Timestamp', 'Value'])  # Write header
    writer.writerows(data)  # Write data rows

print(f"Data saved to {filename}.")
    
    



        


          


    
