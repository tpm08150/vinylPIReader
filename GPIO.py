import RPi.GPIO as GPIO
import time
import board
import neopixel
import cv2

cap = cv2.VideoCapture(0)


pixel_pin = board.D18
ORDER = neopixel.GRB
num_pixels = 1
pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=True, pixel_order=ORDER
)

SwitchA=4
GPIO.setmode(GPIO.BCM)
GPIO.setup(SwitchA, GPIO.IN)

while True:
    ret, frame = cap.read()
    if GPIO.input(SwitchA)==False:
        print("You are pressing button A")
        cv2.imwrite('image.jpg', frame)
        pixels.fill((255, 0, 0))
    else:
        pixels.fill((0, 0, 0))
    cap.release()