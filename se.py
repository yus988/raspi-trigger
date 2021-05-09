import pygame.mixer
import time
import RPi.GPIO as GPIO
from time import perf_counter

pygame.mixer.quit()
pygame.mixer.pre_init(buffer=32)
pygame.mixer.init()

se = pygame.mixer.Sound('gunRaw.wav')
se = pygame.mixer.Sound('gunRawArm.wav')
se = pygame.mixer.Sound('gunRawNeck.wav')
se = pygame.mixer.Sound('gunSamp.wav')
se = pygame.mixer.Sound('gunStime.wav')

# Pin Number
TACT_GPIO = 19

GPIO.setmode(GPIO.BCM)
GPIO.setup(TACT_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def playSE():
    se.play() # loop count
    time.sleep(0.5)   #20秒再生
    pygame.mixer.music.stop()  #停止

# GPIO.add_event_detect(TACT_GPIO, GPIO.RISING, callback=playSE, bouncetime=1)

try: 
    while True:
        # time.sleep(1) 
        if GPIO.input(TACT_GPIO) == 0:
            # print("before play",perf_counter())
            playSE()
            
except KeyboardInterrupt:
        GPIO.cleanup()
        print("Finished and clean up GPIO")