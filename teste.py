import serial
import requests
import json
import random
import time

with serial.Serial('COM5', 9600, timeout=2) as ser:
    while 1:
        x = ser.readline()          # read one byte
        print(x)

        url = "https://sheet.best/api/sheets/12bd5c43-09c2-4412-83e8-398e1946672d"
        data =[ {"id": '10',
                "localizacao": "-20.495034, -54.626731",
                "data": "19/10/2019 14:47:00",
                "temperatura": x.decode("utf-8")[:-2],
                "notificado": True
                }]
        headers = {'Content-type': 'application/json'}
        r = requests.post(url, data=json.dumps(data), headers=headers)
        print ("OK")
        #time.sleep(1)
