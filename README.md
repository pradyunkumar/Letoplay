# Description & Features
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

### Development

Want to contribute? Great! Email me at pradyunkumar03@gmail.com
