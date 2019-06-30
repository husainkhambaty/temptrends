# TempTrends
Capturing the temperature using a DS18B20 temperature sensor and Raspberry PI. This project started out with the need to capture the temperature around the house to look for cold and warm spots. I built this with help from CircuitBasics and extended on it. 

### How does it work?
I used a simple Raspberry PI 3 kit and a DS18B20 water-proof temperature sensor. I've written two python scripts to read the data off the temperature sensor and perform a task. 
I've also used a Time-series DB and a Data visualisation tool to capture the data and visualise it to help make some sense.

### Lets dig deeper
##### sense-standalone.py
This python script helps to capture the temperature and display it on the screen. This simply 