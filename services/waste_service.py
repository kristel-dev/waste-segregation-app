"""Waste Service - Business logic."""

from models.waste_item import WasteItem
from models.waste_category import WasteCategory
from models.disposal_guide import DisposalGuide
from repositories.waste_repository import WasteRepository


class WasteService:
    def __init__(self, repository: WasteRepository) -> None:
        if not isinstance(repository, WasteRepository):
            raise TypeError("Invalid repository type")
        self._repository = repository

    @property
    def repository(self) -> WasteRepository:
        return self._repository

    def search_waste_item(self, query: str) -> list[WasteItem]:
        if not query or not query.strip():
            return []
        return self._repository.search_by_name(query)

    def get_item_info(self, item_name: str) -> WasteItem | None:
        if not item_name or not item_name.strip():
            return None
        return self._repository.get_item(item_name)

    def get_disposal_guide(self, item_name: str) -> DisposalGuide | None:
        item = self.get_item_info(item_name)
        return item.disposal_guide if item else None

    def get_all_categories(self) -> list[WasteCategory]:
        return list(WasteCategory)

    def get_items_by_category(self, category: WasteCategory) -> list[WasteItem]:
        return self._repository.get_items_by_category(category)