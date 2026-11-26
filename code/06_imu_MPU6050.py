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
# Adafruit SensorLab - Gyroscope basic calibration
# https://learn.adafruit.com/adafruit-sensorlab-gyroscope-calibration
from adafruit_mpu6050 import MPU6050

# https://docs.circuitpython.org/en/latest/shared-bindings/time/
import time

# Initialize the screen
display, splash = tft_display.init_display(
    "Inertial Measure Unit test",
    bg_color=tft_display.TFT_RED,
    text_color=tft_display.TFT_WHITE,
    text_scale=1,
)

# Inertial Measure Unit on GP9, GP8 (CN3)
# /!\ CircuitPython requires pull-up resistors on SDA and SCL (4,7K Ohms each) /!\
# This IMU module don't have by default for MicroPython
i2c = busio.I2C(board.GP9, board.GP8)
# Module I2C default address is '0x68'
mpu = MPU6050(i2c)

try:
    while True:
        # Acceleration m/s^2
        print(
            f"Acc X:{mpu.acceleration[0]:.2f}, Y:{mpu.acceleration[1]:.2f}, Z:{mpu.acceleration[2]:.2f}"  # Print for the Thonny IDE terminal
        )
        # Gyroscope rad degrees/s
        print(f"Gyro X:{mpu.gyro[0]:.2f}, Y:{mpu.gyro[1]:.2f}, Z:{mpu.gyro[2]:.2f}")
        # Temperature °Celsius
        # print(f"Temp : {mpu.temperature:.2f} C")
        tft_display.show_text(splash, f"IMU Temp:\n{mpu.temperature:.2f}")
        time.sleep(1)
except KeyboardInterrupt:
    pass
