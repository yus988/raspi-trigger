import pygame.mixer
import time
import RPi.GPIO as GPIO

pygame.mixer.init()
pygame.mixer.music.load('se1.mp3')

# Pin Number
TACT_GPIO = 19

GPIO.setmode(GPIO.BCM)
GPIO.setup(TACT_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def playSE():
    pygame.mixer.music.play(1) # loop count
    time.sleep(2)   #20秒再生
    pygame.mixer.music.stop()  #停止

# GPIO.add_event_detect(TACT_GPIO, GPIO.RISING, callback=playSE, bouncetime=1)

try: 
    while True:
        time.sleep(0) 
        if GPIO.input(TACT_GPIO) == 0:
            playSE()
            
except KeyboardInterrupt:
        GPIO.cleanup()
        print("Finished and clean up GPIO")
    