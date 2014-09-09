#!/usr/bin/env python
# coding=utf-8

import sys
from pyGalileo import *

servoPin = 5

def delaymicro(mcTime):
    """
    delaymicro(mcTime)

    Description:
        Delays the execution of the script for number of microseconds.

    Input:
        mcTime - (int) number of microseconds to delay
    Returns:
        None
    Example:
        delaymicro(500);    - Delay the script for 500 microseconds.
    """
    time.sleep(mcTime/1000000);

def setup():
    pinMode(servoPin, OUTPUT)

def loop():
    while(1):
        digitalWrite(servoPin, HIGH)
        delaymicro(1500)
        digitalWrite(servoPin, LOW)
        delay(20)

setup()
loop()
