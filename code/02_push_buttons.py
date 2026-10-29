# Elektor Pico Primer Kit in CircuitPython
# GitHub project : https://github.com/Mick3DIY/ElektorPicoPrimerKit
# Raspberry Pi Pico : https://www.raspberrypi.com/products/raspberry-pi-pico/
# Documentation, tutorials : https://projects.raspberrypi.org
# CircuitPython : https://learn.adafruit.com/welcome-to-circuitpython
# Thonny IDE : https://thonny.org

# Common file for the TFT LCD screen
import tft_display

# https://docs.circuitpython.org/en/latest/shared-bindings/board/
import board

# https://docs.circuitpython.org/en/latest/shared-bindings/digitalio/index.html
from digitalio import DigitalInOut, Direction, Pull

# Initialise the screen
display, splash = tft_display.init_display("Push buttons test\nwith LEDs", bg_color=tft_display.TFT_RED, text_color=tft_display.TFT_WHITE, text_scale=1)

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
# LEDs LED1 -> LED3
led1 = DigitalInOut(board.GP18)
led1.direction = Direction.OUTPUT
led1.value = True
led2 = DigitalInOut(board.GP19)
led2.direction = Direction.OUTPUT
led2.value = True
led3 = DigitalInOut(board.GP20)
led3.direction = Direction.OUTPUT
led3.value = True
# Buzzer (with a MOSFET NMOS, it turn ON when the pin is set to HIGH !)
buzzer = DigitalInOut(board.GP4)
buzzer.direction = Direction.OUTPUT

try:
    while True:
        if button_K1.value:
            led1.value = True
        else:
            led1.value = False
            tft_display.show_text(splash, "K1")
            print("Button K1") # Prints for the Thonny IDE terminal
        if button_K2.value:
            led2.value = True
        else:
            led2.value = False
            tft_display.show_text(splash, "K2")
            print("Button K2")
        if button_K3.value:
            led3.value = True
        else:
            led3.value = False
            tft_display.show_text(splash, "K3")
            print("Button K3")
        # Buttons K1 + K3 to switch ON the buzzer
        if not button_K1.value and not button_K3.value:
            buzzer.value = True
            print("Buzzzzzer !")
        else:
            buzzer.value = False
except KeyboardInterrupt:
    pass
