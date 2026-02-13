"""Hand Gesture Recognition System

Main application for real-time gesture recognition using flex sensors
connected to Arduino. Converts recognized gestures to speech output.
"""

import serial
import time
import pickle
import win32com.client
from sklearn.preprocessing import StandardScaler

# Gesture phrases corresponding to prediction classes
GESTURE_PHRASES = [
    "hello",
    "how are you",
    "happy morning",
    "good day",
    "i am hungry",
    "good night",
    "i am not feeling well",
    "well done",
    "who are you",
    "come here",
    "happy"
]

# Configuration
MODEL_PATH = '../models/gesture_model.sav'
SERIAL_PORT = 'COM3'
BAUD_RATE = 9600


def main():
    """Main function to run gesture recognition system"""
    # Load the trained model
    print("Loading gesture recognition model...")
    with open(MODEL_PATH, 'rb') as model_file:
        loaded_model = pickle.load(model_file)
    
    # Initialize serial communication
    print(f"Connecting to Arduino on {SERIAL_PORT}...")
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE)
    print("Serial port opened successfully.")
    
    # Initialize text-to-speech
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    
    # Wait for Arduino to initialize
    time.sleep(2)
    
    try:
        print("Starting gesture recognition... Press Ctrl+C to stop.")
        while True:
            # Read data from Arduino
            data = ser.readline().decode().strip()
            print("Received data:", data)
            
            # Parse sensor values
            values = data.split(',')
            if len(values) == 5:
                v1, v2, v3, v4, v5 = values
                
                # Prepare features for prediction
                features = [[
                    float(v1), float(v2), float(v3), float(v4), float(v5)
                ]]
                
                # Predict gesture
                predicted = loaded_model.predict(features)
                gesture_index = int(predicted[0])
                
                if 0 <= gesture_index < len(GESTURE_PHRASES):
                    phrase = GESTURE_PHRASES[gesture_index]
                    print(f"Predicted gesture: {gesture_index} - '{phrase}'")
                    
                    # Convert to speech
                    speaker.Speak(phrase)
                else:
                    print(f"Unknown gesture index: {gesture_index}")
    
    except KeyboardInterrupt:
        print("\nShutting down...")
    finally:
        ser.close()
        print("Serial port closed.")


if __name__ == "__main__":
    main()

