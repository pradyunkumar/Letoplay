# Description
Have you ever wanted to check the precise accuracy of your music ractice based on professional samples? Letoplay is a music accuracy program that gauges the correctness of your music based on training samples based on tempo and tune. Here are some features of the program:

1. Percent Accuracy of Music
2. Training on which parts of the song need improvement (currently in development)
3. Easy to use UI (currently in development)


# How it Works

Letoplay works through a data collected by Dejavu audiofingerprinting. Check out [dejavu documentation](https://github.com/worldveil/dejavu). The song is then broken off into time sections based on the bpm, which are used as targets for the data. To create data, a random sequence of fingerprints are chosen and given a label of the time section. The fingerprints are then called run through word2vec to create an numeric data. This data is then trained through a linear SVC kernel and tested with the test data to determine accuracy. 

NOTE: The features described below are still under development.
The specific training will be created based on tracking the fingerprints at specific times. The UI is developed through flask.


# Installation
NOTE: pip install is in progress of being set up. For now just git clone this documentation. Follow installation instructions from [Dejavu](https://github.com/worldveil/dejavu).

```sh
$ pip install -r requirements.txt
```
### Running the Program

All Audio must be in .wav format. Place training files in the training folder and test files in the test folder. Delete any non-wav files from all train, test, and data. Run model.py to check the accuracy score.

Using test.py, you can record your audio directly to a wav file which will be added to the test directory.

```
$ python3 test.py
File Name: firsttry
Seconds in Audio: 10
Recording...
Done Recording
```

To run the accuracy test:

```sh
$ python3 model.py
```

Expented Result:

```
              precision    recall  f1-score   support

     0.0_1.5       0.77      0.42      0.55        40
     1.5_3.0       0.80      1.00      0.89        40
   12.0_13.5       0.00      0.00      0.00         0
     3.0_4.5       0.84      0.93      0.88        40
     4.5_6.0       0.58      0.90      0.71        40
     6.0_7.5       0.91      1.00      0.95        40
     7.5_9.0       1.00      0.78      0.87        40
    9.0_10.5       1.00      0.65      0.79        40

    accuracy                           0.81       280
   macro avg       0.74      0.71      0.70       280
weighted avg       0.84      0.81      0.81       280

Accuracy Score:  0.8107142857142857
```

### Development

Want to contribute or ask questions? Great! Email me at pradyunkumar03@gmail.com.
