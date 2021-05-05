import RPi.GPIO as GPIO
import time
import _thread
import serial 
import os
import threading
#from adafruit_servokit import ServoKit
# arduino = serial.Serial('/dev/ttyACM1', 9600, timeout=10)
# myKit=ServoKit(channels=16)

GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
my_pwm=GPIO.PWM(32,50)
my_pwm.start(0)
my_pwm1=GPIO.PWM(33,50)
my_pwm1.start(0)


arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=10)
#myKit=ServoKit(channels=16)
val = 1
FrontLeft = 0
FrontRight = 0
BackRight =0
BackLeft = 0
speed1 = 0
speed2 = 0

def forward():
    
    global speed1
    global speed2
    GPIO.setup(11,GPIO.OUT)
    GPIO.setup(12,GPIO.OUT)
    GPIO.output(11,True)
    GPIO.output(12,False)
    speed1=50
    speed2=50

def forwardleft():
    global speed1
    global speed2
    GPIO.output(11,True)
    GPIO.output(12,False)
    speed1=10
    speed2=50
    

def forwardright():
    global speed1
    global speed2
    GPIO.output(11,True)
    GPIO.output(12,False)
    speed1=50
    speed2=10

def backwardleft():
    global speed1
    global speed2
    GPIO.output(11,False)
    GPIO.output(12,True)
    speed1=10
    speed2=50

def backwardright():
    global speed1
    global speed2
    GPIO.output(11,False)
    GPIO.output(12,True)
    speed1=50
    speed2=10

def backward():
    global speed1
    global speed2
    GPIO.output(11,False)
    GPIO.output(12,True)
    speed1=50
    speed2=50

def stop():
    global speed1
    global speed2
    GPIO.output(11,False)
    GPIO.output(12,True)
    speed1=0
    speed2=0

def turnleft():
    for i in range (1,3,1):
        forwardleft()
        time.sleep(1)
        backwardright()
        time.sleep(1)

def turnright():
    for i in range (1,3,1):
        forwardright()
        time.sleep(1)
        backwardleft()
        time.sleep(1)

# def pwmstarter1():
#     global speed1
#     my_pwm.ChangeDutyCycle(speed1)

# def pwmstarter2():
#     global speed2
#     GPIO.output(18,False)
#     print(speed2)
#     GPIO.output(18,True)
#     time.sleep(0.02*speed2)
#     GPIO.output(18,False)
#     time.sleep(0.02*(100-speed2))

def main1() :
    while True:
        
        global val
        global FrontLeft
        global FrontRight
        print("thread1 running............................... \n")
        # elif (val == 3):
        #     BackRight = distance
        #     val = 4
        # elif (val == 4):
        #     BackLeft = distance
            
        #     val = 1

        if (FrontRight < 30 and FrontLeft < 30):
            backward()
            time.sleep(2)
            if (FrontRight >= FrontLeft):
                turnright()
            else:
                turnleft()
        elif (FrontRight < 25):
            turnleft()
        
        elif (FrontLeft < 25):
            turnright()
        else:
            forward()

def mainread():
    
    while True:
        global val
        global FrontLeft
        global FrontRight
        print("threadread running")
        for i in range (1,2,1):
                serial.Serial.reset_input_buffer
                data = arduino.readline()
                #if data:
                #print(data)
                numbers = data.decode('utf-8')
                arr = []
                for word in numbers.split():
                    if word.isdigit():
                        arr.append(int(word))
                # for element in data:
                #     numbers=numbers+element
                # print("\n")
                # numbers = numbers[0:4]
                if (len(arr)==0):
                    continue
                distance = arr[0]
                
                if (val == 1):
                    FrontRight = distance
                    val = 2
                elif (val == 2):
                    FrontLeft = distance
                    val = 1
                    print(FrontRight, FrontLeft)

def main2():
    while True:
        global speed1
        my_pwm.ChangeDutyCycle(speed1)
        print(speed1)
        print("thread2 running \n")
def main3():
    while True:
        global speed2
        my_pwm1.ChangeDutyCycle(speed2)
        print(speed2)
        print("thread3 running \n")

if __name__=="__main__":
    time.sleep(1)
    thread0 = threading.Thread(target=mainread)
    thread1 = threading.Thread(target=main1)
    thread2 = threading.Thread(target=main2)
    thread3 = threading.Thread(target=main3)
    thread0.start()
    thread1.start()
    thread2.start()
    thread3.start()