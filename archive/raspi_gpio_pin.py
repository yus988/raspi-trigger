#!/usr/local/bin/python
# -*- coding: utf-8 -*-
# settings for audio output from headphone jack
# https://igarashi-systems.com/sample/translation/raspberry-pi/configuration/audio-configuration.html

from __future__ import print_function

import RPi.GPIO as GPIO
import time

GPIO.cleanup()

# Pin Number
PIN = 19

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# GPIO.setup(OUT_PIN,GPIO.OUT)
while True:
    try:
        pin_status = GPIO.input(PIN)
        print(pin_status)
        time.sleep(0.1)
    except KeyboardInterrupt:
        GPIO.cleanup()
        print("Finished and clean up GPIO")
        break

