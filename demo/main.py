#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
# init the EV3 BRICK
ev3 = EV3Brick()

# init a motor at port B.
test_motor = Motor(Port.B)

# Write your program here.

# Play a sound 
ev3.speaker.beep()

test_motor.run_target(500,90)

ev3.speaker.beep(frequency=1000,duration=500)

