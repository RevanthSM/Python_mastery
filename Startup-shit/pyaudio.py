import pandas as pd
import numpy as np
from scipy.io.wavfile import write
import pygame

def convert_excel_to_audio(excel_file):
    try:
        excel_data = pd.read_excel(excel_file, sheet_name='Sheet1')

        toa_data = excel_data['TOA'].values
        cumulative_time_data = excel_data['cumulative_time'].values
        power_data = excel_data['power'].values

        # Normalize data using min-max scaling
        toa_data = normalize_data(toa_data)
        cumulative_time_data = normalize_data(cumulative_time_data)
        power_data = normalize_data(power_data)

        # Map data to frequencies
        frequencies_toa = map_to_frequency(toa_data)
        frequencies_cumulative_time = map_to_frequency(cumulative_time_data)
        frequencies_power = map_to_frequency(power_data)

        # Combine frequencies
        combined_frequencies = (frequencies_toa + frequencies_cumulative_time + frequencies_power) / 3

        # Audio parameters
        target_duration = 60  
        sampling_rate = 44100 
        samples_needed = int(target_duration * sampling_rate)
        time = np.linspace(0, target_duration, samples_needed)
        
        # Resize combined frequencies to match time array length
        combined_frequencies = np.resize(combined_frequencies, len(time))
        
        # Generate audio signal
        audio = np.sin(2 * np.pi * combined_frequencies * time)
        audio /= np.max(np.abs(audio))

        # Write audio to WAV file
        wav_output_file = "output.wav"
        write(wav_output_file, sampling_rate, audio)

        # Initialize Pygame mixer for audio playback
        pygame.mixer.init()

        # Load and play WAV file
        pygame.mixer.music.load(wav_output_file)
        pygame.mixer.music.play()

        # Wait for audio playback to finish
        while pygame.mixer.music.get_busy():
            pygame.time.wait(100)

        # Quit Pygame mixer
        pygame.mixer.quit()

    except Exception as e:
        print("An error occurred:", e)

def normalize_data(data):
    # Min-max scaling
    return (data - np.min(data)) / (np.max(data) - np.min(data))

def map_to_frequency(data):
    # Adjust mapping logic as needed
    return data * 1000  

convert_excel_to_audio('Book1.xlsx')