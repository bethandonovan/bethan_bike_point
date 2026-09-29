#import packages
from dotenv import load_dotenv
import os
import boto3
import logging
from datetime import datetime


def load_files_to_s3(data_dir:str, AWS_ACCESS_KEY:str, AWS_SECRET_ACCESS_KEY:str, AWS_BUCKET_NAME:str):
    """_summary_

    Args:
        data_dir (str): _description_
        AWS_ACCESS_KEY (str): _description_
        AWS_SECRET_ACCESS_KEY (str): _description_
        AWS_BUCKET_NAME (str): _description_
    """

    #connect to s3 client
    s3_client = boto3.client(
        's3',
        aws_access_key_id = AWS_ACCESS_KEY,
        aws_secret_access_key = AWS_SECRET_ACCESS_KEY
    )

    #define variables to upload data file, using names created in extract.py
    files_to_upload = os.listdir(data_dir)

    for file in files_to_upload:
        file_to_upload = f'{data_dir}/{file}'
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

