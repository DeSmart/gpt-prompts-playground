"""Decorator which takes json response from GPT-3 and parses it to python dict."""

from functools import wraps

from rich.console import Console
from rich.traceback import install

from lib.timer import timer

install()
console = Console()
