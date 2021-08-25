#include <Servo.h>
const int pingPin = 34; // Trigger Pin of right Ultrasonic Sensor
const int echoPin = 6; // Echo Pin of right Ultrasonic Sensor
const int pingPin2 = 36; // Trigger Pin of left Ultrasonic Sensor
const int echoPin2 = 7; // Echo Pin of left Ultrasonic Sensor
const int pingPin3 = 38; // Trigger Pin of right Ultrasonic Sensor
const int echoPin3 = 8; // Echo Pin of right Ultrasonic Sensor
const int pingPin4 = 40; // Trigger Pin of left Ultrasonic Sensor
const int echoPin4 = 9; // Echo Pin of left Ultrasonic Sensor
const int pingPin5 = 46; // Trigger Pin of right Ultrasonic Sensor
const int echoPin5 = 12; // Echo Pin of right Ultrasonic Sensor
const int pingPin6 = 44; // Trigger Pin of left Ultrasonic Sensor
const int echoPin6 = 11; // Echo Pin of left Ultrasonic Sensor
const int l1 = 2; // Trigger Pin of left Ultrasonic Sensor
const int l2 = 4; // Echo Pin of left Ultrasonic Sensor
const int r1 = 3; // Trigger Pin of left Ultrasonic Sensor
const int r2 = 5; // Echo Pin of left Ultrasonic Sensor
const int d1 = 22; // Trigger Pin of left Ultrasonic Sensor
const int d2 = 24; // Echo Pin of left Ultrasonic Sensor
const int d3 = 26; // Trigger Pin of left Ultrasonic Sensor
const int d4 = 28; // Echo Pin of left Ultrasonic Sensor
Servo myservo;  // create servo object to control a servo
// twelve servo objects can be created on most boards

int pos = 0;    // variable to store the servo position
int stopBot =0;
int started =0;
int movement=0;

void setup() {
  myservo.attach(13);
  //Motor Driver
  pinMode(2,OUTPUT);
  pinMode(3,OUTPUT);
  pinMode(4,OUTPUT);
  pinMode(5,OUTPUT);
  pinMode(22,OUTPUT);
  pinMode(24,OUTPUT);
  pinMode(26,OUTPUT);
  pinMode(28,OUTPUT);
  //Ultrasonic Sensor
  pinMode(6,INPUT);
  pinMode(7,INPUT);
  pinMode(8,INPUT);
  pinMode(9,INPUT);
  pinMode(10,INPUT);
  pinMode(11,INPUT);
  pinMode(12,INPUT);
 
  pinMode(34,OUTPUT);
  pinMode(36,OUTPUT);
  pinMode(38,OUTPUT);
  pinMode(40,OUTPUT);
  pinMode(42,OUTPUT);
  pinMode(44,OUTPUT);
  pinMode(46,OUTPUT);
  
  //Turning Servo
  //pinMode(12,OUTPUT);
  //LED
  pinMode(33,OUTPUT);
  Serial.begin(9600);

  bigdelay();
}

