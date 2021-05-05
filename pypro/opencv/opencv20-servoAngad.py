from adafruit_servokit import ServoKit
import time
myKit=ServoKit(channels=16)
# while True:
#     for i in range(0,,1):
#         myKit.servo[1].angle=i
#         print("clockwise ")
#         print(i)
#         time.sleep(0.01)
#     time.sleep(1)
#     for i in range(60,30,-1):
#         myKit.servo[1].angle=i
#         print("anticlockwise ")
#         print(i)
#         time.sleep(0.01)
#     time.sleep(1)
myKit.servo[2].angle= 0
time.sleep(1)
