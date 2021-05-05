void setup() {
  // put your setup code here, to run once:
pinMode(12,OUTPUT);
pinMode(13,OUTPUT);
pinMode(10,OUTPUT);
pinMode(11,OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
digitalWrite(12,HIGH);
digitalWrite(13,LOW);
analogWrite(10,150);
analogWrite(11,150);

delay(2000);

digitalWrite(12,LOW);
digitalWrite(13,HIGH);

delay(2000);

digitalWrite(12,HIGH);
digitalWrite(13,HIGH);

delay(5000);

analogWrite(10,0);
analogWrite(11,0);

delay(5000);
delay(5000);



}
