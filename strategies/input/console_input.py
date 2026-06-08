"""Console Input Strategy."""

from .input_strategy import InputStrategy


class ConsoleInput(InputStrategy):
    def get_user_input(self, prompt: str) -> str:
        return input(prompt).strip()
