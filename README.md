# PythonArduinoAutoConnexion
Automatic connection between a python script and one or more arduinos

> To run the script, open bash console, go to the repository and type > Python root.py


How to use ? 

Arduino code :
- Download and install the package ArduinoJson (https://github.com/bblanchon/ArduinoJson)
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

How to install all differents libraries ?
You need this package : 
- sudo apt-get install python-pip python-dev build-essential 

> pi serial

- wget https://pypi.python.org/packages/8d/88/cf848688ae011085a6da5a470740dafa3a4b105f84a5f79c3b720c19279c/pyserial-3.3.tar.gz#md5=6afe4c2e47bcec6eb7051b8c1ce19d52
- tar wvf pyserial-3.3.tar.gz
- cd pyserial
- sudo python setup.py install

> termcolor
- wget https://pypi.python.org/packages/8a/48/a76be51647d0eb9f10e2a4511bf3ffb8cc1e6b14e9e4fab46173aa79f981/termcolor-1.1.0.tar.gz
- cd termcolor-1.1.0
- sudo python setup.py install

Enjoy ;) 

