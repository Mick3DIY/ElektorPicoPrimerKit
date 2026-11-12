# Elektor Pico Primer Kit in CircuitPython (slide potentiometer example)
# GitHub project : https://github.com/Mick3DIY/ElektorPicoPrimerKit
# Raspberry Pi Pico : https://www.raspberrypi.com/products/raspberry-pi-pico/
# Documentation, tutorials : https://projects.raspberrypi.org
# CircuitPython : https://learn.adafruit.com/welcome-to-circuitpython
# Thonny IDE : https://thonny.org

# Common file for the TFT LCD screen
import tft_display

# https://docs.circuitpython.org/en/latest/shared-bindings/board/
import board

# https://docs.circuitpython.org/en/latest/shared-bindings/analogio/
from analogio import AnalogIn

# https://docs.circuitpython.org/en/latest/shared-bindings/time/
import time

# Initialize the screen
display, splash = tft_display.init_display(
    "Potentiometer test",
    bg_color=tft_display.TFT_RED,
    text_color=tft_display.TFT_WHITE,
    text_scale=1,
)

# Slide potentiometer on GP26 (CN5)
potentiometer = AnalogIn(board.GP26)

try:
    while True:
        # Read the raw value (0-65535)
        raw_value = potentiometer.value
        # Convert to voltage (0.0V - 3.3V)
        voltage = raw_value * (3.3 / 65535)
        print("Min:0", f"Voltage:{voltage:.2f}", "Max:3.5")  # Print for the Thonny IDE terminal and plotter
        tft_display.show_text(splash, f"Voltage:\n{voltage:.2f}")
        time.sleep(0.3)  # Important !
except KeyboardInterrupt:
    pass
