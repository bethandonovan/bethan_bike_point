import requests as r 
import os as os
import json as j
from datetime import datetime

url = 'https://api.tfl.gov.uk/BikePoint/'
data_dir = 'data' 
os.makedirs(data_dir, exist_ok=True)
timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
filename = f'{data_dir}/{timestamp}.json'

response = r.get(url)

status = response.status_code

data = response.json()

with open(filename, 'w') as file: 
    j.dump(data, file)

