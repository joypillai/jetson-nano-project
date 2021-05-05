import serial
import time
import os
#from adafruit_servokit import ServoKit

arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=10)
#myKit=ServoKit(channels=16)
val = 1
while True:
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
    
    distance = arr[0]
    if (val == 1):
        FrontRight = distance
        val = 2
    elif (val == 2):
        FrontLeft = distance
        val = 3
    elif (val == 3):
        BackRight = distance
        val = 4
    elif (val == 4):
        BackLeft = distance
        print(FrontRight, FrontLeft, BackRight, BackLeft)
        val = 1
    

    #time.sleep(2)
    #print("\n")
    #print(numbers)
    #if distance > 20:
    #    os.system('python3 /home/jetbot/Desktop/pypro/Arduino/gpio.py')    

    