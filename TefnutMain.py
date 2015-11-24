#!/user/bin/python

import sensors 
from datetime import datetime
import csv

#open the sensor data csv file
with open('sensors.csv', 'ab') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)

    #get the current date and time
    today = datetime.now()

    #get the humidity/temperature sensor data
    htSensor = sensors.HumidTempData('P8_11')
    celcius, farenheight, humidity = htSensor.HTvalues()

    #get moisture sensor data
    moistSensor = sensors.analogSensor('P9_33')
    moistValue = moistSensor.ASoneValue()


    #write date and sensor data to the csv file
    wr.writerow([today, celcius, farenheight, humidity, moistValue])

#print '%.4f'%(humidity)
#print '%.2f*C %.2f*F'%(celcius, farenheight)
