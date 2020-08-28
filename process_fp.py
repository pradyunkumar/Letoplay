from dejavu import Dejavu
from createsql import createDJV

import os
import sys
from tqdm import tqdm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import librosa


SR = 44100

def envelope(signal, rate, thresh):

    mask = []
    y = pd.Series(signal).apply(np.abs)
    y_mean = y.rolling(window=int(rate/10), min_periods=1, center=True).mean()  # creates a rolling window to check mean of vals
    for mean in y_mean:
        if mean > thresh:
            mask.append(True)
        else:
            mask.append(False)

    return signal[mask]

def get_fplist(djv, path, limit):
    return [pair[0] for pair in list(djv.get_file_fingerprints(path, limit)[0])]

def create_djv():
    djv = createDJV()
    return djv

def fp_dir(djv, direc):
    djv.fingerprint_directory(direc, ['.wav'])

def catalog_all_fps(djv, direc, limit):
    allfps = []
    for trial in os.listdir(direc):
        path = os.path.join(direc, trial) 
        allfps += get_fplist(djv, path, limit)
    return set(allfps)

def divide_test(testdirec, newdirec, bpm):
    for test in os.listdir(testdirec):
        path = os.path.join(testdirec, test)
        rate, signalx = wavfile.read(path)
        signal = envelope(signalx, rate, 0.005)

        length = signal.shape[0]
        duration = (length/SR)/60
        beats = duration * bpm
        step = int(length/beats)
        start, end = 0, 0
        dur = step/SR

        newpath = f'{newdirec}/{test[:-4]}'
        for x in tqdm(range(0, length, step)):
            end = start + step
            name = f'{newpath}-{round(start/SR, 1)}_{round(start/SR + dur, 1)}-.wav'

            wavfile.write(name, SR, signal[start: end])

            start = end


def bucket_fps(djv, allfps, newdirec):

    buckets = {}

    for part in os.listdir(newdirec):
        place = part.split('-')[1]
        buckets[place] = []

    for part in os.listdir(newdirec):
        place = part.split('-')[1]
        path = os.path.join(newdirec, part)

        part_fps = get_fplist(djv, path, 3)
        intersection = list(set(part_fps) & set(allfps))
        buckets[place] += intersection

    for place in buckets:
        l = buckets[place]
        buckets[place] = list(set(l))

    return buckets

def preprocess(test_direc, data_direc):
    if os.listdir(data_direc):
        print('Already preprocessed')
        return

    djv = create_djv()
    divide_test(test_direc, data_direc, 40)
        
    fp_dir(djv, test_direc)
    fp_dir(djv, data_direc)
            
def process(catalog_dir, data_dir):
    djv = create_djv()
    allfps = catalog_all_fps(djv, catalog_dir, 15)
    buckets = bucket_fps(djv, allfps, data_dir)
    
    return list(allfps), buckets
