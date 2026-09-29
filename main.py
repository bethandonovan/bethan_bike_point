
from modules.log_initialise import set_up_logging
from datetime import datetime
from modules.extract_function import extract_json
from modules.load_function import load_files_to_s3
timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
import os
from dotenv import load_dotenv

#load dotenv
load_dotenv()

logger = set_up_logging('logs', timestamp)
logger.info('Logger Successfully Initialised')

data_dir = 'data'
url = 'https://api.tfl.gov.uk/BikePoint/'
max_retry = 5
delay = 10
AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_BUCKET_NAME = os.getenv('AWS_BUCKET_NAME')

extract_json(url, data_dir, timestamp, max_retry, delay)



load_files_to_s3(data_dir, AWS_ACCESS_KEY, AWS_SECRET_ACCESS_KEY, AWS_BUCKET_NAME )
