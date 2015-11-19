import Adafruit_DHT
import Adafruit_BBIO.ADC as ADC


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

class analogSensor(object):

    ADC.setup()

    def __init__(self, aPin):
        self.aSensorPin = aPin

    def ASoneValue(self):
        aSensorValue = ADC.read(self.aSensorPin)

        return aSensorValue
