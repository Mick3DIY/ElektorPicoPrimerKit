## Example codes

> [!TIP]
> First of all, you need to install CircuitPython (version 10.x, stable version) in your Raspberry Pi Pico !
>
> Follow this link for instructions and download it (in your language) :
> https://circuitpython.org/board/raspberry_pi_pico/
>
> The TFT LCD screen need external libraries (.mpy files) in the Pico "/lib" folder : `adafruit_st7735r`, `adafruit_display_text`.
> Don't forget to install it, check the file `tft_display.py` or install the CircuitPython Library Bundle (version 10.x) :
> https://circuitpython.org/libraries
>
> To upload example codes and run them in your Pico, you need a simple software like Tonny IDE : https://thonny.org

First test before anything else :

* `01_check_screen.py` : checking the TFT LCD screen (with the common code from `tft_display.py`)

If you don't have any error and see the default message, explore the other codes :

* `02_push_buttons.py` : using the onboard LEDs and buzzer

* `03_potentiometer.py` : using the slide potentiometer

* `04_relay.py` : using the magnetic relay with buttons

* `05_leds_ws2812.py` : using the strip of 8 LEDs (WS2812)