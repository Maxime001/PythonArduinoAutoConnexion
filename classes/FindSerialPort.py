from __future__ import print_function
import json
import serial
import time
from SensorNames import SensorNames
import sys
import os
from termcolor import cprint


class FindSerialPort:
    sensorId = None
    # Array who contains the COM port who bad sensorID is detected
    forbiddenComPort = []
    # Serial string type ( COM || /dev/ttyUSB )
    comStr = None
    # Serial connexion
    ser = None
    # Serial Port (int)
    num = None
    # Serial Port (str) - type > COM5
    serialPort = ""
    # Hide compulsory information
    silentMode = False
    # data from serial
    data = None
    # str name of the sensor
    sensorName = None
    # time to wait for data from the serial port
    setTimeOut = 30;

    def __init__(self, sensorId):
        self.sensorId = sensorId
        SensorNameObject = SensorNames(self.sensorId)
        self.sensorName = SensorNameObject.sensorNamePrint()

    # function who return type of OS and serial string type
    def getOs(self):
        if (os.name == 'nt'):
            self.comStr = "COM"
        else:
            self.comStr = "/dev/ttyUSB"

    # try to connect to all serial port
    def getSerialPort(self):
        self.getOs()
        if (self.silentMode == False):
            print("")
            print("---------------------------------")
            print("--- Serial port COM searching ---")
            print("---------------------------------")
            print("")
        else:
            print("Connexion ...")
        for self.num in range(0, 22):
            self.serialPort = self.comStr + str(self.num)
            try:
                self.ser = serial.Serial(self.serialPort, 9600, timeout=0)

                if (self.forbiddenComPort.count(self.num) == 0):
                    if (self.silentMode == False):
                        print("COM Port : " + self.serialPort + " founded")
                        print("")
                        print("Waiting for data...")
                        print("")
                    self.checkSerialPort()
                return

            except Exception as e:
                if (self.silentMode == False):
                    sys.stdout.write(str(self.num) + ", ")
                if(self.num == 21):
                    self.errorNoSerialFounded()
                time.sleep(0.05)

    # when a connexion is etablished, checking if the ID of the arduino is correct
    def checkSerialPort(self):
        self.getData()
        try:
            self.data = json.loads(self.data)
        except Exception as e:
            self.errorNotAJsonObject()

        if (int(self.data['id']) == self.sensorId):
            if (self.silentMode == False):
                cprint("Arduino " + str(self.data['id']) +" Connected ! (" + self.sensorName + ")", 'white', 'on_green')
            else:
                print("Connected")
        else:
            self.errorBadArduinoId()

    def getData(self):
        self.data = self.ser.readline()
        startTimeLeft = time.time()
        timeOut = None
        while (self.data == ""):
            timeOut = self.setTimeOut - (time.time() - startTimeLeft)
            timeOut = format(float(timeOut), '.2f')

            if(float(timeOut) < 0):
                print("")
                self.errorTimeOut()
                self.data = False
            else:
                print("Timeout for this serial port in : " + str(timeOut) + " Seconds  ", end='\r')
                sys.stdout.flush()
            # starting reading port after 5 seconds
            if(float(time.time() - startTimeLeft) > float(5.0)):
                self.data = self.ser.readline()
            time.sleep(0.05)
        print("")
        if(self.data != False):
            cprint("------- " + self.serialPort + " DATA DETECTED -------", 'cyan', 'on_yellow')
            time.sleep(2)
        timeOut = None

    def errorTimeOut(self):
        if (self.silentMode == False):
            sys.stdout.flush()
            print("Timeout for this COM port")
            print(str(self.serialPort) + " has been added to forbiden port for this arduino")
            print("")
        self.ser.close()
        self.errorAddToForbiddenArray()


    def errorBadArduinoId(self):
        if (self.silentMode == False):
            print("Bad arduino ID, checking others serial port ...(ID of this Arduino : " + str(
                self.data['id']) + " || Excepted ID : " + str(self.sensorId) + ")")
            print(str(self.serialPort) + " has been added to forbiden port for this arduino")
            print("")
        self.ser.close()
        self.errorAddToForbiddenArray()

    def errorNotAJsonObject(self):
        print("Bad arduino : No Json Object detected, checking others serial port ... ")
        print(str(self.serialPort) + " has been added to forbiden port for this arduino")
        self.ser.close()
        self.errorAddToForbiddenArray()

    def errorAddToForbiddenArray(self):
        self.ser.close()
        self.forbiddenComPort.append(self.num)
        self.getSerialPort(self.forbiddenComPort)

    def errorNoSerialFounded(self):
        print("")
        cprint('Info Error, no serial port found for this sensor (sensor ID : ' + str(self.sensorId) + ' - Sensor name : '+ self.sensorName +')', 'white', 'on_red')
