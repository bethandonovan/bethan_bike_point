import requests as r 
import os as os
import json as j
from datetime import datetime
import time as t
import logging as l

url = 'https://api.tfl.gov.uk/BikePoint/'
data_dir = 'data' 
os.makedirs(data_dir, exist_ok=True)
timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
filename = f'{data_dir}/{timestamp}.json'


log_dir = 'log'
os.makedirs(log_dir, exist_ok=True)
log_filename = f'{log_dir}/{timestamp}.json'

l.basicConfig(
    filename = log_filename,
    format = '%(asctime)s - %(levelname)s - %(message)s',
    level = l.INFO
)

logger = l.getLogger()
l.info('Logger Successfully Initialised')

max_retry = 5
attempt = 0
delay = 10

while attempt < max_retry:

    response = r.get(url)
    status = response.status_code

    if 200 <= status < 300:
        data = response.json()
        if len(data) > 0:
            try:
                with open(filename, 'w') as file: 
                    j.dump(data, file)
                print(f'File {filename} was successfully saved')
                l.info(f'File {filename} was successfully saved')
            except Exception as e:
                print(f'An error has occured {e}')
                l.warning(f'An error has occured {e}')
            break 
        else: 
            print('No Data Returned')
            l.warning('No Data Returned')
            break    
    elif  status <200 or status >=500:
        t.sleep(delay)
        attempt += 1
        print(f'Status code: {status}. Retrying. Attempt Number {attempt}')
        l.info(f'Status code: {status}. Retrying. Attempt Number {attempt}')

    else:
        print(f'Error. Status code {status}. Fix it')
        l.critical(f'Error. Status code {status}. Fix it')