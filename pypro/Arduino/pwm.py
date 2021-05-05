import RPi.GPIO as GPIO
import time
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
my_pwm=GPIO.PWM(33,100)
my_pwm.start(1)
x=1
# for i in range(1,99,1):  
#     my_pwm.ChangeDutyCycle(i)
#     time.sleep(0.5)
#     print(i)
# for i in range(99,1,-1):  
#     my_pwm.ChangeDutyCycle(i)
#     time.sleep(0.5)
#     print(i)

for i in range(1,99,1):  
    #my_pwm.ChangeDutyCycle(i)
    time.sleep(0.5)
    print(i)
    

