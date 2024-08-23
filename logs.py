"""Module doc string"""

import logging
import os
import sys

from colorama import Back, Fore, Style, init

LOGGER_LEVEL = os.getenv("LOGGER_LEVEL", "INFO")

# Initialize colorama
init(autoreset=True)

logger = logging.getLogger(__name__)

if not logger.hasHandlers():
    logger.propagate = False
    logger.setLevel(LOGGER_LEVEL)

    # Define color codes for different log levels
    log_colors = {
        logging.DEBUG: Fore.CYAN,
        logging.INFO: Fore.GREEN,
        logging.WARNING: Fore.YELLOW,
        logging.ERROR: Fore.RED,
        logging.CRITICAL: Fore.RED + Back.WHITE + Style.BRIGHT,
    }

    class ColoredFormatter(logging.Formatter):
        """Module doc string"""

        def format(self, record):
            """Module doc string"""

            levelno = record.levelno
            color = log_colors.get(levelno, "")

            # Format the message
            message = record.getMessage()

            # Format the rest of the log details
            details = self._fmt % {
                "asctime": self.formatTime(record, self.datefmt),
                "levelname": record.levelname,
                "module": record.module,
                "funcName": record.funcName,
                "lineno": record.lineno,
            }

            # Combine details and colored message
            return f"{Fore.WHITE}{details} :: {color}{message}{Style.RESET_ALL}"

    normal_handler = logging.StreamHandler(sys.stdout)
    normal_handler.setLevel(logging.DEBUG)
    normal_handler.addFilter(lambda logRecord: logRecord.levelno < logging.WARNING)

    error_handler = logging.StreamHandler(sys.stderr)
    error_handler.setLevel(logging.WARNING)

    formatter = ColoredFormatter(
        "%(asctime)s :: %(levelname)s :: %(module)s :: %(funcName)s :: %(lineno)d"
    )

    normal_handler.setFormatter(formatter)
    error_handler.setFormatter(formatter)

    logger.addHandler(normal_handler)
    logger.addHandler(error_handler)
