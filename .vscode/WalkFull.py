#!/usr/bin/env python3
#add imports
from ev3dev2.wheel import *
from ev3dev2.sensor.lego import *
from ev3dev2.sound import *
from time import *
from ev3dev2.motor import *
from ev3dev2.sensor import *
def inToCm(inch):
    return inch*2.54
#create the child class of MoveTank, MoveDifferential. Creates new wheel class that you can adjust the width and diameter. 
class newTire(Wheel):
  def __init__(self):
    super().__init__(43.2,22)
STUD_MM = 8

#IF TURNING IS NOT ACCURATE AT ALL: 
#Change the movedifferential function, (number * stud_mm) to affect the amount turned

m = MoveDifferential(OUTPUT_D, OUTPUT_B, newTire, 15 * STUD_MM)
#calibrate the Gyro
gyro = GyroSensor()
gyro.reset()
gyro.calibrate()
#Create the function, correct that corrects the turn to the targetAngle from the angle (the current angle)
def correct(targetAngle, angle):
    #only applicable if m.turnRight is used
    while(abs(gyro.angle) != targetAngle):
        if(gyro.angle > targetAngle):
            m.turn_left(SpeedRPM(10),1)
        else:
            m.turn_right(SpeedRPM(10),1)
        time.sleep(.1)
        if(abs(gyro.angle) == targetAngle):
            break
#subtak1a function is a void that takes the parameter, length of the line it needs to go, in mm, and repeat, the number of times it needs to repeat 
def subtask1a(length, repeat):
  for k in range(repeat):
    m.on_for_distance(SpeedRPM(40), length)
    print(gyro.angle)
    m.on_for_distance(SpeedRPM(-40), length)
#Calls the function
def goForward(length):
   m.on_for_distance(SpeedRPM(40), length)
def goForwardRepeat(length, repeat, wait):
   for i in range(repeat):
      m.on_for_distance(SpeedRPM(40), length)
      time.sleep(wait)



goForward(inToCm(12), 1)
