#!/usr/bin/python3

from machine import Pin

def get_pin():
    pass

def setup_sensor(pin):
    motion = Pin(pin, Pin.IN)
    
    return motion

def main():
    pin = 1
    motion = setup_sensor(pin)


if __name__=='__main__':
    main()
