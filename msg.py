#!/usr/bin/python3

from umqtt.simple import MQTTClient
import cfg


def xmt(server="localhost", topic="MQTT", note="empty message"):
    c = MQTTClient("umqtt_client", server)
    c.connect()
    c.publish(bytes(topic, 'UTF-8'), bytes(note, 'UTF-8'))
    c.disconnect()


def sub_cb(topic, msg):
    print((topic, msg))


def send(data):
    config = cfg.read_cfg('config.json')
    subject = str(config['ptopic'])
    server = str(config['server'])
    note = str(data)

    xmt(server=server, topic=subject, note=note)


def rcv(server="localhost", topic="MQTT"):

    c = MQTTClient("umqtt_client", server)
    c.set_callback(sub_cb)
    c.connect()
    c.subscribe(bytes(topic, 'UTF-8'))
    while True:
        if True:
            # Blocking wait for message
            c.wait_msg()
        else:
            # Non-blocking wait for message
            # c.check_msg()
            # Need to sleep to avoid 100% CPU usage (in a real
            # app other useful actions would be performed instead)
            # time.sleep(1)
            pass
    c.disconnect()


def main():

    xmt()
    rcv()
    send('Device Ready')

if __name__ == "__main__":
    main()
