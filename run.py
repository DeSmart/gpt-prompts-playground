import json
import logging
from sys import exit

from rich.console import Console
from rich.traceback import install

import prompts.recommend as prompts_recommend
from lib.logger import install_logger

install()
install_logger("INFO")
console = Console()

# https://platform.openai.com/examples

try:
    # ret = prompts_recommend.recommend_prompt_1()
    ret = prompts_recommend.recommend_prompt_2()
    logging.info("GPT response:\n%s", json.dumps(ret, ensure_ascii=False, indent=2))
except Exception as error:  # pylint: disable=broad-except
    logging.error("Error parsing the response: %s", error)
    exit(1)
