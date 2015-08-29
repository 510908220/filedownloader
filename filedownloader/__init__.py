import logging
from .http_file import download as http_download
from .http_file import downloads as http_downloads

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# console handler
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter(
	'%(asctime)s  %(levelname)10s - %(message)s   [%(filename)s %(funcName)s line:%(lineno)d threadid:%(thread)d]')
console.setFormatter(formatter)
logger.addHandler(console)

# file handler
file_handler = logging.FileHandler(__name__ + ".log", "w")
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter(
	'%(asctime)s  %(levelname)10s - %(message)s   [%(filename)s %(funcName)s line:%(lineno)d threadid:%(thread)d]')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

__all__ = ["http_download", "http_downloads"]
