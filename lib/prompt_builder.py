import json
from dataclasses import dataclass

from rich.console import Console
from rich.traceback import install

install()
console = Console()


@dataclass
class PromptMessage:
    """GPT messages"""

    role: str
    content: str


@dataclass
class PromptOptions:
    """Options for GPT."""

    model: str = "gpt-3.5-turbo"
    temperature: float = 0.5
    max_tokens: int = 50
    stop: int = None
    top_p: float = 1.0
    presence_penalty: float = 0.0
    frequency_penalty: float = 0.0


class PromptBuilder:
    """Prompt builder for GPT"""

    def __init__(self, **kwargs) -> None:
        self.messages = []
        self.options = PromptOptions(**kwargs)

    def text(self, text: str) -> None:
        """Add standard text prompt."""
        self._add_message("user", text)

    def json(self, template) -> None:
        """Add JSON prompt, enforcing strict JSON format on the output from GPT"""
        json_template = json.dumps(template, separators=(",", ":"))

        prompt = f"IMPORTANT: Make a JSON formatted output, without spaces and new lines with format: `{json_template}`. Make output only proper JSON file, nothing else."  # pylint: disable=line-too-long
        self._add_message("system", prompt)

    def get_messages(self) -> list:
        """Get messages for GPT grouped by role."""
        messages = {"user": [], "system": []}

        for message in self.messages:
            messages[message.role].append(message.content)

        return [
            {"role": "user", "content": "\n".join(messages["user"])},
            {"role": "system", "content": "\n".join(messages["system"])},
        ]

    def _add_message(self, role: str, content: str) -> None:
        """Add message to prompt."""
        self.messages.append(PromptMessage(role=role, content=content))
