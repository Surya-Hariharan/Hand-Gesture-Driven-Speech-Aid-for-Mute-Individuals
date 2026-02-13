"""WiFi Data Collector for Gesture Recognition

Collects gesture data over WiFi from ESP8266/Arduino and sends predictions
to ThingSpeak for cloud monitoring and logging.
"""

import os
import pickle
import urllib.request
import http.client
import pandas as pd
from time import sleep
from datetime import datetime

# Configuration
MODEL_PATH = '../models/gesture_model.sav'
WIFI_BASE_URL = "http://192.168.137.233/"
THINGSPEAK_API_KEY = "QIXHGRZ00NB0BGZU"
DATA_FILE_PATH = "../data/wifi_collected_data.csv"
SLEEP_INTERVAL = 1  # seconds


def load_model():
    """Load the trained gesture recognition model"""
    print("Loading gesture recognition model...")
    with open(MODEL_PATH, 'rb') as model_file:
        return pickle.load(model_file)


def transfer_data(my_url):
    """Send and receive data over WiFi
    
    Args:
        my_url (str): URL endpoint to request
        
    Returns:
        str: Response data or error message
    """
    try:
        response = urllib.request.urlopen(WIFI_BASE_URL + my_url)
        data = response.read().decode("utf-8")
        return data
    except http.client.HTTPException as e:
        print(f"HTTP Error: {e}")
        return str(e)
    except Exception as e:
        print(f"Connection Error: {e}")
        return str(e)


def save_to_csv(v1, v2, v3, prediction, data_list):
    """Save collected data to CSV file
    
    Args:
        v1, v2, v3: Sensor values
        prediction: Model prediction
        data_list: List to store data entries
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data_list.append([timestamp, v1, v2, v3, prediction])
    
    # Save to CSV every 10 entries to avoid excessive file I/O
    if len(data_list) % 10 == 0:
        df = pd.DataFrame(
            data_list, 
            columns=['Timestamp', 'V1', 'V2', 'V3', 'Prediction']
        )
        df.to_csv(DATA_FILE_PATH, index=False)
        print(f"Data saved to {DATA_FILE_PATH}")


def send_to_thingspeak(v1, v2, v3, prediction):
    """Send data to ThingSpeak cloud platform
    
    Args:
        v1, v2, v3: Sensor values
        prediction: Model prediction
    """
    try:
        url = (
            f"https://api.thingspeak.com/update?"
            f"api_key={THINGSPEAK_API_KEY}&"
            f"field1={v1}&field2={v2}&field3={v3}&field4={prediction}"
        )
        
        conn = urllib.request.urlopen(url)
        response = conn.read()
        status_code = conn.getcode()
        
        print(f"ThingSpeak status code: {status_code}")
        return status_code == 200
        
    except Exception as e:
        print(f"ThingSpeak upload error: {e}")
        return False


def main():
    """Main function for WiFi data collection and processing"""
    print("=== WiFi Gesture Data Collector ===")
    
    # Load the trained model
    loaded_model = load_model()
    
    # Initialize data collection
    data_list = []
    counter = 0
    
    print(f"Starting data collection from {WIFI_BASE_URL}")
    print("Press Ctrl+C to stop...")
    
    try:
        while True:
            # Request data from WiFi device
            response = transfer_data(str(counter))
            print(f"Raw response: {response}")
            
            # Parse the received data
            values = response.split('-')
            
            if len(values) == 3:
                try:
                    v1, v2, v3 = [float(val.strip()) for val in values]
                    
                    # Prepare data for prediction
                    features = [[v1, v2, v3]]
                    
                    # Make prediction
                    prediction = loaded_model.predict(features)[0]
                    
                    print(f"Sensor values: V1={v1}, V2={v2}, V3={v3}")
                    print(f"Predicted gesture: {prediction}")
                    
                    # Save data locally
                    save_to_csv(v1, v2, v3, prediction, data_list)
                    
                    # Send to cloud
                    send_to_thingspeak(v1, v2, v3, prediction)
                    
                except ValueError as e:
                    print(f"Data parsing error: {e}")
                    
            else:
                print(f"Invalid data format. Expected 3 values, got {len(values)}")
            
            print(f"Counter: {counter}")
            print("-" * 40)
            
            sleep(SLEEP_INTERVAL)
            counter += 1
            
    except KeyboardInterrupt:
        print("\nStopping data collection...")
        
        # Final save of any remaining data
        if data_list:
            df = pd.DataFrame(
                data_list, 
                columns=['Timestamp', 'V1', 'V2', 'V3', 'Prediction']
            )
            df.to_csv(DATA_FILE_PATH, index=False)
            print(f"Final data saved to {DATA_FILE_PATH}")
        
        print(f"Total data points collected: {len(data_list)}")
        print("WiFi data collection completed.")


if __name__ == "__main__":
    main()

