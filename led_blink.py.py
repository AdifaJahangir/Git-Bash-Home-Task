import time
import machine

led = machine.Pin(2, machine.Pin.OUT)

while True:
    led.value(1)  # Turn LED on
    time.sleep(1)  # Wait 1 second
    led.value(0)  # Turn LED off
    time.sleep(1)  # Wait 1 second
