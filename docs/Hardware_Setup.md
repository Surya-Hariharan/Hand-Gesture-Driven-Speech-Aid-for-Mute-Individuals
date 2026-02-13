# Hardware Setup Guide

## Circuit Diagram

### Arduino Connections

#### Flex Sensors (Digital Input with Pull-up)
- Finger 1 (Thumb): Pin A8
- Finger 2 (Index): Pin A9  
- Finger 3 (Middle): Pin A10
- Finger 4 (Ring): Pin A11
- Finger 5 (Pinky): Pin A12

**Note**: Each flex sensor should be connected with a 10kΩ pull-up resistor to 5V.

#### Accelerometer (Analog Input)
- X-axis: Pin A0
- Y-axis: Pin A1
- VCC: 5V
- GND: Ground

#### I2C LCD Display (16x2)
- SDA: Pin A4
- SCL: Pin A5
- VCC: 5V
- GND: Ground
- I2C Address: 0x27 (default)

#### Power
- Arduino powered via USB or external 5V supply
- Ensure all components share common ground

## Flex Sensor Mounting Guide

### Glove Preparation
1. Use a thin, flexible glove (latex, nitrile, or fabric)
2. Ensure glove fits snugly but allows finger movement

### Sensor Placement
- **Thumb**: Mount on back of thumb, aligned with joint
- **Index Finger**: Mount on back of finger, covering both joints
- **Middle Finger**: Mount on back of finger, covering both joints  
- **Ring Finger**: Mount on back of finger, covering both joints
- **Pinky**: Mount on back of finger, covering both joints

### Mounting Methods
1. **Adhesive Tape**: Use thin electrical tape or medical tape
2. **Fabric Adhesive**: For permanent mounting on fabric gloves
3. **Sewing**: For durable installation on fabric gloves

### Wiring Considerations
- Use thin, flexible wires (28-30 AWG recommended)
- Create service loops at finger joints to prevent wire breakage
- Route wires along the back of the hand to avoid interference
- Use a small connector at the wrist for easy glove removal

## Calibration Procedure

### Initial Setup
1. Upload the Arduino sketch
2. Connect the serial monitor (9600 baud)
3. Wear the glove and observe sensor readings

### Threshold Adjustment
1. **Relaxed Position**: Note sensor values with fingers straight
2. **Bent Position**: Note sensor values with fingers fully bent
3. **Calculate Threshold**: Set threshold midway between relaxed and bent values
4. **Update Code**: Modify threshold values in Arduino sketch

Example:
```cpp
// If relaxed = 200 and bent = 600, set threshold = 400
if(flexSensor1 > 400) {
    finger1 = 1;  // Finger is bent
} else {
    finger1 = 0;  // Finger is straight
}
```

### Fine-tuning
- Test each gesture multiple times
- Adjust thresholds if detection is unreliable
- Consider individual finger sensitivity differences

## Troubleshooting Hardware Issues

### Common Problems

#### No Serial Communication
- Check USB cable connection
- Verify COM port in Device Manager (Windows)
- Ensure correct baud rate (9600)

#### Inconsistent Sensor Readings
- Check flex sensor connections
- Verify pull-up resistors are installed
- Ensure sensors are not damaged

#### LCD Not Displaying
- Verify I2C connections (SDA/SCL)
- Check I2C address using I2C scanner sketch
- Ensure proper power supply (5V)

#### Erratic Accelerometer Data
- Check analog pin connections
- Verify power supply stability
- Shield from electromagnetic interference

### Testing Individual Components

#### Flex Sensor Test
```cpp
void loop() {
    int sensorValue = analogRead(A8);
    Serial.println(sensorValue);
    delay(100);
}
```

#### LCD Test
```cpp
#include <LCD_I2C.h>
LCD_I2C lcd(0x27);

void setup() {
    lcd.begin();
    lcd.backlight();
    lcd.print("LCD Test OK");
}
```

#### Accelerometer Test
```cpp
void loop() {
    int x = analogRead(A0);
    int y = analogRead(A1);
    Serial.print("X: ");
    Serial.print(x);
    Serial.print(" Y: ");
    Serial.println(y);
    delay(100);
}
```

## Performance Optimization

### Hardware Tips
- Use shielded cables for long wire runs
- Add capacitors across power lines for noise reduction
- Ensure solid connections (solder preferred over breadboard)
- Keep sensors away from high-current switching circuits

### Enclosure Recommendations
- Use a small project box for Arduino and circuits
- Ensure adequate ventilation
- Provide strain relief for cables
- Consider waterproofing for outdoor use

## Safety Considerations

- Use low-voltage circuits only (5V max)
- Ensure no sharp edges on mounted sensors
- Test thermal comfort during extended use
- Include emergency disconnect method
- Follow local electrical safety standards