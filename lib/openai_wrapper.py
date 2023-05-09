"""Simple wrapper for the OpenAI API."""
from rich.traceback import install
from rich.console import Console

from os import getenv
import logging
import openai
from dotenv import load_dotenv
from lib.prompt_builder import PromptBuilder
import json

install()
console = Console()
load_dotenv()

openai.api_key = getenv("OPENAI_API_KEY")


def get_response(
    prompt: PromptBuilder,
):
    """Get a response from the OpenAI API."""
    logging.info(
        "Prompt:\n%s", json.dumps(prompt.get_messages(), ensure_ascii=False, indent=2)
    )

    res = openai.ChatCompletion.create(
        messages=prompt.get_messages(),
        model=prompt.options.model,
        temperature=prompt.options.temperature,
        max_tokens=prompt.options.max_tokens,
        stop=prompt.options.stop,
        top_p=prompt.options.top_p,
        frequency_penalty=prompt.options.frequency_penalty,
        presence_penalty=prompt.options.presence_penalty,
    )

    logging.debug("Response:\n%s", res)
    return res
