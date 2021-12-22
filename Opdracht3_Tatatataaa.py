import RPi.GPIO as GPIO
import time
GPIO.setmode( GPIO.BCM )
GPIO.setwarnings( 0 )

print( "GPIO pulse" )

def pulse(pin_nr, high_time, low_time):
    """
    Geef een puls op de pin:
    Maak de pin pin_nr hoog, wacht high_time,
    maak de pin laag, en wacht nog low_time
    """

    GPIO.output(pin_nr, GPIO.HIGH)
    time.sleep(high_time)
    GPIO.output(pin_nr, GPIO.LOW)
    time.sleep(low_time)

n = 1
led = 18

GPIO.setup(led, GPIO.OUT)

while True:
    while n < 4:
        pulse(led, 0.2, 0.2)
        n += 1
    pulse(led, 0.2, 2.0)
    break
