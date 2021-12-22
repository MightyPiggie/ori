import time
import RPi.GPIO as GPIO

GPIO.setmode( GPIO.BCM ) 
GPIO.setwarnings( 0 )

print("neopixels vlag")

clock_pin = 19
data_pin = 26
nr_leds = 8

GPIO.setup( clock_pin, GPIO.OUT )
GPIO.setup( data_pin, GPIO.OUT )


def apa102_send_bytes( clock_pin, data_pin, bytes ):
   """
   zend de bytes naar de APA102 LED strip die is aangesloten op de clock_pin en data_pin
   """
   for byte in bytes:
      binary = []

      for item in range(0, 8):
         bit = byte % 2 
         binary.insert(0, bit)
         byte = byte // 2
      
      for bit in binary:
         if bit == 1:
            GPIO.output(data_pin, GPIO.HIGH)
         if bit == 0:
            GPIO.output(data_pin, GPIO.LOW)
      
         GPIO.output(clock_pin, GPIO.HIGH)
         GPIO.output(clock_pin, GPIO.LOW) 

def apa102( clock_pin, data_pin, colors ):
   """
   zend de colors naar de APA102 LED strip die is aangesloten op de clock_pin en data_pin
    
   De colors moet een list zijn, met ieder list element een list van 3 integers,
   in de volgorde [ blauw, groen, rood ].
   Iedere kleur moet in de range 0..255 zijn, 0 voor uit, 255 voor vol aan.
    
   bv: colors = [ [ 0, 0, 0 ], [ 255, 255, 255 ], [ 128, 0, 0 ] ]
   zet de eerste LED uit, de tweede vol aan (wit) en de derde op blauw, halve strekte.
   """
 
   apa102_send_bytes( clock_pin, data_pin, [0, 0, 0, 0])

   for color in colors:
      apa102_send_bytes(clock_pin, data_pin, [255])
      apa102_send_bytes(clock_pin, data_pin, color)

   apa102_send_bytes(clock_pin, data_pin, [255, 255, 255, 255])
 
   apa102_send_bytes( clock_pin, data_pin, [0, 0, 0, 0])

blue = [ 128, 0, 0 ]
white = [ 64, 64, 64 ]
red = [ 0, 0, 255 ]

def colors( x, n, on, off ):
   result = []
   
   for i in range( 0, n ):
      if i == x:
           result.append( on )
      else:
           result.append( off )
   
   return result  


def vlag( clock_pin, data_pin, delay, n = 8 ):
   while True:
      for x in range( 0, n ):
         apa102( clock_pin, data_pin, colors( x, n, red, red) )
         time.sleep(0.2)

      for x in range(0,n):
         apa102( clock_pin, data_pin, colors( x, n, white, white ) )
         time.sleep(0.2)

      for x in range(0, n):
         apa102( clock_pin, data_pin, colors( x, n, blue, blue ) )
         time.sleep(0.2)
         
vlag( clock_pin, data_pin, 0.03 )  