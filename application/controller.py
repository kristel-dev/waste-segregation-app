# controller.py
"""Main Application Controller."""

from typing import Optional
from strategies.input.console_input import ConsoleInput
from strategies.output.screen_display import ScreenDisplay
from strategies.output.gui_display import GUIDisplay
from strategies.input.gui_input import GUIInput
from services.waste_service import WasteService


class WasteSegregationApp:
    def __init__(self, input_strategy, output_strategy, service: WasteService):
        self._input_strategy = input_strategy
        self._output_strategy = output_strategy
        self._service = service
        self._running = False
        self._gui_mode = isinstance(output_strategy, GUIDisplay)

    def run(self) -> None:
        if self._gui_mode:
            self._running = True
            self._display_welcome()
            return

        self._running = True
        self._display_welcome()

        while self._running:
            self._show_menu()
            choice = self._input_strategy.get_user_input("\nEnter your choice: ")
            self._handle_menu_choice(choice)

    def _show_menu(self) -> None:
        menu = """
=========================
WASTE SEGREGATION GUIDE
=========================
1. Search for waste item
2. Browse by category
3. View all items
4. Exit
"""
        self._output_strategy.display(menu)

    def _handle_menu_choice(self, choice: str) -> None:
        handlers = {
            "1": self._handle_search,
            "2": self._handle_browse,
            "3": self._handle_view_all,
            "4": self._handle_exit,
        }
        handler = handlers.get(choice)
        if handler:
            handler()
        else:
            self._output_strategy.display("Invalid choice.")

    def _handle_search(self, query: Optional[str] = None) -> list:
        if query is None:
            query = self._input_strategy.get_user_input("\nEnter item name: ")

        results = self._service.search_waste_item(query)

        if self._gui_mode and isinstance(self._output_strategy, GUIDisplay):
            self._output_strategy.display_results(results, f"Search results for '{query}'")
        else:
            if not results:
                self._output_strategy.display(f"\nNo items found for: {query}")
            else:
                for item in results:
                    self._output_strategy.display(f"\n--- {item.name} ---")
                    self._output_strategy.display(f"Category: {item.category}")
                    self._output_strategy.display(str(item.disposal_guide))

        return results

    def _handle_browse(self, category_value: Optional[str] = None) -> list:
        categories = self._service.get_all_categories()

        if self._gui_mode:
            if category_value:
                category = None
                for cat in categories:
                    if cat.value == category_value:
                        category = cat
                        break
                if category:
                    items = self._service.get_items_by_category(category)
                    if isinstance(self._output_strategy, GUIDisplay):
                        self._output_strategy.display_results(items, f"Category: {category_value}")
                    return items
            return []

        # Console mode
        self._output_strategy.display("\nCategories:")
        for i, cat in enumerate(categories, 1):
            self._output_strategy.display(f"{i}. {cat}")

        choice = self._input_strategy.get_user_input("\nSelect category number: ")
        try:
            index = int(choice) - 1
            if 0 <= index < len(categories):
                items = self._service.get_items_by_category(categories[index])
                for item in items:
                    self._output_strategy.display(f"- {item.name}")
                return items
        except ValueError:
            self._output_strategy.display("Invalid selection.")

        return []

    def _handle_view_all(self) -> list:
        items = self._service.repository.get_all_items()

        if self._gui_mode and isinstance(self._output_strategy, GUIDisplay):
            self._output_strategy.display_results(items, "All Items")
        else:
            self._output_strategy.display(f"\nTotal items: {len(items)}")
            for item in items:
                self._output_strategy.display(f"- {item.name} ({item.category})")

        return items

    def _handle_exit(self) -> None:
        self._output_strategy.display("\nThank you for using Waste Segregation Guide!")
        self._running = False

    def _display_welcome(self) -> None:
        welcome = """
======================================
WELCOME TO WASTE SEGREGATION GUIDE
======================================
Proper waste disposal protects our environment.
"""
        if self._output_strategy:
            self._output_strategy.display(welcome)

    def get_item_details(self, item_name: str):
        """Get detailed disposal guide for an item."""
        item = self._service.get_item_info(item_name)
        if item and isinstance(self._output_strategy, GUIDisplay):
            self._output_strategy.display_item_details(item)
        return item

    @property
    def service(self) -> WasteService:
        return self._service
