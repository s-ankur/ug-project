#include <EEPROM.h>
int n,a;
byte x;
void setup()
{

  n=1024;
   a = EEPROM.read(n-1);
   int b= EEPROM.read(n-2);
   a+=b<<8;
  Serial.begin(9600);    
  Serial.println(a);
  
  for (int i=0;i<a;i++)
  {

    byte x=EEPROM.read(i);
    Serial.println(x, DEC);

  }
}

void loop()

{

}
