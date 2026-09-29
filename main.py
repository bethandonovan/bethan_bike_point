
from modules.log_initialise import set_up_logging
from datetime import datetime

timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S')

logger = set_up_logging('logs', timestamp)
logger.info('Logger Successfully Initialised')