void loop() {
  long duration,duration2,duration3,duration4,duration5,duration6;
  int cm,cm2,cm3,cm4,cm5,cm6;
  
  char data;
  pos=55;
//  for (pos = 0; pos <= 40; pos += 1) { 
//    // in steps of 1 degree
//    myservo.write(pos);
//    delay(15);
//  }

   //pinMode(pingPin, OUTPUT);
   digitalWrite(pingPin, LOW);
   delayMicroseconds(2);
   digitalWrite(pingPin, HIGH);
   delayMicroseconds(10);
   digitalWrite(pingPin, LOW);
   //pinMode(echoPin, INPUT);
   duration = pulseIn(echoPin, HIGH);
   cm = microsecondsToCentimeters(duration);
   //Serial.print(cm);
   //Serial.print(" cm front");
   //Serial.println();

   //pinMode(pingPin4, OUTPUT);
   digitalWrite(pingPin4, LOW);
   delayMicroseconds(2);
   digitalWrite(pingPin4, HIGH);
   delayMicroseconds(10);
   digitalWrite(pingPin4, LOW);
   //pinMode(echoPin4, INPUT);
   duration4 = pulseIn(echoPin4, HIGH);
   cm4 = microsecondsToCentimeters(duration4);
//   Serial.print(cm4);
//   Serial.print(" cm left");
//   Serial.println();

   
     //pinMode(pingPin2, OUTPUT);
     digitalWrite(pingPin2, LOW);
     delayMicroseconds(2);
     digitalWrite(pingPin2, HIGH);
     delayMicroseconds(10);
     digitalWrite(pingPin2, LOW);
     //pinMode(echoPin2, INPUT);
     duration2 = pulseIn(echoPin2, HIGH);
     cm2 = microsecondsToCentimeters(duration2);
//     Serial.print(cm2);
//     Serial.print(" cm right");
//     Serial.println();


     digitalWrite(pingPin6, LOW);
     delayMicroseconds(2);
     digitalWrite(pingPin6, HIGH);
     delayMicroseconds(10);
     digitalWrite(pingPin6, LOW);
     //pinMode(echoPin6, INPUT);
     duration6 = pulseIn(echoPin6, HIGH);
     cm6 = microsecondsToCentimeters(duration6);
//     Serial.print(cm6);
//     Serial.print(" cm left");
//     Serial.println();

   

     //pinMode(pingPin3, OUTPUT);
     digitalWrite(pingPin3, LOW);
     delayMicroseconds(2);
     digitalWrite(pingPin3, HIGH);
     delayMicroseconds(10);
     digitalWrite(pingPin3, LOW);
     //pinMode(echoPin3, INPUT);
     duration3 = pulseIn(echoPin3, HIGH);
     cm3 = microsecondsToCentimeters(duration3);
//     Serial.print(cm3);
//     Serial.print(" cm back");
//     Serial.println();
  
     
  
     digitalWrite(pingPin5, LOW);
     delayMicroseconds(2);
     digitalWrite(pingPin5, HIGH);
     delayMicroseconds(10);
     digitalWrite(pingPin5, LOW);
     //pinMode(echoPin5, INPUT);
     duration5 = pulseIn(echoPin5, HIGH);
     cm5 = microsecondsToCentimeters(duration5);
//     Serial.print(cm5);
//     Serial.print(" cm left");
//     Serial.print(" done");
//     Serial.println();
     

  
  if (started==0 && cm<40){

    myservo.write(55);

    
      backward();
      startmotor();
      if(cm3>cm5){
        fronttoright();
        delay(15);
        righttofront();
      }
      else if(cm5>cm3){
        fronttoleft();
        delay(15);
        lefttofront();
      }
      else{
        backward();  
      }
   
  }

    if(cm>40 && started==0){
      started=1;
      stopmotor();
    }
  

  if(movement==0 && started==1){

      myservo.write(55);
      if (cm<40 && (cm2-cm6)>30){
        stopmotor();
        fronttoleft();
        backward();
        delay(1000);
        stopmotor();
        lefttofront();
      }
      else if (cm<40 && (cm6-cm2)>30){
        stopmotor();
        fronttoright();
        backward();
        delay(1000);
        stopmotor();
        righttofront();
      }
      else if (cm2<20){
        backward();
        delay(1000);
        stopmotor();
        fronttoleft();
        forward();
        delay(1000);
        lefttofront();
      }
      else if (cm6<20){
        backward();
        delay(1000);
        stopmotor();
        fronttoright();
        forward();
        delay(1000);
        righttofront();
      }
      else if(cm<40){
        stopmotor();
        stopBot=1;
      }
      else if(cm2>cm6){
        forward();
        startmotor();
        fronttoright();
        delay(15);
        righttofront();
      }
      else if(cm6>cm2){
        forward();
        startmotor();
        fronttoleft();
        delay(15);
        lefttofront();
      }
      else{
        forward();
      }
    
   

    
    
    if(stopBot==1){
      Serial.print(stopBot);
      Serial.println();  
      Serial.print(stopBot);
      Serial.println();
      stopBot=0;
      movement=1;
      bigdelay();
      delay(10000);
      delay(10000);
      //bigdelay();
    }
    
    else{
      stopBot=0;
      Serial.print(stopBot);
      Serial.println();  
      Serial.print(stopBot);
      Serial.println();      
    }
     
    
   serialFlush();
  
   
    
  }
  else if(movement==1 && started==1){
     myservo.write(55);

      if (cm4<40 && (cm3-cm5)>30){
        stopmotor();
        fronttoleft();
        forward();
        delay(1000);
        stopmotor();
        lefttofront();
      }
      else if (cm4<40 && (cm5-cm3)>30){
        stopmotor();
        fronttoright();
        forward();
        delay(1000);
        stopmotor();
        righttofront();
      }
      else if (cm3<20){
        forward();
        delay(1000);
        stopmotor();
        fronttoleft();
        backward();
        delay(1000);
        lefttofront();
      }
      else if (cm5<20){
        forward();
        delay(1000);
        stopmotor();
        fronttoright();
        backward();
        delay(1000);
        righttofront();
      }
      
      else if(cm4<40){
        stopmotor();
        stopBot=2;
      }
      else if(cm3>cm5){
        backward();
        startmotor();
        fronttoright();
        delay(15);
        righttofront();
      }
      else if(cm5>cm3){
        backward();
        startmotor();
        fronttoleft();
        delay(15);
        lefttofront();
      }
      else{
        backward();  
      }
 

    if(stopBot==2){
      Serial.print(stopBot);
      Serial.println();
      Serial.print(stopBot);
      Serial.println();
      movement=0;
      stopBot=0;
      bigdelay();
      delay(5000); 
    }
    
    else{
      stopBot=0;
      Serial.print(stopBot);
      Serial.println();  
      Serial.print(stopBot);
      Serial.println();      
    }

   serialFlush();
  }

}

