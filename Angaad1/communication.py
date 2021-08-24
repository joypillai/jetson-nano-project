import RPi.GPIO as GPIO
import time
import _thread
import serial 
import os
import threading

arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=10)
val = 1
Front = 0
Back = 0
Right = 0
Left = 0
stopBot = 0

def main1() :
    while True:
        
        global val
        global Left
        global Right
        global Front
        global Back
        global stopBot
        #print("thread1 running \n")
        for i in range (1,2,1):
            
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
                Front = distance
                val = 2
            elif (val == 2):
                stopBot = distance
                val = 1
                
            # elif (val == 3):
            #     Back = distance
            #     val = 4
            # elif (val == 4):
            #     Left = distance
            #     val = 1
                print(stopBot)
                print("\n")
                
            if (stopBot==1):
                #time.sleep(5)
                arData='Y'
                byteData=bytes(arData, 'utf-8')
                arduino.write(byteData)
                stopBot=0
                arData='N'
            else:
                arData='N'
                byteData=bytes(arData, 'utf-8')
                arduino.write(byteData)

            serial.Serial.reset_input_buffer
            time.sleep(0.05)
        
if __name__=="__main__":
    thread1 = threading.Thread(target=main1)
    thread1.start()