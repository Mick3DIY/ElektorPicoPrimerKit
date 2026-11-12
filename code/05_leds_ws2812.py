# Elektor Pico Primer Kit in CircuitPython (strip LEDs example)
# GitHub project : https://github.com/Mick3DIY/ElektorPicoPrimerKit
# Raspberry Pi Pico : https://www.raspberrypi.com/products/raspberry-pi-pico/
# Documentation, tutorials : https://projects.raspberrypi.org
# CircuitPython : https://learn.adafruit.com/welcome-to-circuitpython
# Thonny IDE : https://thonny.org

# Common file for the TFT LCD screen
import tft_display

# https://docs.circuitpython.org/en/latest/shared-bindings/board/
import board

# https://docs.circuitpython.org/projects/neopixel/en/latest/
import neopixel

# https://docs.circuitpython.org/en/latest/shared-bindings/time/
import time

# Initialize the screen
display, splash = tft_display.init_display(
    "Strip LEDs with\nRGB colors",
    bg_color=tft_display.TFT_RED,
    text_color=tft_display.TFT_WHITE,
    text_scale=1,
)

# 8 LEDs on the strip
num_leds = 8
# Strip LEDs on GP16 (CN6), pixel[0] -> pixel[7]
pixel = neopixel.NeoPixel(board.GP16, num_leds, brightness=0.25, auto_write=False)


def fade_leds(color, text):
    """Fade up LEDS from 0 to 255"""
    tft_display.show_text(splash, "LEDs fade\nup to :\n" + text)
    print("LEDs fade up to : " + text)  # Prints for the Thonny IDE terminal
    for j in range(256):
        pixel.fill(color(j))
        pixel.show()
        time.sleep(0.01)


try:
    while True:
        fade_leds(lambda j: (j, 0, 0), "Red")
        fade_leds(lambda j: (0, j, 0), "Green")
        fade_leds(lambda j: (0, 0, j), "Blue")
except KeyboardInterrupt:
    fade_leds(lambda j: (0, 0, 0), "")  # Black to switch "OFF" LEDs
    pass
