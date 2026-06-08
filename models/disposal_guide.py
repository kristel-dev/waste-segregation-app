# models/disposal_guide.py
"""Disposal Guide Value Object."""


class DisposalGuide:
    def __init__(self, instructions: str, tips: list, warnings: list = None):
        self._instructions = instructions
        self._tips = tuple(tips)
        self._warnings = tuple(warnings) if warnings else tuple()

    @property
    def instructions(self) -> str:
        return self._instructions

    @property
    def tips(self) -> tuple:
        return self._tips

    @property
    def warnings(self) -> tuple:
        return self._warnings

    def __str__(self) -> str:
        lines = [f"Instructions: {self._instructions}"]
        if self._tips:
            lines.append("Tips: " + ", ".join(self._tips))
        if self._warnings:
            lines.append("Warnings: " + ", ".join(self._warnings))
        return "\n".join(lines)
