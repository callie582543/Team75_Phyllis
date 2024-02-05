# Description: This is the main file for the EV3 robot. It is the file that is run when the robot is turned on. It is responsible for initializing the robot and running the main loop.
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython


# Create objects here.
ev3 = EV3Brick()


# Write program here.

