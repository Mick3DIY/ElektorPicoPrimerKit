# Elektor Pico Primer Kit in CircuitPython (Inertial Measure Unit example)
# GitHub project : https://github.com/Mick3DIY/ElektorPicoPrimerKit
# Raspberry Pi Pico : https://www.raspberrypi.com/products/raspberry-pi-pico/
# Documentation, tutorials : https://projects.raspberrypi.org
# CircuitPython : https://learn.adafruit.com/welcome-to-circuitpython
# Thonny IDE : https://thonny.org

# Common file for the TFT LCD screen
import tft_display

# https://docs.circuitpython.org/en/latest/shared-bindings/board/
import board

# https://docs.circuitpython.org/en/latest/shared-bindings/busio/
import busio

# https://docs.circuitpython.org/projects/register/en/latest/
# Don't forget to install this folder in the Pico "/lib" folder (adafruit_mpu6050 dependency)
# https://docs.circuitpython.org/projects/mpu6050/en/latest/
# Don't forget to install this library (.mpy file) in the Pico "/lib" folder
from adafruit_mpu6050 import MPU6050

# https://docs.circuitpython.org/en/latest/shared-bindings/time/
import time

# Inertial Measure Unit on GP9, GP8 (CN3)
i2c = busio.I2C(board.GP9, board.GP8)
mpu = MPU6050(i2c, address=0x68)
