import serial.tools.list_ports
import subprocess
import os
from dotenv import load_dotenv

load_dotenv()

ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

serialInst.baudrate = 9600
serialInst.port = os.getenv('SERIAL_INST_PORT')
# serialInst.port = val
serialInst.open()

# Continuously read from the serial port
while True:
    if serialInst.in_waiting:
        packet = serialInst.readline()
        value = packet.decode("utf").rstrip("\n").rstrip("\r")
        print(value)
        try:
            if 40 < int(value) < 120:
                # Play the jungle drum-like sound
                subprocess.call(
                    [
                        "afplay",
                        "/Users/benediktbreitschopf/Library/CloudStorage/GoogleDrive-benedikt.breitschopf@gmail.com/Meine Ablage/MA/heartbeatsound3.wav",
                    ]
                )
        except:
            print("An exception occurred")

        # Check if the received value is "true"
