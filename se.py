import pygame.mixer
import time

pygame.mixer.init()
pygame.mixer.music.load('se2.mp3')
pygame.mixer.music.play(1) # loop count

time.sleep(2)   #20秒再生
pygame.mixer.music.stop()  #停止