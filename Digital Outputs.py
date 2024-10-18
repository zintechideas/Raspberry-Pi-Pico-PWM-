from machine import Pin
from time import sleep

led = Pin(21, Pin.OUT)
button = Pin(20, Pin.IN, Pin.PULL_DOWN)

while True:
  led.value(button.value())
  sleep(0.1)
  print(button.value())