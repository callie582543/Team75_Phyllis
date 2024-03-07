#!/usr/bin/env python3
#adds imports. Albeight it is slightly redundant
from ev3dev2.wheel import *
from ev3dev2.sensor.lego import *
from ev3dev2.sound import *
from time import *
from ev3dev2.motor import *
from ev3dev2.sensor import *
import math 
def inToMm(inch):
    return inch*25.4
#create the child class of MoveTank, MoveDifferential. Creates new wheel class that you can adjust the width and diameter. 
class newTire(Wheel):
  def __init__(self):
    super().__init__(43.2,22)
m = MoveDifferential(OUTPUT_D, OUTPUT_B, newTire, 193)
#calibrate the Gyro
gyro = GyroSensor()
gyro.reset()
gyro.calibrate()
target_angle = 0
#Create the function, correct that corrects the turn to the targetAngle from the angle (the current angle)
def correct(targetAngle, angle):
    #only applicable if m.turnRight is used
#while(abs(gyro.angle) != targetAngle):
    while(abs(gyro.angle) != targetAngle):
        if(abs(gyro.angle) > targetAngle):
            m.turn_left(SpeedRPM(10),1)
        else:
            m.turn_right(SpeedRPM(10),1)
        time.sleep(.1)
        if(abs(gyro.angle) == targetAngle):
            break
#a void function that takes the parameter (degrees) to which it must turn. It calls the correct() function to correct the angle it turns and calibrates it 
def turn(degrees):
    m.turn_right(SpeedRPM(80),degrees)
    print(gyro.angle)
    correct(degrees, gyro.angle)
    time.sleep(1)
    print(gyro.angle)
    gyro.calibrate()
#a function that was used for testing the angle
def testAngle(times):
    for k in range (times):    
        turn(180)
#subtaskB function that takes the parameters, length it must go, and n number of times it will repeat
def subtaskB(length1, length2 , n):
    for k in range(n):
        m.on_for_distance(SpeedRPM(40), length1)
        turn(90)
        m.on_for_distance(SpeedRPM(40), length2)



        
#calls subtaskB
subtaskB(inToMm(12), inToMm(12), 1)
