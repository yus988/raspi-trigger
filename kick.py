#!/usr/bin/env python
# -*- coding:utf-8 -*-

# モノが距離センサの上を
# スイッチを押したら音がなる。はじめに鳴らす音を 1, 2, 3, 4, 5 で指定

import spidev
import time
import matplotlib.pyplot as plt
import numpy as np
from time import perf_counter
import csv
import datetime
import pygame.mixer
import RPi.GPIO as GPIO

# 解説参照
def readAdc(channel, spi):
    adc = spi.xfer2([1, (8 + channel) << 4, 200])
    # print(adc)
    data = ((adc[1] & 3) << 8) + adc[2]
    return data

def convertVolts(data, vref):
    volts = (data * vref) / float(1023)
    volts = round(volts, 4)
    return volts

def playSE(se):
    se.play()  # loop count
    time.sleep(0.5)  # 一定時間再生
    pygame.mixer.music.stop()  # 停止
    
####################### setup se #################################
pygame.mixer.quit()
pygame.mixer.pre_init(buffer=64)
pygame.mixer.init()

arrName = [
    'gunRaw.wav',
    'gunRawArm.wav',
    'gunRawNeck.wav',
    'gunSamp.wav',
    'gunStime.wav'
]

se1 = pygame.mixer.Sound(arrName[0])
se2 = pygame.mixer.Sound(arrName[1])
se3 = pygame.mixer.Sound(arrName[2])
se4 = pygame.mixer.Sound(arrName[3])
se5 = pygame.mixer.Sound(arrName[4])

# seType = input("input type num : ")
# if seType == "1":
#     se = se1
#     name = arrName[0]
# elif seType == "2":
#     se = se2
#     name = arrName[1]
# elif seType == "3":
#     se = se3
#     name = arrName[2]
# elif seType == "4":
#     se = se4
#     name = arrName[3]
# elif seType == "5":
#     se = se5
#     name = arrName[4]
# print(name)

# debug
se = pygame.mixer.Sound("pi.wav")

##################### set up for mcp3008 ##############################

spi = spidev.SpiDev()
# spi.open(bus,device)
spi.open(0, 0)
spi.max_speed_hz = 1000000

vref = 5.0 # MCP3008 の Vref に入れた電圧. ここでは 5V
try:
    while True:
        data = readAdc(0, spi)
        volts = convertVolts(data, vref)
        print(volts)
        # if volts > 1:
        #     playSE(se)
        # MCP3008 の Vref に入れた電圧. ここでは 5V
        # time.sleep(0.1)

except KeyboardInterrupt:
        print('!FINISH!')

