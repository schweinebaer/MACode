## The Impact of Sham Audio Biofeedback on Heart Rate
### Benedikt Breitschopf

Master’s Thesis · Bauhaus-Universität Weimar · Faculty of Media · Human-Computer Interaction (HCI) M.Sc.

This repository contains all the necessary files to carry out the data recording section of the thesis. Below, you will find a detailed description for each participant, outlining the steps involved.

---

### Preparation per participant


0. Define SERIAL_INST_PORT & USER_ID in *.env*
1. *0-initArduino.ino*
2. *1-recordThresholdData.py*
3. *2-displayThresholdData.py*
4. *3-defineThreshold.py*
5. *4-setupArduino.ino*
6. *5-calculateAvgBPM.py*
7. *6-6-displayAndCalculateAvg.py*
8. *7-generateShamSound.py*

### Sham and real audio biofeedback files
1. *playSham.py*: Plays the sham audio file records heart beats
2. *playReal.py*: Plays live heart beats and records heart beats
2. *playBase.py*: Records heart beats. No sound is played.


### Arduino wire mapping

Blue 5V
White GND
Green A3