void bigdelay(){
  delay(10000);
  delay(10000);
  delay(10000);
}

void serialFlush(){
  while(Serial.available() > 0) {
    char t = Serial.read();
  }
}

long microsecondsToCentimeters(long microseconds) {
   return microseconds * 0.034 / 2;
}

void fronttoleft(){
   for (pos = 55; pos <= 75; pos += 1) { 
    myservo.write(pos);
    delay(15);
  }
  analogWrite(l1,50);
  analogWrite(l2,50);
  analogWrite(r1,100);
  analogWrite(r2,100);
  
}

void fronttoright(){
  for (pos = 55; pos >= 30; pos -= 1) { 
    myservo.write(pos);
    delay(15);
  }
  analogWrite(l1,100);
  analogWrite(l2,100);
  analogWrite(r1,50);
  analogWrite(r2,50);
}

void lefttofront(){
  for (pos = 75; pos >= 50; pos -= 1) { 
    myservo.write(pos);
    delay(15);
  }
  analogWrite(l1,100);
  analogWrite(l2,100);
  analogWrite(r1,100);
  analogWrite(r2,100);
}

void righttofront(){
  for (pos = 30; pos <= 55; pos += 1) { 
    myservo.write(pos);
    delay(15);
  }
  analogWrite(l1,100);
  analogWrite(l2,100);
  analogWrite(r1,100);
  analogWrite(r2,100);
}

void forward(){
  digitalWrite(d1,HIGH);
  digitalWrite(d2,LOW);
  digitalWrite(d3,HIGH);
  digitalWrite(d4,LOW);
}

void backward(){
  digitalWrite(d1,LOW);
  digitalWrite(d2,HIGH);
  digitalWrite(d3,LOW);
  digitalWrite(d4,HIGH);
}

void stopmotor(){
  analogWrite(l1,0);
  analogWrite(l2,0);
  analogWrite(r1,0);
  analogWrite(r2,0);
}

void startmotor(){
  analogWrite(l1,100);
  analogWrite(l2,100);
  analogWrite(r1,100);
  analogWrite(r2,100);
}
