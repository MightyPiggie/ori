import RPi.GPIO as GPIO
import time
import datetime

GPIO.setmode( GPIO.BCM )
GPIO.setwarnings( 0 )

print( "sr04 print" )

sr04_trig = 20
sr04_echo = 21

GPIO.setup( sr04_trig, GPIO.OUT )
GPIO.setup( sr04_echo, GPIO.IN, pull_up_down=GPIO.PUD_DOWN )

def sr04( trig_pin, echo_pin ):
   """
   Return the distance in cm as measured by an SR04
   that is connected to the trig_pin and the echo_pin.
   These pins must have been configured as output and input.s
   """

   # send trigger pulse    
   GPIO.output(trig_pin, GPIO.HIGH)
   
   # wait for echo high and remember its start time
   time.sleep(0.00001)
   GPIO.output(trig_pin, GPIO.LOW)
 
   start_tijd = time.time()
   stop_tijd = time.time()
   
   while GPIO.input(echo_pin) == GPIO.LOW:
      start_tijd = time.time()
   
   # wait for echo low and remember its end time
   while GPIO.input(echo_pin) == GPIO.HIGH:
      stop_tijd = time.time()

   # calculate and return distance
   totale_tijd = stop_tijd - start_tijd
   afstand = (totale_tijd * 34300) / 2

   return afstand

while True:
   print( sr04( sr04_trig, sr04_echo ))
   time.sleep( 0.5 )
