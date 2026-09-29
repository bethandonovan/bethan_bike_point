
from modules.log_initialise import set_up_logging
from datetime import datetime
from modules.extract_function import extract_json

timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S')

logger = set_up_logging('logs', timestamp)
logger.info('Logger Successfully Initialised')

data_dir = 'data'
url = 'https://api.tfl.gov.uk/BikePoint/'
max_retry = 5
delay = 10

extract_json(url, data_dir, timestamp, max_retry, delay)