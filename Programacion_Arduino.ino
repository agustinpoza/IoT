unsigned long time;
unsigned long t = 0;
int TPT = 1000;
int LED = 7;
const int Sensor = A0;
//-------------------------------------------------------------------------------------------------------------------------------------------------------------
void setup() {
  Serial.begin(9600);
  pinMode(LED, OUTPUT);
}
//-------------------------------------------------------------------------------------------------------------------------------------------------------------
void loop() {
  if (Serial.available() > 0) {
    char VR = Serial.read();
    switch(VR) {
      case 'A': digitalWrite(LED, HIGH);
      break;
      case 'a': digitalWrite(LED, LOW);
      break;
    }
  }
  time = millis();
  if (time - t > TPT){
    t = time;
    LeerLM35();
  }
}
//-------------------------------------------------------------------------------------------------------------------------------------------------------------
void LeerLM35() {
  int value = analogRead(Sensor);
  float millivolts = (value / 1023.0) * 5000;
  float celsius = millivolts / 10; 
  Serial.println(celsius);
}
