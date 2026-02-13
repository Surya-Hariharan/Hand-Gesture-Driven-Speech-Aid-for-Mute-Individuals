# Hand Gesture Driven Speech Aid for Mute Individuals

## Overview

This project implements an assistive technology system that enables mute individuals to communicate through hand gestures. The system uses flex sensors attached to a glove to detect finger movements and translates specific gesture patterns into speech output.

## Features

- **Real-time Gesture Recognition**: Uses K-Nearest Neighbors (KNN) machine learning algorithm for gesture classification
- **Text-to-Speech**: Converts recognized gestures into spoken words using Windows Speech API (SAPI)
- **Arduino Integration**: Collects sensor data from flex sensors and accelerometer
- **Multiple Communication Modes**: 
  - Serial communication for direct connection
  - WiFi-based data collection for wireless operation
- **Visual Feedback**: LCD display shows sensor readings and status

## Hardware Requirements

### Electronics
- Arduino Uno/Nano
- 5x Flex sensors (for finger detection)
- 1x Accelerometer (MPU6050 or similar)
- 16x2 I2C LCD display
- Jumper wires and breadboard
- Glove for sensor mounting

### Computer
- Windows PC with Python 3.7+
- USB port for Arduino connection
- (Optional) WiFi capability for wireless mode

## Software Requirements

- Python 3.7 or higher
- Arduino IDE
- Required Python packages (see [requirements.txt](requirements.txt))

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Surya-Hariharan/Hand-Gesture-Driven-Speech-Aid-for-Mute-Individuals.git
cd Hand-Gesture-Driven-Speech-Aid-for-Mute-Individuals
```

### 2. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 3. Upload Arduino Sketch
1. Open [arduino/gesture_sensor.ino](arduino/gesture_sensor.ino) in Arduino IDE
2. Install the `LCD_I2C` library through the Library Manager
3. Connect your Arduino and upload the sketch

### 4. Hardware Setup
1. Connect flex sensors to analog pins A8-A12
2. Connect accelerometer to A0 (X-axis) and A1 (Y-axis)
3. Connect I2C LCD (SDA to A4, SCL to A5)
4. Mount sensors on a glove according to the finger layout

## Usage

### Training the Model (Optional)
If you want to retrain the model with new gesture data:
```bash
cd src
python train_model.py
```

### Running the Main Application
1. Connect the Arduino via USB
2. Update the COM port in the code if needed (default: COM3)
3. Run the main application:
```bash
cd src
python gesture_recognition.py
```

### Gesture Definitions
The system recognizes the following gestures/phrases:
- 0: "hello"
- 1: "how are you"
- 2: "happy morning"
- 3: "good day"
- 4: "i am hungry"
- 5: "good night"
- 6: "i am not feeling well"
- 7: "well done"
- 8: "who are you"
- 9: "come here"
- 10: "happy"

## Project Structure

```
├── src/                          # Source code
│   ├── gesture_recognition.py    # Main application
│   ├── train_model.py           # Model training script
│   ├── wifi_data_collector.py   # WiFi data collection
│   └── test_tts.py              # Text-to-speech testing
├── arduino/                      # Arduino code
│   └── gesture_sensor.ino       # Sensor data collection
├── data/                         # Datasets
│   ├── gesture_dataset.csv      # Training data
│   └── raw_sensor_data.csv      # Raw sensor readings
├── models/                       # Trained models
│   └── gesture_model.sav        # KNN classifier
├── docs/                         # Documentation
├── requirements.txt              # Python dependencies
└── README.md                     # This file
```

## How It Works

1. **Data Collection**: Flex sensors measure finger bend angles, accelerometer measures hand orientation
2. **Signal Processing**: Arduino reads analog values and converts them to digital format
3. **Feature Extraction**: Sensor values are processed and normalized
4. **Classification**: KNN model predicts gesture based on sensor patterns
5. **Speech Output**: Recognized gesture is converted to speech using Windows SAPI

## Customization

### Adding New Gestures
1. Collect training data for new gestures
2. Update the gesture dataset in [data/gesture_dataset.csv](data/gesture_dataset.csv)
3. Add corresponding phrases to the `r` array in `gesture_recognition.py`
4. Retrain the model using `train_model.py`

### Adjusting Sensor Sensitivity
Modify the threshold values in the Arduino code:
```cpp
if(a>390)  // Adjust this value for sensor sensitivity
```

## Troubleshooting

### Common Issues
1. **Serial Connection Error**: Check COM port and ensure Arduino drivers are installed
2. **Low Accuracy**: Recalibrate sensors or collect more training data
3. **Speech Not Working**: Ensure Windows Speech API is enabled
4. **Sensor Issues**: Check wiring and sensor connections

### Performance Tips
- Ensure sensors are securely mounted on the glove
- Calibrate sensors for each user
- Use consistent gesture movements during training and operation

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the open-source community for libraries and resources
- Special appreciation for accessibility technology research
- Arduino and Python communities for excellent documentation

## Contact

Surya Hariharan - [GitHub](https://github.com/Surya-Hariharan)

Project Link: [https://github.com/Surya-Hariharan/Hand-Gesture-Driven-Speech-Aid-for-Mute-Individuals](https://github.com/Surya-Hariharan/Hand-Gesture-Driven-Speech-Aid-for-Mute-Individuals)