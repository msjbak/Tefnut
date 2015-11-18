import Adafruit_DHT

class HumidTempData(object):

    def __init__(self, htPin):
        self.sensorPin = htPin

    def HTvalues(self):
        humid, temp = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, self.sensorPin)

        if temp is not None:
            temperatureC = temp
            temperatureF = ((float(temp)*9)/5)+32
        else:
            temperatureC = 'not found'
            temperatureF = 'not found'

        if humid is not None:

class HumidTempData(object):

    def __init__(self, htPin):
        self.sensorPin = htPin

    def HTvalues(self):
        humid, temp = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, self.sensorPin)

 if temp is not None:
            temperatureC = temp
            temperatureF = ((float(temp)*9)/5)+32
        else:
            temperatureC = 'not found'
            temperatureF = 'not found'


        if humid is not None:
            humidity = humid
	else:
            humidity = 'not found'


        return temperatureC, temperatureF, humidity
