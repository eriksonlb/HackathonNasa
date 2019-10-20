int flame_sensor_pin = 2 ;// initializing pin 2 as the sensor output pin
int flame_pin = HIGH ; // state of sensor

void setup() {
  
pinMode ( flame_sensor_pin , INPUT ); // declaring sensor pin as input pin for Arduino
Serial.begin ( 9600 );// setting baud rate at 9600

}

void loop() {
  
flame_pin = digitalRead ( flame_sensor_pin ) ; //reading from the sensor

if (flame_pin == LOW ) // applying condition
{
  Serial.println ("OK");
}

else
{
  Serial.println ("FIRE");
}

delay(1000);
}
