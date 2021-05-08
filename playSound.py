# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 07:50:49 2020
@author: Souichirou Kikuchi
"""

import RPi.GPIO as GPIO
from time import sleep
import subprocess

LED_GPIO = 4 # LEDに接続するGPIO番号
TACT_GPIO = 17 # Tack Switchに接続するGPIO番号
MP3_FILE = './se1.mp3' # 再生したいファイルPath

def toggle_switch(channel):
    global isPlaying
    global process
    if channel == TACT_GPIO:
        if isPlaying == False:
            isPlaying = True
            GPIO.output(LED_GPIO, GPIO.HIGH)
            args = ['mpg321', MP3_FILE]
            process = subprocess.Popen(args)
        else:
            isPlaying = False
            GPIO.output(LED_GPIO, GPIO.LOW)
            args = ['kill', str(process.pid)]
            subprocess.Popen(args)

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_GPIO, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(TACT_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(TACT_GPIO, GPIO.RISING, callback=toggle_switch, bouncetime=200)

isPlaying = False
process = None

try:
    while True:
        sleep(0.01)

except KeyboardInterrupt:
    pass

GPIO.cleanup()