

#include <AFMotor.h>
#include <stdio.h>
#include <string.h>
AF_DCMotor motor1(1);
AF_DCMotor motor2(2);
AF_DCMotor motor3(3);
AF_DCMotor motor4(4);
 char input;
 int data ;
 int n;
 void setup() {
  // M2
  motor1.setSpeed(200);
  //M1
  motor2.setSpeed(200);
  //M4
  motor3.setSpeed(200);
  //M3
  motor4.setSpeed(200);
  
  Serial.begin(9600);                               //initialize serial COM at 9600 baudrate
  Serial.flush();
  Serial.println("Hello!,How are you Python ?");
}
 
void loop() {
while (Serial.available())    //whatever the data that is coming in serially and assigning the value to the variable “data”

{ 
  Serial.flush();
  n = Serial.readString().toInt();
  Serial.print("this is input" );
  Serial.print(n);
    data = n;
    Serial.print(data);
    
if (data == 0) 
{
  // Serial.println("Hello!,How are you Python ? FORWARD");
   forward();
   delay(4000);
} 
else if (data ==1)
{
  backward();
}
else if (data == 2)
{
    right();
}
else if (data ==3)
{
  left();
}
else if (data == 4)
{
  Stop();
}
else {
  Serial.println("Hello!,i'm in else ");
   forward();
   delay(4000);

  }
}
       
}

void right(){
 motor1.run(FORWARD);
 motor2.run(FORWARD);
 motor3.run(BACKWARD);
 motor4.run(FORWARD);
motor3.setSpeed(190);
 motor4.setSpeed(210);
  }

  void left(){
 motor1.run(FORWARD);
 motor2.run(FORWARD);
 motor3.run(FORWARD);
 motor4.run(BACKWARD);
motor3.setSpeed(210);
 motor4.setSpeed(190);
  }
   void backward(){
 motor1.run(BACKWARD);
 motor2.run(BACKWARD);
 motor3.run(BACKWARD);
 motor4.run(BACKWARD);
motor3.setSpeed(210);
 motor4.setSpeed(190);
  }
   void forward(){
 motor1.run(FORWARD);
 motor2.run(FORWARD);
 motor3.run(FORWARD);
 motor4.run(FORWARD);
 motor3.setSpeed(210);
 motor4.setSpeed(210);
  }
  void Stop(){
 motor3.setSpeed(0);
 motor4.setSpeed(0);
 motor1.setSpeed(0);
 motor2.setSpeed(0);
  }
