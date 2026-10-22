# Elektor Pico Primer Kit in CircuitPython
# GitHub project : https://github.com/Mick3DIY/ElektorPicoPrimerKit
# Raspberry Pi Pico : https://www.raspberrypi.com/products/raspberry-pi-pico/
# Documentation, tutorials : https://projects.raspberrypi.org
# CircuitPython : https://learn.adafruit.com/welcome-to-circuitpython
# Thonny IDE : https://thonny.org

# Common file for the TFT LCD screen
import tft_display

# Only one call to check the screen
tft_display.init_display(bg_color=0xFF0000, text_color=0xFFFFFF) # RGB colors in hexadecimal