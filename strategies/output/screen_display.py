"""Screen Display Strategy."""

from .output_strategy import OutputStrategy


class ScreenDisplay(OutputStrategy):
    def __init__(self, use_colors: bool = True):
        self._use_colors = use_colors

    def display(self, content: str) -> None:
        print(content)
