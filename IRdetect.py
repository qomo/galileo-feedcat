#!/usr/bin/env python
import sys

#galileo_path = "/media/mmcblk0p1/";
#if galileo_path not in sys.path:
#    sys.path.append(galileo_path);

from pyGalileo import *
'''/*
  Button
 
 Turns on and off a light emitting diode(LED) connected to digital  
 pin 13, when detect someone get close to the senser attached to pin 4. 
 
 
 The circuit:
 * LED attached from pin 13 to ground 
 * IRdetect senser attached to pin 2 5V and GND
 
 * Note: on most Arduinos there is already an LED on the board
 attached to pin 13.
 
 created 2005
 by DojoDave <http://www.0j0.org>
 modified 30 Aug 2011
 by Tom Igoe
 modified 27 Aug 2014
 by QomoLiao
 
 This example code is in the public domain.
 
 http://www.arduino.cc/en/Tutorial/Button
 */'''

#// constants won't change. They're used here to 
#// set pin numbers:
#const int buttonPin = 2;     // the number of the pushbutton pin
irPin = 4;
#const int ledPin =  13;      // the number of the LED pin
ledPin =  13;

#// variables will change:
#int buttonState = 0;         // variable for reading the pushbutton status
irState = 0;

#void setup() {
def setup():
  #// initialize the LED pin as an output:
  pinMode(ledPin, OUTPUT);      
  #// initialize the pushbutton pin as an input:
  pinMode(irPin, INPUT);     
#}

#void loop(){
def loop():
  while(1):
      #// read the state of the pushbutton value:
      irState = digitalRead(irPin);

      #// check if the pushbutton is pressed.
      #// if it is, the buttonState is HIGH:
      if (irState == HIGH):# {     
        #// turn LED on:    
        digitalWrite(ledPin, HIGH);  
      #} 
      else:# {
        #// turn LED off:
        digitalWrite(ledPin, LOW); 
      #}
#}

setup();
loop();
