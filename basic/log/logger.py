'''
logging module
reference: https://docs.python.org/3/library/logging.html
'''
import logging
import sys
## by delfault logging level is above warning

# basic config
logging.basicConfig(level=logging.DEBUG, filename="log.log", filemode="w",
                    format="%(asctime)s - %(levelname)s - %(message)s")

logging.debug("Debug Level")
logging.info("Info Level")
logging.warning("Warning level")
logging.error("Error Level")
logging.critical("Critial Level")

try:
    1/0
except ZeroDivisionError as e:
    logging.error("ZeroDivisionError", exc_info=True)


## Customer Logger
logger = logging.getLogger(__name__)
handler = logging.FileHandler("test.log")
formater = logging.Formatter("%(asctime)s - %(name)s - %(message)s")
handler.setFormatter(formater)
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)
logger.info("test the customer logger")

## logging filter

class LevelFilter(logging.Filter):
    def filter(self, record):
        if record.levelno < logging.WARNING:
            return False
        else:
            return True

stream_logger = logging.getLogger("streaming")
stream_logger.setLevel(logging.INFO)
stream_handler = logging.StreamHandler(sys.stdout)
stream_logger.addHandler(stream_handler)
stream_logger.addFilter(LevelFilter())
stream_logger.info("Filter logging info")
stream_logger.warning("Filter logging Warning")


