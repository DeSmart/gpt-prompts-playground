"""Simple decorator to calculate the time taken by a function to execute."""
import time
from rich.console import Console
from rich.traceback import install
import logging


install()
console = Console()


def timer(func):
    """Calculate the time taken by a function to execute."""

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_seconds = round(end_time - start_time, 1)

        logging.info("%s took %d seconds to execute.", func.__name__, elapsed_seconds)

        return result

    return wrapper
