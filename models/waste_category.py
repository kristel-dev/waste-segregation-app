"""Waste Category Enumeration."""

from enum import Enum


class WasteCategory(Enum):
    BIODEGRADABLE = "Biodegradable"
    NON_BIODEGRADABLE = "Non-Biodegradable"
    RECYCLABLE = "Recyclable"
    HAZARDOUS = "Hazardous"
    ELECTRONIC_WASTE = "Electronic Waste"
    CONSTRUCTION = "Construction Waste"
    MEDICAL = "Medical Waste"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return self.value