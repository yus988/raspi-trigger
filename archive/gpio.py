#!/usr/local/bin/python
# -*- coding: utf-8 -*-
# settings for audio output from headphone jack
# https://igarashi-systems.com/sample/translation/raspberry-pi/configuration/audio-configuration.html

from __future__ import print_function

import RPi.GPIO as GPIO
import time

# Pin Number
PIN = 19
OUT_PIN = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(OUT_PIN,GPIO.OUT)

GPIO.output(OUT_PIN, True)
while True:
    pin_status = GPIO.input(PIN)
    print(pin_status)
    time.sleep(0.1)

GPIO.cleanup()