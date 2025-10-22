#include <Wire.h>

volatile char buf[80];
volatile unsigned count = 0;
volatile bool received = false;

void setup() {
   Serial.begin(115200);
   delay(5000);
   Serial.println("Started");

   Wire.begin(11);
   Wire.onReceive(receiveEvent);
}

void loop() {
   if( received ) {
      for( unsigned i=0; i<count; ++i ) {
         Serial.print(buf[i]);
      }
      received = false;
      count = 0;
   }
   delay(50);
}

void receiveEvent(int howMany) {
   for( int i=0; i<howMany; ++i ) {
      char c = Wire.read();
      if( count < sizeof buf ) {
         buf[count++] = c;
      }
   }
   received = true;
}