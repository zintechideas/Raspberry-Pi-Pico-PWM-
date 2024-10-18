from machine import Pin, ADC
from time import sleep

pot = ADC(Pin(27))

while True:
  pot_value = pot.read_u16() 
  print(pot_value)
  sleep(0.1)