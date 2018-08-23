# -*- coding: cp1252 -*-
import sys
import json
import time
import random

import paho.mqtt.client as mqtt




def generate(host, port, username, password, topic, interval_ms, verbose):
    #generate data and send it to an MQTT broker"""
    mqttc = mqtt.Client()

    if username:
        mqttc.username_pw_set(username, password)

    mqttc.connect(host, port)

    interval_secs = interval_ms / 1000.0

    while True:
        sensor_id = random.randint(90, 100)
        
        min_val = random.randint(0, 100)
        max_val = random.randint(0, 100)
        val = random.randint(0,190)

        data = {
            "id": sensor_id,
            "value": val
        }

        payload = json.dumps(data)
        print payload

        if verbose:
            print("%s: %s" % (topic, payload))

        mqttc.publish(topic, payload)
        time.sleep(interval_secs)


def main():
    #main entry point, load and validate config and call generate"""
    try:
        
           # mqtt_config = config.get("mqtt", {})
           # misc_config = config.get("misc", {})
            

            interval_ms =  500
            verbose =  False



            host =  "139.59.20.218"
            port =  1883
            username = "mqtt_Admin"
            password = "WAnD_WAnD"
            topic =  "sensors"
            
            generate(host, port, username, password, topic, interval_ms, verbose)
    except IOError as error:
        print("Error opening config file ‘%s’" % config_path, error)

main()
