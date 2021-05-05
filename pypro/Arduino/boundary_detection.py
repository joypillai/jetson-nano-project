import serial 
import time
import os

arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=10)


while True:
    
    data = arduino.readline()
    if data:
        print(data)
        #print('Hi Arduino')
        
    numbers = data.decode('utf-8')
    # numbers = data
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
    if distance > 20:
        os.system('python3 /home/jetbot/Desktop/pypro/Arduino/gpio.py')    

    