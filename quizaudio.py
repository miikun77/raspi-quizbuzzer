import RPi.GPIO as GPIO
from time import sleep
from pygame import mixer

# Set variables
# These are BCM GPIO number on the board (NOT Physical number)
# Please visit https://www.pinout.xyz

btn1 = 4
btn2 = 27
btn3 = 10
btn4 = 5

led1 = 17
led2 = 22
led3 = 9
led4 = 6

# GPIO settings
GPIO.setmode(GPIO.BCM)
GPIO.setup(btn1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(btn2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(btn3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(btn4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)
GPIO.setup(led4, GPIO.OUT)

# Set up pygame.mixer.Sound
mixer.init()
buz_sound = mixer.Sound("buzzer.wav")


# Check Ready
# Check if the LEDs and buzzer work
GPIO.output(led1,True)
GPIO.output(led2,True)
GPIO.output(led3,True)
GPIO.output(led4,True)
sleep(2)
GPIO.output(led1,False)
GPIO.output(led2,False)
GPIO.output(led3,False)
GPIO.output(led4,False)

# When you want to exit, press Ctrl & C
try:
	while True:
		# The LED will turn on after the button is pressed.
		# The sound will be played to the external output, and the LEd will turn off after 5 seconds.
		if GPIO.input(btn1):
			GPIO.output(led1, True)
			buz_sound.play()
			sleep(5)
			GPIO.output(led1, False)
		
		if GPIO.input(btn2):
			GPIO.output(led2, True)
			buz_sound.play()
			sleep(5)
			GPIO.output(led2, False)

		if GPIO.input(btn3):
			GPIO.output(led3, True)
			buz_sound.play()
			sleep(5)
			GPIO.output(led3, False)
		
		if GPIO.input(btn4):
			GPIO.output(led4, True)
			buz_sound.play()
			sleep(5)
			GPIO.output(led4, False)

except KeyboardInterrupt:
	GPIO.cleanup()
	print("Bye!")

