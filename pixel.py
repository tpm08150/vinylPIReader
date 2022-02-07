import board
import neopixel
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

pixel_pin = board.D18
ORDER = neopixel.GRB
num_pixels = 1
pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=True, pixel_order=ORDER
)

pixel.fill((255, 0 ,0))