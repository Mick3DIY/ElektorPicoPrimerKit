# Elektor Pico Primer Kit in CircuitPython (magnetic relay with push buttons example)
# GitHub project : https://github.com/Mick3DIY/ElektorPicoPrimerKit
# Raspberry Pi Pico : https://www.raspberrypi.com/products/raspberry-pi-pico/
# Documentation, tutorials : https://projects.raspberrypi.org
# CircuitPython : https://learn.adafruit.com/welcome-to-circuitpython
# Thonny IDE : https://thonny.org

# Common file for the TFT LCD screen
import tft_display

# https://docs.circuitpython.org/en/latest/shared-bindings/board/
import board

# https://docs.circuitpython.org/en/latest/shared-bindings/digitalio/
from digitalio import DigitalInOut, Direction, Pull

# https://docs.circuitpython.org/en/latest/shared-bindings/time/
import time

# Initialize the screen
display, splash = tft_display.init_display("Magnetic relay test\nwith push buttons", bg_color=tft_display.TFT_RED, text_color=tft_display.TFT_WHITE, text_scale=1)

# From the schematic, the buttons, LEDs pins are made with +3,3V (sinking method) by default
# They turns ON when the pin is set to LOW !
# Buttons K1 -> K3
button_K1 = DigitalInOut(board.GP2)
button_K1.direction = Direction.INPUT
button_K1.pull = Pull.UP
button_K2 = DigitalInOut(board.GP3)
button_K2.direction = Direction.INPUT
button_K2.pull = Pull.UP
button_K3 = DigitalInOut(board.GP22)
button_K3.direction = Direction.INPUT
button_K3.pull = Pull.UP
# Magnetic relay on GP26 (CN5)
relay = DigitalInOut(board.GP26)
relay.direction = Direction.OUTPUT
relay_state = False
# Button K2 state
prev_button_K2_state = True

try:
    while True:
        curr_button_K2_state = button_K2.value
        # Button K1 switch ON (temporary) the magnetic relay (if he's not already ON)
        if button_K1.value:
            if relay_state == False:
                relay.value = False
        else:
            if relay_state == False:
                relay.value = True
                tft_display.show_text(splash, "Relay is \nON TMP")
                print("Relay : ON TMP") # Prints for the Thonny IDE terminal
        # Button K2 switch ON or OFF the magnetic relay
        if curr_button_K2_state == False and prev_button_K2_state == True:
            relay_state = not relay_state # Toggle relay state
            relay.value = relay_state
            text_state = ("OFF", "ON")[relay_state]
            tft_display.show_text(splash, "Relay is {text_state}")
            print(f"Relay : {text_state}")
        prev_button_K2_state = curr_button_K2_state
        time.sleep(0.05) # Debounce delay
except KeyboardInterrupt:
    pass
