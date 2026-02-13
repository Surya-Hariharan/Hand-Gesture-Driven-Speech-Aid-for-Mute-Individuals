import os
import urllib.request
import http
import pandas as pd
import re
from time import sleep
from datetime import datetime

import pickle
filename = 'model.sav'
loaded_model = pickle.load(open(filename, 'rb'))

base = "http://192.168.137.233/"

def transfer(my_url):   #use to send and receive data
    try:
        n = urllib.request.urlopen(base + my_url).read()
        n = n.decode("utf-8")
        return n
    except http.client.HTTPException as e:
        return e

# Specify the absolute path for the Excel file
excel_file_path = r"C:\Users\SURYA HA\OneDrive\Desktop\Hand_gest_2024_amirtha\data1.csv"

# Create an empty list to store data
data_list = []

# Create a function to split and save data to Excel
def save_to_excel(v1, v2, v3, v4):
    data_list.append([v1, v2, v3, v4])
    df = pd.DataFrame(data_list, columns=['V1', 'V2', 'V3', 'Target'])
    df.to_excel(excel_file_path, index=False)

ct = 0
while True:
    res = transfer(str(ct))
    response = str(res)
    print(response)
    
    # Split the received data
    values = response.split('-')
    if len(values) == 3:
        v1, v2, v3 = values
        #save_to_excel(v1, c1, v2, c2)
        reports = [[v1, v2, v3]]
        predicted = loaded_model.predict(reports)
        print(predicted)
        #ct=int(predicted)
        print(ct)
        conn = urllib.request.urlopen("https://api.thingspeak.com/update?api_key=QIXHGRZ00NB0BGZU&field1="+str(v1)+"&field2="+str(v2)+"&field3="+str(v3)+"&field4="+str(predicted))
        response = conn.read()
        print ("http status code=%s" % (conn.getcode()))
        print("")
    
    sleep(1)

