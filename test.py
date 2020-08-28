import sounddevice as sd
from scipy.io.wavfile import write
from visualizer import make_plots
from time import sleep

SAMPLE_RATE = 44100
CHANNELS = 1
MIC_ID = 6

sd.default.device = 6

fname = input("File name: ") + '.wav'
fs = 44100  # Sample rate
seconds = 10  # Duration of recording

seconds = int(input('Seconds in Audio: ')) #Optional Time Specification
sleep(1)
print('Recording...')
myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
sd.wait()  # Wait until recording is finished
write(f'/home/pradyun/Documents/py/Musicy/test/{fname}', fs, myrecording)  # Save as WAV file
print('Done Recording\n')


# make_plots('tries/', numtrials)