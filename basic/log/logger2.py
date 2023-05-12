import logging
import uuid
import inspect
import sys
import socket
from pathlib import Path
import datetime as dt
from basic.log.notebook import is_jupyter_notebook

CRITICAL = logging.CRITICAL
ERROR = logging.ERROR
WARN = logging.WARN
INFO = logging.INFO
DEBUG = logging.DEBUG

__SHORT_FORMAT = '%(asctime)s %(app_name)s [Session id: %(session_id)s] %(levelname)s [%(module)s:%(lineno)d][%(client)s]: %(message)s'
__LONG_FORMAT = '%(asctime)s %(app_name)s [Session id: %(session_id)s] [%(levelname)s] ({}-{}) [%(module)s:%(lineno)d][%(client)s]: %(message)s'


class LoggingContext:
    Client = ''
    Application_name = 'DTT'
    Session_id = uuid.uuid4()


'''
logging Filter
'''
class AppFilter(logging.Filter):
    def filter(self, record):
        record.app_name = LoggingContext.Application_name
        record.client = LoggingContext.Client
        record.session_id = LoggingContext.Session_id
        return True


def logger(level=INFO, name=None):
    if name is None:
        name = __get_logger_name()

    log = logging.getLogger(name)
    # os.makedirs(__log_folder(), exist_ok=True)
    log.addFilter(AppFilter())
    log.setLevel(level)
    # log.addHandler(__file_handler()) File handler disabled
    if is_jupyter_notebook():
        log.addHandler(__notebook_handler())
        log.addHandler(__jupyter_stdout_handler())
    else:
        log.addHandler(__console_handler())
    return log

def service_logger(level=INFO, name='log_service'):
    log = logging.getLogger(name)
    log.addFilter(AppFilter())
    log.setLevel(level)
    if not log.handlers:
        if is_jupyter_notebook():
            log.addHandler(__jupyter_stdout_handler())
        else:
            log.addHandler(__console_handler())
    return log

def __get_logger_name():
    frame = inspect.stack()[2].frame
    return frame.f_locals['__name__'].split('.')[-1]

def __file_handler(include_host=False):
    fh = logging.FileHandler(__log_file(), mode='a', encoding='utf-8')
    fh.setFormatter(__formatter())
    return fh


def __notebook_handler():
    nb = logging.StreamHandler(sys.stdout)
    nb.setFormatter(logging.Formatter('%(message)s'))
    return nb


def __jupyter_stdout_handler():
    nb = logging.StreamHandler(sys.__stdout__)
    nb.setFormatter(__formatter(True))
    return nb


def __console_handler():
    ch = logging.StreamHandler()
    ch.setFormatter(__formatter())
    return ch

def __formatter(include_host=False):
    hostname = socket.gethostname()
    host = socket.gethostbyname(hostname)
    if include_host:
        msg_format = __LONG_FORMAT.format(hostname, host)
    else:
        msg_format = __SHORT_FORMAT
    return logging.Formatter(msg_format)

def __log_folder():
    return Path(__file__).parent.parent.parent / 'logs'

def __log_file():
    now = dt.datetime.now()
    year = f'{now.year}'
    month = f'{now:%m}'
    filename = f'logs_nb_{year}_{month}.txt'
    return __log_folder() / filename

def name_and_args():
    caller = inspect.stack()[1][0]
    args, _, _, values = inspect.getargvalues(caller)
    print(args)
    return [(i, values[i]) for i in args]


if __name__ == "__main__":
    print(Path(__file__).parent.parent)
    path = __log_file()
    print(path)
    my_logger = logger()
    my_logger.info("fasdfa")
    name_and_args()



