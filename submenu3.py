#!/usr/bin/python

import os
import callvidsub3
import subprocess
import time
import RPi.GPIO as GPIO

#subprocess.run(['setterm', '-blank', 'force'])  # doesn't capture output

#set up GPIO using BCM numbering

GPIO.setmode(GPIO.BCM)
#All Gpio's as input and pull up

GPIO.setup(22, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(17, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(5, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(6, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down = GPIO.PUD_UP)

#Start menu
myprocess = subprocess.Popen(['omxplayer','--no-osd','--win','0,0,1920,1080','--loop', '/mnt/usb/sub3/menusub3.mp4'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE, close_fds=True)
cmd = '/mnt/usb/./scotttv.py'
while True:

      if GPIO.input(17) ==0:
           myprocess.communicate(b"q")
           callvidsub3.tata("01.mp4")
           os.execv(cmd, [''])
           time.sleep(5)

      if (GPIO.input(27) == 0):
            myprocess.communicate(b"q")
            callvidsub3.tata("02.mp4")
            os.execv(cmd, [''])
            time.sleep(5)

      if (GPIO.input(22) == 0):
            myprocess.communicate(b"q")
            callvidsub3.tata("03.mp4")
            os.execv(cmd, [''])
            time.sleep(5)
      
      if (GPIO.input(13) == 0):
            myprocess.communicate(b"q")
            callvidsub3.tata("04.mp4")
            os.execv(cmd, [''])
            time.sleep(5)

      if (GPIO.input(6) == 0):
            myprocess.communicate(b"q")
            callvidsub3.tata("05.mp4")
            os.execv(cmd, [''])
            time.sleep(5)

      if (GPIO.input(5) == 0):
            myprocess.communicate(b"q")
            callvidsub3.tata("06.mp4")
            os.execv(cmd, [''])
            time.sleep(5)


GPIO.cleanup()

