import pydub
import random

def generate_audio_file(nature_file, heartbeat_file, output_file):
    # Load the audio files
    nature_sound = pydub.AudioSegment.from_file(nature_file)
    heartbeat_sound = pydub.AudioSegment.from_file(heartbeat_file)

    # Calculate the interval reduction rate
    total_duration = 5 * 60 * 1000  # 5 minutes in milliseconds
    initial_bpm = 50
    final_bpm = 0.5 * initial_bpm
    interval_reduction_rate = (initial_bpm - final_bpm) / total_duration

    # Generate the combined audio
    combined_audio = pydub.AudioSegment.silent(duration=total_duration)

    current_time = 0
    while current_time < total_duration:
        # Calculate the interval for the heartbeat drum sound
        interval = 60000 / initial_bpm  # interval in milliseconds
        initial_bpm -= interval_reduction_rate
        interval = max(0, interval)

        # Add heartbeat drum sound at the current time
        combined_audio = combined_audio.overlay(heartbeat_sound, position=current_time)

        # Update the current time
        current_time += interval

    # Adjust the speed of the heartbeat drum sound
    combined_audio = combined_audio.speedup(playback_speed=0.5, chunk_size=10)

    # Overlay the nature sound on the combined audio
    combined_audio = combined_audio.overlay(nature_sound)

    # Export the combined audio as an MP3 file
    combined_audio.export(output_file, format='mp3')

# Example usage
nature_file = 'nature_sound.mp3'
heartbeat_file = 'heartbeat_drum.mp3'
output_file = 'combined_audio.mp3'

generate_audio_file(nature_file, heartbeat_file, output_file)


nature_file = '/Users/benediktbreitschopf/Library/CloudStorage/GoogleDrive-benedikt.breitschopf@gmail.com/Meine Ablage/MA/backgroundMusic46.mp3'
heartbeat_file = '/Users/benediktbreitschopf/Library/CloudStorage/GoogleDrive-benedikt.breitschopf@gmail.com/Meine Ablage/MA/heartbeatsound3.wav'
output_file = 'combined_audio.mp3'


generate_audio_file(nature_file, heartbeat_file, output_file)
