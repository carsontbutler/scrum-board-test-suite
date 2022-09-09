from datetime import datetime
import logging
import time

# Logging setup
timestr = time.strftime("%Y-%m-%d_%H%M%S")
log = logging.getLogger(__name__)
logging.basicConfig(filename=timestr, encoding='utf-8',
                    level=logging.DEBUG, format='%(asctime)s %(message)s')

log = logging.getLogger(__name__)

def pytest_configure(config):
    """ Create a log file if log_file is not mentioned in *.ini file"""
    if not config.option.log_file:
        timestamp = datetime.strftime(datetime.now(), '%Y-%m-%d_%H-%M-%S')
        config.option.log_file = 'log_' + timestamp
