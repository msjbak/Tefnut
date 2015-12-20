#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('sensorData.db')
print "Opened database successfully"

conn.execute('''CREATE TABLE PlantValues
	(sensorID VARCHAR(30) NOT NULL,
       	dateTimeStamp TIMESTAMP NOT NULL,
       	recordLength INT,
       	onTime INT,
       	airHumidity FLOAT,
       	airTemp FLOAT,
       	soilTemp FLOAT,
	soilMoisture FLOAT,
	light FLOAT,
       	state VARCHAR(30));''')
print "Table created successfully"

conn.close()
