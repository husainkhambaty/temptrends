#!/usr/bin/env python3
import os
import yaml
from datetime import datetime



config_file = "config.yml"
config = []

def read_config():
    with open(config_file, 'r') as ymlfile:
        cfg = yaml.load(ymlfile, Loader=yaml.BaseLoader)
    return cfg

def log(message):
    print(datetime.now().strftime("[%Y-%m-%d %H:%M:%S]") + " " + message)

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
            log("Celsius : %0.3fC, Farenheit : %0.3fF" % (temp[0], temp[1]))

def kill():
    quit()

if __name__ == '__main__':
    try:

        # Read the configuration
        config = read_config()

        # Get the sensor id
        sensor = get_sensor()

        # Loop the sensor for data
        loop(sensor)

    except KeyboardInterrupt:
        # Kill on ctrl + C
        kill()
