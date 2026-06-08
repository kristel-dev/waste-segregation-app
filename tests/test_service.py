"""Unit Tests for Service."""

import pytest
from services.waste_service import WasteService
from repositories.waste_repository import WasteRepository


class TestWasteService:
    def test_service_initialization(self):
        repo = WasteRepository()
        service = WasteService(repo)
        assert service.repository == repo
    
    def test_search_waste_item(self):
        repo = WasteRepository()
        service = WasteService(repo)
        results = service.search_waste_item("battery")
        assert len(results) > 0
    
    def test_search_no_results(self):
        repo = WasteRepository()
        service = WasteService(repo)
        results = service.search_waste_item("nonexistent")
        assert results == []
    
    def test_get_all_categories(self):
        repo = WasteRepository()
        service = WasteService(repo)
        categories = service.get_all_categories()
        assert len(categories) > 0