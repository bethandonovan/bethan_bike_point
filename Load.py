#import packages
from dotenv import load_dotenv
import os
import boto3
import logging
from datetime import datetime

#load dotenv
load_dotenv()

#define access keys
AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_BUCKET_NAME = os.getenv('AWS_BUCKET_NAME')

log_dir = 'log'
timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
log_filename = f'{log_dir}/load_log_{timestamp}.log'


logging.basicConfig(
    filename = log_filename,
    format = '%(asctime)s - %(levelname)s - %(message)s',
    level = logging.INFO
)

logger = logging.getLogger()
logging.info('Logger Successfully Initialised')

#connect to s3 client
s3_client = boto3.client(
    's3',
    aws_access_key_id = AWS_ACCESS_KEY,
    aws_secret_access_key = AWS_SECRET_ACCESS_KEY
)

#define variables to upload data file, using names created in extract.py

files_to_upload = os.listdir('data')

for file in files_to_upload:
    file_to_upload = f'data/{file}'
    try:
    #upload the file to s3 bucket 
        s3_client.upload_file(
            file_to_upload,
            AWS_BUCKET_NAME,
            file
        )
        print(f'{file} has been uploaded successfully')
        logging.info(f'{file} has been uploaded successfully')
        os.remove(file_to_upload)
    except Exception as e:
        print('An error has occured')
        logging.warning('An error has occured')

