import os
from tqdm import tqdm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from python_speech_features import mfcc, logfbank
import librosa
from sys import argv

rows = 1
cols = 2

def plot_signals(signals):
    fig, axes = plt.subplots(nrows=rows, ncols=cols, sharex=False,
                             sharey=True, figsize=(20,5))
    fig.suptitle('Time Series', size=16)
    i = 0
    for x in range(rows):
        for y in range(cols):
            
            axes[y].set_title(list(signals.keys())[i])
            axes[y].plot(list(signals.values())[i])
            axes[y].get_xaxis().set_visible(False)
            axes[y].get_yaxis().set_visible(False)
            i += 1

def plot_fft(fft):
    fig, axes = plt.subplots(nrows=rows, ncols=cols, sharex=False,
                             sharey=True, figsize=(20,5))
    fig.suptitle('Fourier Transforms', size=16)
    i = 0
    for x in range(rows):
        for y in range(cols):
            data = list(fft.values())[i]
            Y, freq = data[0], data[1]
            axes[y].set_title(list(fft.keys())[i])
            axes[y].plot(freq, Y)
            axes[y].get_xaxis().set_visible(False)
            axes[y].get_yaxis().set_visible(False)
            i += 1

def plot_fbank(fbank):
    fig, axes = plt.subplots(nrows=rows, ncols=cols, sharex=False,
                             sharey=True, figsize=(20,5))
    fig.suptitle('Filter Bank Coefficients', size=16)
    i = 0
    for x in range(rows):
        for y in range(cols):
            axes[y].set_title(list(fbank.keys())[i])
            axes[y].imshow(list(fbank.values())[i],
                    cmap='hot', interpolation='nearest')
            axes[y].get_xaxis().set_visible(False)
            axes[y].get_yaxis().set_visible(False)
            i += 1

def plot_mfccs(mfccs):
    fig, axes = plt.subplots(nrows=rows, ncols=cols, sharex=False,
                             sharey=True, figsize=(20,5))
    fig.suptitle('Mel Frequency Cepstrum Coefficients', size=16)
    i = 0
    for x in range(rows):
        for y in range(cols):
            axes[y].set_title(list(mfccs.keys())[i])
            axes[y].imshow(list(mfccs.values())[i],
                    cmap='hot', interpolation='nearest')
            axes[y].get_xaxis().set_visible(False)
            axes[y].get_yaxis().set_visible(False)
            i += 1

def envelope(y, rate, thresh):
    mask = []
    y = pd.Series(y).apply(np.abs)
    y_mean = y.rolling(window=int(rate/10), min_periods=1, center=True).mean()  # creates a rolling window to check mean of vals
    for mean in y_mean:
        if mean > thresh:
            mask.append(True)
        else:
            mask.append(False)
    
    return mask

def calc_fft(y, rate):
    n = len(y)
    freq = np.fft.rfftfreq(n, d=1/rate)
    Y = abs(np.fft.rfft(y)/n)
    return Y, freq

def make_plots(indir, runs):

    # if len(argv) != 2:
    #     print('Need 2 args')
    #     sys.exit(1)
    # thedir = argv[1]

    thedir = indir
    rows = runs
    
    signals = {}
    fft = {}
    fbank = {}
    mfccs = {}

    for audsamp in os.listdir(thedir):
        # captures first file of each instrument
        f = f"{thedir}/{audsamp}"

        signal, rate = librosa.load(f , sr=44100)
        mask = envelope(signal, rate, 0.0005)
        signal = signal[mask]
        signals[audsamp] = signal
        fft[audsamp] = calc_fft(signal, rate)

        bank = logfbank(signal[:rate], rate, nfilt=26, nfft=1103).T
        fbank[audsamp] = bank
        mel = mfcc(signal[:rate], rate, numcep=13, nfilt=26, nfft=1103).T
        mfccs[audsamp] = mel

    plot_signals(signals)
    plt.show()

    plot_fft(fft)
    plt.show()

    plot_fbank(fbank)
    plt.show()

    plot_mfccs(mfccs)
    plt.show()

# if __name__ == "__main__":
#     main()