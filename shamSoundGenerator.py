from pydub import AudioSegment

def generate_audio_file(start_bpm, end_bpm, heartbeat_file, nature_file, output_file):
    # Load the heartbeat sound
    heartbeat = AudioSegment.from_file(heartbeat_file)

    # Load the nature sound
    nature_sound = AudioSegment.from_file(nature_file)

    # Define the duration of the output audio (5 minutes)
    total_duration = 5 * 60 * 1000  # milliseconds

    # Calculate the time interval between heartbeats at the beginning and end
    initial_interval = 60000 / start_bpm
    final_interval = 60000 / end_bpm

    # Calculate the linear decrease in interval
    interval_difference = (initial_interval - final_interval) / total_duration

    # Create a new audio segment to store the final output
    output = AudioSegment.silent(duration=total_duration)

    # Iterate over the total duration and overlay each heartbeat on the output audio
    current_time = 0
    while current_time < total_duration:
        # Calculate the current interval
        interval = initial_interval - (current_time * interval_difference)

        # Overlay the current heartbeat sound on the output audio
        output = output.overlay(heartbeat, position=current_time)

        # Update the current time
        current_time += interval

    # Overlay the nature sound on the combined audio
    output = output.overlay(nature_sound)

    # Export the final output audio to a file
    output.export(output_file, format="mp3")


# Example usage
start_bpm = 50
end_bpm = start_bpm * 0.5  # 50% of the starting BPM
heartbeat_file = "/Users/benediktbreitschopf/Library/CloudStorage/GoogleDrive-benedikt.breitschopf@gmail.com/Meine Ablage/MA/heartbeatsound3.wav"
nature_file = "/Users/benediktbreitschopf/Library/CloudStorage/GoogleDrive-benedikt.breitschopf@gmail.com/Meine Ablage/MA/backgroundMusic46.mp3"
output_file = "output.mp3"

generate_audio_file(start_bpm, end_bpm, heartbeat_file, nature_file, output_file)
