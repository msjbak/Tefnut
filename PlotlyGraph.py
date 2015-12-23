import plotly.plotly as py
import plotly.tools as tls
from plotly.graph_objs import *
import numpy as np


class graph:

    def __init__ (self, t, m , h):
        self.temp = t
	self.moisture = m
	self.humidity = h

    def streamOut(self):


#write to the plotly graph

stream_ids = tls.get_credentials_file()['stream_ids']





pyPlotly.plot({
    "Temp vs Moisture": [{
        "temperature": [farenheight],
        "moisture": [moistValue]
    }],
    "Layout":{
        "title":"Sensors"
    }
}, filename='tempVmoisture',
   privacy='public')



