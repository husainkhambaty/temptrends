#!/usr/bin/env python3
import os
import requests 
import time
import yaml

config_file = "config.yml"
config = []

def read_config():
    with open(config_file, 'r') as ymlfile:
        cfg = yaml.load(ymlfile, Loader=yaml.BaseLoader)
    return cfg

def log(t):
    
    # Create the data string
    data = 'temp,room=' + config['app']['location'] +',region=' + config['app']['region'] + ' value=' + str(t)

    # POST to the Influxdb hosted on the cloud host
    #requests.post(
    #    url="https://" + config['influxdb']['host'] + "/write?db=" + config['influxdb']['db_name'],
    #    data=data,
    #    headers={'Content-Type': 'application/octet-stream'}
    #)
    print(data)

def get_sensor():
    for i in os.listdir(config['device']['path']):
        if i != 'w1_bus_master1':
            sensor = i
    return sensor

def read(sensor):
    # Path to the w1_slave file where the temp data is written
    location = config['device']['path'] + sensor + '/w1_slave'

    # open the file and read it
    tfile = open(location)
    text = tfile.read()

    # close the file
    tfile.close()

    # Get the second line    
    secondline = text.split("\n")[1]

    # Get the last piece of text with the temperature i.e t=#####
    temperaturedata = secondline.split(" ")[9]

    # Get the numbers from the 3rd char onwards
    temperature = float(temperaturedata[2:])

    # Convert to celsius and farenheit
    celsius = temperature / 1000
    farenheit = (celsius * 1.8) + 32

    return celsius, farenheit

def loop(sensor):
    while True:
        if read(sensor) != None:
            temp = read(sensor)
            log(temp[0])
        
        time.sleep(int(config['app']['data_capture_interval']))
            
def kill():
    quit()

if __name__ == '__main__':
    try:
        
        config = read_config()
        sensor = get_sensor()
        loop(sensor)

    except KeyboardInterrupt:
        kill()

