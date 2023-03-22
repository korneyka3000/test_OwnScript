import logging

from .lighter import Lighter

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s",
    filename="api_lighter.log",
    filemode="w",
)
