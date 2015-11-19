import sensors

htSensor = sensors.HumidTempData('P8_11')
celcius, farenheight, humidity = htSensor.HTvalues()

print '%.4f'%(humidity)
print '%.2f*C %.2f*F'%(celcius, farenheight)
