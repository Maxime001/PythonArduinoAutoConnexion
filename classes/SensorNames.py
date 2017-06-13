

class SensorNames:

    sensorName = None

    options = {1: "Test",
               2: "Test2",
               }

    def __init__(self,sensorId):
        self.sensorId = sensorId

    def sensorNamePrint(self):
        return self.options[self.sensorId]

