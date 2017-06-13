from classes.DataManagment import DataManagment
from classes.FindSerialPort import FindSerialPort


# Serial Port searching
serialPortTest = FindSerialPort(1)
serialPortTest.getSerialPort()

# Start of measures
sensorTest = DataManagment(serialPortTest)
sensorTest.readData()