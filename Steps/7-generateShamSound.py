from pydub import AudioSegment
import os
from dotenv import load_dotenv

load_dotenv()


def generate_audio_file(start_bpm, end_bpm, heartbeat_file):
    # Load the heartbeat sound
    heartbeat = AudioSegment.from_file(heartbeat_file)

    # Define the duration of the output audio (5 minutes)
    total_duration = 5 * 60 * 1000  # milliseconds

    # Define the duration of the ending output audio (1 minutes)
    ending_duration = 1 * 60 * 1000  # milliseconds

    # Calculate the time interval between heartbeats at the beginning and end
    initial_interval = 60000 / start_bpm
    final_interval = 60000 / end_bpm

    # Calculate the linear decrease in interval
    interval_difference = (initial_interval - final_interval) / total_duration

    # Create a new audio segment to store the final output
    output = AudioSegment.silent(duration=total_duration)

    # Create a new audio segment to store the final output
    output_ending = AudioSegment.silent(duration=ending_duration)

    heartbeat_interval = ending_duration / end_bpm

    # Iterate over the total duration and overlay each heartbeat on the output audio
    current_time = 0
    while current_time < total_duration:
        # Calculate the current interval
        interval = initial_interval - (current_time * interval_difference)

        # Overlay the current heartbeat sound on the output audio
        output = output.overlay(heartbeat, position=current_time)

        # Update the current time
        current_time += interval

    # Add heartbeats evenly spaced throughout the audio
    for i in range(int(end_bpm)):
        start_time = i * heartbeat_interval
        output_ending = output_ending.overlay(heartbeat, position=start_time)

    # Concatenate the ending audio segment to the output audio
    output = output + output_ending * 3

    # Export the final output audio to a file
    output.export(f"shamSound{os.getenv('USER_ID')}.mp3", format="mp3")


# Example usage
start_bpm = 56
end_bpm = start_bpm * 0.5  # 50% of the starting BPM
heartbeat_file = "/Users/benediktbreitschopf/Library/CloudStorage/GoogleDrive-benedikt.breitschopf@gmail.com/Meine Ablage/MA/heartbeatsound3.wav"

generate_audio_file(start_bpm, end_bpm, heartbeat_file)
