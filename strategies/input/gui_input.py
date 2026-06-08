# strategies/input/gui_input.py
"""GUI Input Strategy for Tkinter."""

from typing import Optional
from .input_strategy import InputStrategy


class GUIInput(InputStrategy):
    """Input strategy that uses Tkinter variables for input."""

    def __init__(self):
        self._search_var = None
        self._category_var = None

    def set_search_variable(self, var):
        """Set the StringVar for search input."""
        self._search_var = var

    def set_category_variable(self, var):
        """Set the StringVar for category selection."""
        self._category_var = var

    def get_user_input(self, prompt: str) -> str:
        """Get input from the appropriate source."""
        # This can be extended based on context
        if self._search_var:
            return self._search_var.get().strip()
        return input(prompt)

    def get_search_query(self) -> str:
        """Get search query from search variable."""
        return self._search_var.get().strip() if self._search_var else ""

    def get_selected_category(self) -> str:
        """Get selected category from category variable."""
        return self._category_var.get() if self._category_var else ""