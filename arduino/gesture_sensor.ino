#include <LCD_I2C.h>

LCD_I2C lcd(0x27);

void setup() {
  Serial.begin(9600);
  lcd.begin(); // If you are using more I2C devices using the Wire library use lcd.begin(false)
               // this stop the library(LCD_I2C) from calling Wire.begin()
  lcd.backlight();
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("HAND GESTURE");
  lcd.setCursor(0, 1);
  lcd.print("MONITORING");
  delay(3000);
  lcd.clear();
  
  pinMode(A0, INPUT);
  pinMode(A1, INPUT);
  pinMode(A8, INPUT_PULLUP);
  pinMode(A9, INPUT_PULLUP);
  pinMode(A10, INPUT_PULLUP);
  pinMode(A11, INPUT_PULLUP);
  pinMode(A12, INPUT_PULLUP);
}

void loop() {
  int x = analogRead(A0);
  int y = analogRead(A1);
  int a = analogRead(A8);
  int b = analogRead(A9);
  int c = analogRead(A10);
  int d = analogRead(A11);
  int e = analogRead(A12);
  
  String s = "X:" + String(x) + " Y:" + String(y);
  String t = "F1:" + String(a) + " F2:" + String(b);
  String u = "F3:" + String(c) + " F4:" + String(d);
  String v = "F5:" + String(e);
  
  lcd.setCursor(0, 0);
  lcd.print(s);
  lcd.setCursor(0, 1);
  lcd.print(t);
  delay(1000);
  lcd.clear();
  
  lcd.setCursor(0, 0);
  lcd.print(u);
  lcd.setCursor(0, 1);
  lcd.print(v);
  delay(1000);
  lcd.clear();
  
  if (a > 390) {
    a = 1;
  } else {
    a = 0;
  }
  
  if (b > 460) {
    b = 1;
  } else {
    b = 0;
  }
  
  if (c > 455) {
    c = 1;
  } else {
    c = 0;
  }
  
  if (d > 455) {
    d = 1;
  } else {
    d = 0;
  }
  
  if (e > 460) {
    e = 1;
  } else {
    e = 0;
  }
  
  Serial.print(a);
  Serial.print(",");
  Serial.print(b);
  Serial.print(",");
  Serial.print(c);
  Serial.print(",");
  Serial.print(d);
  Serial.print(",");
  Serial.print(e);
  Serial.println();
  delay(1000);
}
