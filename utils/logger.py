import logging
import os

LOG_DIR = "logs"

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

LOG_FILE = os.path.join(
    LOG_DIR,
    "movie_booking.log"
)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def log_info(message):

    logging.info(message)


def log_error(message):

    logging.error(message)


def log_warning(message):

    logging.warning(message)