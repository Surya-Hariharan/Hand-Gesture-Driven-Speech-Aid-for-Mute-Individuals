import serial
import time
import os
import urllib.request
import http
import pandas as pd
from time import sleep
from datetime import datetime
import win32com.client

r=["hello","how are you","happy morning","good day","i am hungry","good night","i am not feeling well","well done","who are you","come here","happy"]
from sklearn.preprocessing import StandardScaler

import pickle
filename = '../models/gesture_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))

serial_port = 'COM3'  
baud_rate = 9600
ser = serial.Serial(serial_port, baud_rate)
print("Serial port opened successfully.")

time.sleep(2)
threshold = 0.0
data_list = []
try:
    while True:
        data = ser.readline().decode().strip()
        print("Received data:", data)
        values = data.split(',')
        if len(values) == 5:
            v1, v2,v3,v4,v5 = values
            features = [[float(v1), float(v2),float(v3), float(v4),float(v5)]]
            predicted = loaded_model.predict(features)
            print(predicted)
            print(r[int(predicted)])
            
            speaker = win32com.client.Dispatch("SAPI.SpVoice")
            speaker.Speak(str(r[int(predicted)]))
        
except KeyboardInterrupt:
    ser.close()
    print("Serial port closed.")

