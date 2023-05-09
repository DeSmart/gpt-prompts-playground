"""Various JSON-related checks."""
import json
from re import match, DOTALL, MULTILINE


def parse_json(json_str: str) -> dict:
    """Checks if string is valid JSON and returns it as dict."""
    try:

        # Additional parsing of the response to get rid of the gpt junk (leaves only JSON)
        json_regex = r"^[^\{\}\[\]]*([\{\[].+[\}\]])[^\{\}\[\]]*$"
        matched = match(json_regex, json_str, flags=DOTALL | MULTILINE)

        if not matched:
            raise ValueError("Can't get proper JSON from json_str.")

        return json.loads(matched[1])
    except ValueError as exc:
        raise ValueError("Can't parse json_str to JSON.") from exc
