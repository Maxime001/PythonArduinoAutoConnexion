import json
import time
import datetime
from datetime import datetime

class DataManagment:

    serialPortObject = None
    ser = None
    data = None
    date = None

    def __init__(self,serialPortObject):
        self.serialPortObject = serialPortObject
        self.ser = self.serialPortObject.ser

    # Description of the device connected
    def description(self):
        print("-----------------------------")
        print("Description of this sensor : ")
        print("ID : " + str(self.serialPortObject.sensorId))
        print("Name : " + str(self.serialPortObject.sensorName))
        print("Serial connexion : " + str(self.serialPortObject.serialPort))
        print("-----------------------------")

    # Read the data of the serial and print it
    def readData(self):
        while(True):
            self.data = self.ser.readline()
            if(self.data != ""):
                self.date = datetime.now()
                print("----------------------------------")
                print("Date : " + str(self.date))
                self.data = json.loads(self.data)
                # rounding
                print (json.dumps(self.data, indent=4))
            time.sleep(0.5)

