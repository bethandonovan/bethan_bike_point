import requests as r 
import os as os
import json as j
from datetime import datetime
import time as t

url = 'https://api.tfl.gov.uk/BikePoint/'
data_dir = 'data' 
os.makedirs(data_dir, exist_ok=True)
timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
filename = f'{data_dir}/{timestamp}.json'

max_retry = 5
attempt = 0
delay = 10

while attempt < max_retry:

    response = r.get(url)
    status = response.status_code

    if 200 <= status < 300:
        data = response.json()
        with open(filename, 'w') as file: 
            j.dump(data, file)
        print(f'File {filename} was successfully saved')
        break

    elif  status <200 or status >=500:
        t.sleep(delay)
        attempt += 1
        print(f'Status code: {status}. Retrying. Attempt Number {attempt}')

    else:
        print(f'Error. Status code {status}. Fix it')