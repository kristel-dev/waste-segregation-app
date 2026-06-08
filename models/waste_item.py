"""Waste Item Entity."""

from .waste_category import WasteCategory
from .disposal_guide import DisposalGuide


class WasteItem:
    def __init__(self, name: str, category: WasteCategory, disposal_guide: DisposalGuide):
        self._name = name
        self._category = category
        self._disposal_guide = disposal_guide

    @property
    def name(self) -> str:
        return self._name

    @property
    def category(self) -> WasteCategory:
        return self._category

    @property
    def disposal_guide(self) -> DisposalGuide:
        return self._disposal_guide

    def matches_query(self, query: str) -> bool:
        return query.lower().strip() in self._name.lower()

    def __str__(self) -> str:
        return f"{self._name} ({self._category})\n{self._disposal_guide}"