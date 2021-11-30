from machine import Pin PWM
from time import sleep
servo=PWM(pin 0,frequency)
frequency=5000
while True:
  for duty_cycle in range(0,1023)
  servo.duty(duty_cycle)
  sleep(1)
  
