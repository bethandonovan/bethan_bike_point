import json as j
import os
import time 
import logging
from datetime import datetime
import requests as r 

logger = logging.getLogger(__name__)

def extract_json(url:str, data_dir:str, timestamp:str, max_retry:int, delay:int):
    """Automates json extraction

    Args:
        url (str): URL to download JSON from
        data_dir (str): Directory to save the data in
        timestamp (str): Timestamp for the filename
        max_retry (int): Number of times it will try to call the API
        delay (int): How long to wait in between retries
    """

    os.makedirs(data_dir, exist_ok=True)

    filename = f'{data_dir}/{timestamp}.json'

    
    attempt = 0


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