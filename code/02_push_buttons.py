# Elektor Pico Primer Kit in CircuitPython
# GitHub project : https://github.com/Mick3DIY/ElektorPicoPrimerKit
# Raspberry Pi Pico : https://www.raspberrypi.com/products/raspberry-pi-pico/
# Documentation, tutorials : https://projects.raspberrypi.org
# CircuitPython : https://learn.adafruit.com/welcome-to-circuitpython
# Thonny IDE : https://thonny.org

# Common file for the TFT LCD screen
import tft_display

# Initialise the screen
display, splash = tft_display.init_display("Push buttons test\nwith LEDs", bg_color=0xFF0000, text_color=0xFFFFFF, text_scale=1)
