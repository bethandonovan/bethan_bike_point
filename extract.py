import requests as r 
import os as os
import json as j
from datetime import datetime
import time
from modules.log_initialise import set_up_logging
import logging
from dotenv import load_dotenv

#load dotenv
load_dotenv()

url = 'https://api.tfl.gov.uk/BikePoint/'
data_dir = 'data' 
os.makedirs(data_dir, exist_ok=True)
timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
filename = f'{data_dir}/{timestamp}.json'

log_dir = 'log'

logger = set_up_logging(log_dir, timestamp)
logger.info('Logger Successfully Initialised')

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
                logging.info(f'File {filename} was successfully saved')
            except Exception as e:
                print(f'An error has occured {e}')
                logging.warning(f'An error has occured {e}')
            break 
        else: 
            print('No Data Returned')
            logging.warning('No Data Returned')
            break    
    elif  status <200 or status >=500:
        time.sleep(delay)
        attempt += 1
        print(f'Status code: {status}. Retrying. Attempt Number {attempt}')
        logging.info(f'Status code: {status}. Retrying. Attempt Number {attempt}')

    else:
        print(f'Error. Status code {status}. Fix it')
        logging.critical(f'Error. Status code {status}. Fix it')