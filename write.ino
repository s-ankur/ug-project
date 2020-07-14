#include <EEPROM.h>
int n;
int led = 13;


void setup()
{
  n=1024;
  Serial.begin(9600);
   pinMode(led, OUTPUT);     
  digitalWrite(led, LOW);    // turn the LED off by making the voltage LOW

 // while(!Serial.available());
    digitalWrite(led, HIGH);   // turn the LED on (HIGH is the voltage level)

}

int i =0;
void loop()
{
  if (i>n-4 or (Serial.available() and Serial.read()=='s'))
  {
      digitalWrite(led, LOW);
      while(true);
  }
  else if(i<n-2)
  {
    for(int j=0;j<100;j++)
    {
    delay(3000);
    }
    int val = analogRead(0) / 4;
    Serial.println(val);
    EEPROM.write(i, val);
    i++;
    EEPROM.write(n-1,i&255);
    EEPROM.write(n-2,i>>8);
  }
}
