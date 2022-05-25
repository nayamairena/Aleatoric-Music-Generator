#import mido
#import random
#import sys
#import time
import pyaudio
import wave
import numpy as np
import argparse
"""
#Parse through the command line arguments to allow the user to customize commands.
parser = argparse.ArgumentParser(description='Play an aleatoric.')
parser.add_argument('--root', dest='root', type = int, default=48,
                    help='root note of scale (default: 48)')
parser.add_argument('--beats', dest='beats', type = int, default=8,
                    help='Time signature of SIG beats per measure (default: 8)')
parser.add_argument('--bpm', dest='bmp', type = float, default="90.0",
                    help='Beat frequency of beats per minute (default: 90)')
parser.add_argument('--ramp', dest='ramp', type = float, default=0.5,
                    help='Fraction of the beat time for the note envelope (default: 0.5)')
parser.add_argument('--accent', dest='accent', type = float, default=5.0,
                    help='Volume for the first accent beat of each measure (default: 5.0)')
parser.add_argument('--volume', dest='volume', type = float, default=8.0,
                    help='Volume for the unaccented beats of each measure (default: 8.0)')
args = parser.parse_args()
"""

#Create Sine wave
#CONST variables to set for the audio files.
SAMPLE_RATE = 48000
CHANNELS = 1
SAMPLE_SIZE = 2

#Part 1: sine.wav
#Use wave library to open and write to the WAV file.
sine_wav = wave.open('sine.wav', 'wb')
sine_wav.setnchannels(CHANNELS)
sine_wav.setsampwidth(SAMPLE_SIZE)
sine_wav.setframerate(SAMPLE_RATE)



for i in range(10):
    #Use numpy library linspace() to set samples and duration of 1 second.
    samples = np.linspace(0, 1, SAMPLE_RATE)
    #Set amplitude 
    amp = 32767*0.25
    #Get sine wave using numpy sin() function. 
    sine_data = amp * np.sin(2 * np.pi * (i*50+1) * samples)
    #Write the frames as 16-bit int to the WAV file.
    sine_wav.writeframes(sine_data.astype(np.int16))
sine_wav.close()


wf = wave.open('sine.wav', 'rb')
#Create PyAudio
p = pyaudio.PyAudio()
stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels = wf.getnchannels(),
                rate = wf.getframerate(),
                output = True)
data = wf.readframes(1024)
while data != b'':
    stream.write(data)
    data = wf.readframes(1024)
    

stream.close()
p.terminate()