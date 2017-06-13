#include <ArduinoJson.h>

// Json library initialization
StaticJsonBuffer<200> jsonBuffer;
JsonObject& root = jsonBuffer.createObject();

// variables initialization 
int timer = 3000;
int idArduino = 2;

void setup() {
  Serial.begin(9600);
}

void loop() {
  printResult();
  delay(timer); 
}

/**
 * Get the data of the DTY sensor
 */


/**
 * Print the data
 */
void printResult(){
  root["id"] = idArduino;
  root["success"] = 1;
  root.printTo(Serial);
  delay(timer);
}
