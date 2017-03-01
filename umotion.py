#!/usr/bin/python3

from machine import Pin
import cfg
import msg


def setup_sensor(pin):
    motion = Pin(pin, Pin.IN)

    return motion


def wait_detection(c, motion):
    detections = 0
    server = c['server']
    topic = c['ptopic']
    while detections < 10:
        if motion.value():
            detections += 1
            msg.xmt(server, topic, 'motion detected')
            msg.xmt(server, topic, str(detections))
        else:
            pass


def main():
    c = cfg.read_cfg()
    pin = int(c['pin'])
    motion = setup_sensor(pin)
    wait_detection(c, motion)


if __name__ == '__main__':
    main()
