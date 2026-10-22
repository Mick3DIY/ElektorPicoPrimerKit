# Elektor Pico Primer Kit in CircuitPython (common code for the TFT LCD screen)
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
# Don't forget to install this library (.mpy file) in the Pico "/lib" folder
from adafruit_st7735r import ST7735R as TFT_ST

# https://docs.circuitpython.org/projects/display_text/en/latest/
# Don't forget to install this library (folder) in the Pico "/lib" folder
from adafruit_display_text import label

# https://docs.circuitpython.org/en/latest/shared-bindings/terminalio/
import terminalio


def init_display(splash_text="Pico\nPrimer\nKit", bg_color=0x000000, text_color=0xFFFF00, text_scale=2, pos_x=5, pos_y=15):
    """Initialise the display and show a default message
    Return (display, splash)
    """
    # Connection pins for the SPI interface (from Makerfabs)
    tft_sck = board.GP10    # SPI/SCK Serial Clock signal (from the Pico)
    tft_mosi = board.GP11   # SPI/TX Main Out Selected In (data line)
    tft_miso = board.GP12   # SPI/RX Main In Selected Out (data line)
    tft_cs = board.GP13     # SPI/CS Chip Select (which display)
    tft_dc = board.GP14     # SPI/DC Data Command (command, data)
    tft_reset = board.GP15  # SPI/RESET Reset the display controller

    # Release all active used displays
    displayio.release_displays()
    # Define the SPI bus (3 wires serial protocol)
    tft_spi = busio.SPI(clock=tft_sck, MOSI=tft_mosi, MISO=tft_miso)
    # Manage the display over SPI
    display_bus = FourWire(tft_spi, command=tft_dc, chip_select=tft_cs, reset=tft_reset)
    # Define the ST7735R driver
    display = TFT_ST(
        display_bus, width=130, height=160  # A bit larger than the screen display
    )
    # Create a new "sprite" group
    splash = displayio.Group()
    display.root_group = splash
    # Background color
    bitmap = displayio.Bitmap(display.width, display.height, 1)
    palette = displayio.Palette(1)
    palette[0] = bg_color
    # Add a new tile
    bg_sprite = displayio.TileGrid(bitmap, pixel_shader=palette, x=0, y=0)
    splash.append(bg_sprite)
    # Add the default text message
    text_label = label.Label(
        terminalio.FONT, text=splash_text, color=text_color, scale=text_scale, x=pos_x, y=pos_y
    )
    splash.append(text_label)
    return display, splash


def show_text(splash, splash_text, text_color=0xFFFF00, text_scale=2, pos_x=5, pos_y=15):
    """Replace the default message"""
    for i in range(len(splash) - 1, -1, -1):
        if isinstance(splash[i], label.Label):
            splash.pop(i)
    text_label = label.Label(
        terminalio.FONT, text=splash_text, color=text_color, scale=text_scale, x=pos_x, y=pos_y
    )
    splash.append(text_label)