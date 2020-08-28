import os
import sys
from tqdm import tqdm
import pandas as pd
import numpy as np
from random import choice, choices

import process_fp
import gensim as gn

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

def load_data(buckets, k):

    X = []
    y = []

    for bucket in buckets:
        for i in range(k):
            seq = choices(buckets[bucket], k=200)
            seq = sorted(seq)
            X.append(seq)
            y.append(bucket)

    return X, y

def create_w2v(vocabulary):
    w2v = gn.models.Word2Vec(min_count=1, size=25, window=2)
    w2v.build_vocab(vocabulary, progress_per=10000)
    w2v.train(vocabulary, total_examples=w2v.corpus_count, epochs=30)
    return w2v

def create_Sentences(buckets):
    sentences = []

    for bucket in buckets:
        sentences.append(buckets[bucket])

    return sentences

def preprocess(X, y, sentences):

    w2v = create_w2v(sentences)

    for x in X:
        for i in range(len(x)):
            fp = x[i]
            x[i] = w2v.wv[fp]

    le = LabelEncoder()
    le.fit_transform(y)

    X = np.array(X)
    nsamples, nx, ny = X.shape
    X = X.reshape((nsamples, nx*ny))

    return X, y, le

def clean_dir(direc):
    for f in os.listdir(direc):
        os.remove(os.path.join(direc, f))

def model(X, y):

    svc = SVC(kernel='sigmoid')
    svc.fit(X, y)

    return svc

def process_train(train_direc, data_direc):
    process_fp.preprocess(train_direc, data_direc)
    allfps, buckets = process_fp.process(train_direc, data_direc)

    X, y = load_data(buckets, 100)

    sentences = create_Sentences(buckets)
    X, y, labels = preprocess(X, y, sentences)

    clean_dir(data_direc)
    return X, y, sentences

def process_test(test_direc, data_direc, train_sentences, samples):
    process_fp.preprocess(test_direc, data_direc)
    alltestsfps, test_buckets = process_fp.process(test_direc, data_direc)

    X_test, y_test = load_data(test_buckets, samples)

    test_sentences = create_Sentences(test_buckets)
    X_test, y_test, labels = preprocess(X_test, y_test, (train_sentences + test_sentences))

    clean_dir(data_direc)
    return X_test, y_test

def detect_errors(svc, X_test, y_test):

    y_pred = svc.predict(X_test)

    print(confusion_matrix(y_test, y_pred))
    print(classification_report(y_test, y_pred))
    print('Accuracy Score: ', accuracy_score(y_test, y_pred))


X_train, y_train, train_buckets = process_train('train/', 'data/')

X_test, y_test = process_test('test/', 'data/', train_buckets, 30)

svc = model(X_train, y_train)

detect_errors(svc, X_test, y_test)