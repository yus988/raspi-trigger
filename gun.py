# 銃撃時に振動をならすスクリプト
# スイッチを押したら音がなる。はじめに鳴らす音を 1, 2, 3, 4, 5 で指定

import pygame.mixer
import time
import RPi.GPIO as GPIO
from time import perf_counter

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


# arrSe = pygame.sndarray.samples(sndArr)
# print(arrSe)

# Pin Number
TACT_GPIO = 19
GPIO.setmode(GPIO.BCM)
GPIO.setup(TACT_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def playSE(se):
    se.play()  # loop count
    time.sleep(0.5)  # 一定時間再生
    pygame.mixer.music.stop()  # 停止

# GPIO.add_event_detect(TACT_GPIO, GPIO.RISING, callback=playSE, bouncetime=1)


seType = input("input type num : ")
if seType == "1":
    se = se1
    name = arrName[0]
elif seType == "2":
    se = se2
    name = arrName[1]
elif seType == "3":
    se = se3
    name = arrName[2]
elif seType == "4":
    se = se4
    name = arrName[3]
elif seType == "5":
    se = se5
    name = arrName[4]

print(name)


try:
    while True:
        # time.sleep(1)
        if GPIO.input(TACT_GPIO) == 0:
            # print("before play",perf_counter())
            playSE(se)

except KeyboardInterrupt:
    GPIO.cleanup()
    print("Finished and clean up GPIO")
    # estart python