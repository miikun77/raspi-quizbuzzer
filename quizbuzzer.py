import RPi.GPIO as GPIO
from time import sleep

# set variable
# These are pysical GPIO number on the board
btn1 = 4
btn2 = 27
btn3 = 10
btn4 = 5

led1 = 17
led2 = 22
led3 = 9
led4 = 6

buzzer =  12

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
GPIO.setup(buzzer, GPIO.OUT)

# Check Ready
GPIO.output(led1,True)
GPIO.output(led2,True)
GPIO.output(led3,True)
GPIO.output(led4,True)
sleep(2)
GPIO.output(led1,False)
GPIO.output(led2,False)
GPIO.output(led3,False)
GPIO.output(led4,False)


try:
	while True:
	
		GPIO.output(led1, False)
		GPIO.output(led2, False)
		GPIO.output(led3, False)
		GPIO.output(led4, False)

	
		while True:
			if GPIO.input(btn1):
				GPIO.output(led1, True)
				GPIO.output(buzzer, True)
				sleep(0.5)
				GPIO.output(buzzer, False)
				sleep(5)
				break
			
			if GPIO.input(btn2):
				GPIO.output(led2, True)
				GPIO.output(buzzer, True)
				sleep(0.5)
				GPIO.output(buzzer, False)
				sleep(5)
				break
			
			if GPIO.input(btn3):
				GPIO.output(led3, True)
				GPIO.output(buzzer, True)
				sleep(0.5)
				GPIO.output(buzzer, False)
				sleep(5)
				break
			
			if GPIO.input(btn4):
				GPIO.output(led4, True)
				GPIO.output(buzzer, True)
				sleep(0.5)
				GPIO.output(buzzer, False)
				sleep(5)
				break

except KeyboardInterrupt:
	GPIO.cleanup()
	print("Bye!")

