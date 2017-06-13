# PythonArduinoAutoConnexion
Automatic connection between a python script and one or more arduinos

> To run the script, open bash console, go to the repository and type > Python root.py


How to use ? 

Arduino code :
- Take an arduino, send the programm placed in the folder arduinoProgram. 
- Just set-up the ID of the arduino line 18 (you can keep the default ID)

Python code : 
- Open classes/SensorNames.py and change if needed the name of your sensor
- Run root.py and enjoy !

> By default, this script just read the json object of the arduino.


How to install Python 2.7 ?
- sudo apt-get update
- sudo apt-get upgrade
- wget --no-check-certificate https://www.python.org/ftp/python/2.7.11/Python-2.7.11.tgz
- tar -xzf Python-2.7.11.tgz
- cd Python-2.7.11
- ./configure 
- make
- sudo make install 
