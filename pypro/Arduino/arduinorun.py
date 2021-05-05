import serial 
import time
import os
from adafruit_servokit import ServoKit

arduino = serial.Serial('/dev/ttyACM1', 9600, timeout=10)
myKit=ServoKit(channels=16)

while True:
    
    # if (ack == 1):
    #     arduino.write(bytes('YES\n','utf-8'))
    #     ack = 0
    
    data = arduino.readline()
    if data:
        print(data)
        
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

    print(distance)
   
    
    

    #time.sleep(2)
    #print("\n")
    #print(numbers)
    #if distance > 20:
    #    os.system('python3 /home/jetbot/Desktop/pypro/Arduino/gpio.py')    

    