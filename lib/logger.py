"""Logging module for Dekick""" ""
import logging
from rich.logging import RichHandler


def install_logger(level: str = ""):
    """Installs the logger and sets the log level and filenam"""

    level = "INFO" if level == "" else level
    # log_format = "%(asctime)s  %(message)s"
    log_format = "[%(module)s:%(lineno)d] %(message)s"

    rich_handler = RichHandler(
        rich_tracebacks=True,
        level=level,
        show_time=True,
        show_path=True,
        tracebacks_show_locals=True,
        show_level=True,
        omit_repeated_times=False,
        enable_link_path=True,
    )

    config = {
        # "force": True,
        "level": level,
        "format": log_format,
        "datefmt": "[%Y-%m-%d %H:%M:%S]",
        "handlers": [rich_handler],
    }

    logging.basicConfig(**config)
