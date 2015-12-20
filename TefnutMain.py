#!/user/bin/python

import sensors 
from datetime import datetime
import sqlite3
import csv

#get sensordata first, then write to the database and csv file

#get datestamp
today = datetime.now()

#get the humidity/temperature sensor data
htSensor = sensors.HumidTempData('P8_11')
celcius, farenheight, humidity = htSensor.HTvalues()

#get moisture sensor data
moistSensor = sensors.analogSensor('P9_33')
moistValue = moistSensor.ASoneValue()


#connect to the sensor data database
conn = sqlite3.connect('sensorData.db')

#write date and sensor data to the sData table in the sensors database
conn.execute("INSERT INTO PlantValues VALUES(sensorID('System01'), dateTimeStamp(today), airHumidity(humidity), airTemp(farenheight), soilMoisture(moistValue))"

#commit changes to the database
conn.commit()
#close the database connection
conn.close()

#open the sensor data csv file
with open('valsInDB.csv', 'ab') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)

    #write date and sensor data to the csv file
    wr.writerow([today, humidity, farenheight, moistValue])
