"""Input Strategy Abstract Base Class."""

from abc import ABC, abstractmethod


class InputStrategy(ABC):
    @abstractmethod
    def get_user_input(self, prompt: str) -> str:
        pass
