"""Unit Tests for Repository."""

import pytest
from repositories.waste_repository import WasteRepository


class TestWasteRepository:
    def test_initial_items_loaded(self):
        repo = WasteRepository()
        items = repo.get_all_items()
        assert len(items) > 0
    
    def test_get_item_exists(self):
        repo = WasteRepository()
        item = repo.get_item("banana peel")
        assert item is not None
    
    def test_get_item_not_exists(self):
        repo = WasteRepository()
        item = repo.get_item("nonexistent")
        assert item is None
    
    def test_search_by_name(self):
        repo = WasteRepository()
        results = repo.search_by_name("bottle")
        assert len(results) > 0
    
    def test_search_no_results(self):
        repo = WasteRepository()
        results = repo.search_by_name("xyz123")
        assert results == []