#include <Servo.h>

Servo myservo;
const int pingPin = 7; // Trigger Pin of Ultrasonic Sensor
const int echoPin = 6; // Echo Pin of Ultrasonic Sensor
//unsigned long millis_prev=0;
//unsigned long millis_current=0;
//int pos = 0;
//int rotation = 0;

void setup()
{
  Serial.begin(9600);
  //myservo.attach(9);
  while(!Serial){
    
  }
}

void loop()
{
  
  
  long duration, inches, cm;
  int buffer[16];
  pinMode(pingPin, OUTPUT);
  digitalWrite(pingPin, LOW);
  delayMicroseconds(2);
  digitalWrite(pingPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(pingPin, LOW);
  pinMode(echoPin, INPUT);
  duration = pulseIn(echoPin, HIGH);
  inches = microsecondsToInches(duration);
  cm = microsecondsToCentimeters(duration);
  //Serial.print(inches);
  //Serial.print("in, ");
//  if (Serial.available())
//  {
//    int size = Serial.readBytesUntil('\n', buffer, 12);
//  }
  
    Serial.print(cm);
    Serial.println();
   
  
  

//  millis_current=millis();
//  if (millis_current - millis_prev >= 1 && rotation == 0) { // goes from 0 degrees to 180 degrees
//  // in steps of 1 degree
//    myservo.write(pos);
//    Serial.print(pos);
//    Serial.print("\n");
//    pos+=5;
//    millis_prev=millis();
//    if (pos >= 180){
//      rotation = 1;
//    }
//    //delay(15);                       // waits 15ms for the servo to reach the position
//  }
//  else if (millis_current - millis_prev >= 15 && rotation == 1) { // goes from 0 degrees to 180 degrees
//  // in steps of 1 degree
//    myservo.write(pos);
//    Serial.print(pos);
//    Serial.print("\n");
//    pos-=5;
//    millis_prev=millis();
//    if (pos <= 0){
//      rotation = 0;
//    }
//    //delay(15);                       // waits 15ms for the servo to reach the position
//  }
delay(500);
}

long microsecondsToInches(long microseconds) {
   return microseconds / 74 / 2;
}

long microsecondsToCentimeters(long microseconds) {
   return microseconds / 29 / 2;
}
