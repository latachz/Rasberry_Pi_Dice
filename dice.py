import RPi.GPIO as GPIO
import time
import random

GPIO.setwarnings(False)

GPIO.cleanup()

GPIO.setmode(GPIO.BCM)

#pins

button = 18
channels = [2, 3, 4, 17, 27, 22]
one = [2]
two = [2, 22]
three =[2, 3, 4]
four = [2, 4, 17, 22]
five = [2, 3, 4, 17, 22]
six = [2, 3, 4, 17, 27, 22]
numbers = [one, two, three, four, five, six]

#setup buttons and leds

GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(channels, GPIO.OUT)

#turn off all leds

GPIO.output(channels, GPIO.OUT)

#button

while True:
    input_state = GPIO.input(button)
    if input_state == True:
        GPIO.output(channels, GPIO.OUT)
        print('Losowanie:')
        time.sleep(.2)
        print('....')
        time.sleep(.2)
        GPIO.output(random.choice(numbers), GPIO.HIGH)
        
