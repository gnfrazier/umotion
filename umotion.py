#!/usr/bin/python3

from machine import Pin
import cfg
import msg
import time


def setup_sensor(pin):
    motion = Pin(pin, Pin.IN)

    return motion


def wait_detection(c, motion):
    detections = 0
    server = c['server']
    topic = c['ptopic']
    delay = int(c['delay'])
    try:
        while detections < 10:
            if motion.value():
                detections += 1
                msg.xmt(server, topic, 'motion detected')
                msg.xmt(server, topic, str(detections))
                time.sleep(delay)
            else:
                pass
    except Exception as e:
        # log.debug(e)
        #mem = gc.mem_alloc()
        # log.debug(mem)
        gc.collect()
        time.sleep(1)


def main():
    c = cfg.read_cfg()
    pin = int(c['pin'])
    motion = setup_sensor(pin)
    wait_detection(c, motion)


if __name__ == '__main__':
    main()
