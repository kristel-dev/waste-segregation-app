"""Output Strategy Abstract Base Class."""

from abc import ABC, abstractmethod


class OutputStrategy(ABC):
    @abstractmethod
    def display(self, content: str) -> None:
        pass
