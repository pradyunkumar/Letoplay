# Letoplay
This is a prototype version of a machine learning based program that detects errors in your music and trains you to fix them. 
As of 0.0.0, the program only determines accuracy of the compared data.

This program works by using audio fingerprinting on multiple training examples of the song. It records the fingerprints and bucketizes them. These buckets are turned into sequences and sampled by using word2vec to convert them into arrays. By using a simple SVM linear kernel classifier, the porgram is able to determine acuracy of tests with high accuracy.

Put various versions of the piece in .wav form inside the trial folder, and put a test version inside the test folder. Delete the info.txt inside data. 
