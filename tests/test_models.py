"""Unit Tests for Models."""

import pytest
from models.waste_item import WasteItem
from models.waste_category import WasteCategory
from models.disposal_guide import DisposalGuide


class TestWasteCategory:
    def test_category_values(self):
        assert WasteCategory.BIODEGRADABLE.value == "Biodegradable"
        assert WasteCategory.RECYCLABLE.value == "Recyclable"
        assert WasteCategory.HAZARDOUS.value == "Hazardous"


class TestDisposalGuide:
    def test_create_guide(self):
        guide = DisposalGuide("Recycle it", ["Tip 1"], ["Warning 1"])
        assert guide.instructions == "Recycle it"
        assert guide.tips == ("Tip 1",)
        assert guide.warnings == ("Warning 1",)


class TestWasteItem:
    def test_create_item(self):
        guide = DisposalGuide("Test", ["Tip"], [])
        item = WasteItem("Test Item", WasteCategory.RECYCLABLE, guide)
        assert item.name == "Test Item"
        assert item.category == WasteCategory.RECYCLABLE
    
    def test_matches_query(self):
        guide = DisposalGuide("Test", [], [])
        item = WasteItem("Plastic Bottle", WasteCategory.RECYCLABLE, guide)
        assert item.matches_query("plastic") is True
        assert item.matches_query("glass") is False