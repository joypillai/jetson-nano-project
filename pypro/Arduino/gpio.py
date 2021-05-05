import RPi.GPIO as GPIO
import time
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.output(11,False)
GPIO.output(12,False)
my_pwm=GPIO.PWM(32,100)
my_pwm.start(1)
my_pwm1=GPIO.PWM(33,100)
my_pwm1.start(1)

GPIO.output(11,True)
GPIO.output(12,False)

while True:
    my_pwm.ChangeDutyCycle(0)
    my_pwm1.ChangeDutyCycle(0)