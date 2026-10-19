# Elektor Pico Primer Kit in CircuitPython
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
from adafruit_st7735r import ST7735R as TFT_ST

# https://docs.circuitpython.org/projects/display_text/en/latest/
from adafruit_display_text import label

# https://docs.circuitpython.org/en/latest/shared-bindings/terminalio/
import terminalio

# Connection pins for the SPI interface (from Makerfabs)
tft_sck = board.GP10    # SPI/SCK Serial Clock signal (from the Pico)
tft_mosi = board.GP11   # SPI/TX Main Out Selected In (data line)
tft_miso = board.GP12   # SPI/RX Main In Selected Out (data line)
tft_cs = board.GP13     # SPI/CS Chip Select (which display)
tft_dc = board.GP14     # SPI/DC Data Command (command, data)
tft_reset = board.GP15  # SPI/RESET Reset the display controller

# Release all active used displays
displayio.release_displays()
# Bus SPI (3 wires serial protocol)
tft_spi = busio.SPI(clock=tft_sck, MOSI=tft_mosi, MISO=tft_miso)
# Manage the display over SPI 
display_bus = FourWire(tft_spi, command=tft_dc, chip_select=tft_cs, reset=tft_reset)
# Use the ST7735R driver
display = TFT_ST(display_bus, width=130, height=160) # A bit larger than the screen display
# Create a new "sprite" group
splash = displayio.Group()
display.root_group = splash
# Background color (red)
color_bitmap = displayio.Bitmap(display.width, display.height, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0xFF0000 # RGB in hexadecimal
# Create a new tile
bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite)
# Create the text message (yellow)
text_label = label.Label(
    terminalio.FONT, text="Pico\nPrimer\nKit", color=0xFFFF00, scale=2, x=5, y=20
)
splash.append(text_label)
