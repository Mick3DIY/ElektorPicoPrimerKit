# ElektorPicoPrimerKit in CircuitPython (V9)
# GitHub project : https://github.com/Mick3DIY/ElektorPicoPrimerKit
# Raspberry Pi Pico : https://www.raspberrypi.com/products/raspberry-pi-pico/
# Documentation, tutorials : https://projects.raspberrypi.org
# CircuitPython : https://learn.adafruit.com/welcome-to-circuitpython
# Thonny IDE : https://thonny.org

# https://docs.circuitpython.org/en/latest/shared-bindings/board/
import board

# https://docs.circuitpython.org/en/latest/shared-bindings/busio/
import busio

# https://docs.circuitpython.org/en/latest/shared-bindings/displayio/
import displayio

# https://docs.circuitpython.org/en/latest/shared-bindings/fourwire/
from fourwire import FourWire

# https://docs.circuitpython.org/projects/st7735r/en/latest/
from adafruit_st7735r import ST7735R

# https://docs.circuitpython.org/projects/display_text/en/latest/
from adafruit_display_text import label

# https://docs.circuitpython.org/en/latest/shared-bindings/terminalio/
import terminalio