"""GUI Display Strategy for Tkinter Treeview."""

from typing import Callable, Optional
from tkinter import ttk
import tkinter as tk

from .output_strategy import OutputStrategy


class GUIDisplay(OutputStrategy):
    """Output strategy that displays to a Tkinter treeview and text widget."""

    def __init__(
        self,
        tree: ttk.Treeview,
        details_text: tk.Text,
        status_callback: Optional[Callable[[str], None]] = None,
    ):
        self._tree            = tree
        self._details_text    = details_text
        self._status_callback = status_callback
        self._current_items   = []

    # ── OutputStrategy contract ──────────────────────────────────────────────
    def display(self, content: str) -> None:
        """Fallback: print to console (used in non-GUI contexts)."""
        print(content)

    # ── GUI-specific methods ─────────────────────────────────────────────────
    def display_results(self, items: list, title: str = "Results") -> None:
        """Populate the treeview with a list of WasteItem objects."""
        # Clear existing rows
        for row in self._tree.get_children():
            self._tree.delete(row)

        self._current_items = items

        if not items:
            self._tree.insert("", tk.END, text="No items found", values=("", ""))
            self._set_details("No items to display.\n\nTry a different search term or category.")
            if self._status_callback:
                self._status_callback("No items found")
            return

        for idx, item in enumerate(items):
            instructions = item.disposal_guide.instructions
            preview = (instructions[:65] + "…") if len(instructions) > 65 else instructions
            tag = "even" if idx % 2 == 0 else "odd"
            self._tree.insert(
                "", tk.END,
                text=item.name,
                values=(item.category.value, preview),
                tags=(tag,),
            )

        if self._status_callback:
            self._status_callback(f"{title}: {len(items)} item(s) found")

    def display_item_details(self, item) -> None:
        """Render the full disposal guide for a single item in the details pane."""
        sep  = "─" * 50
        text = (
            f"{sep}\n"
            f"  {item.name.upper()}\n"
            f"{sep}\n\n"
            f"  Category : {item.category.value}\n\n"
            f"  How to dispose\n"
            f"  {item.disposal_guide.instructions}\n"
        )

        if item.disposal_guide.tips:
            text += "\n  Tips\n"
            for tip in item.disposal_guide.tips:
                text += f"    •  {tip}\n"

        if item.disposal_guide.warnings:
            text += "\n  ⚠  Warnings\n"
            for warning in item.disposal_guide.warnings:
                text += f"    •  {warning}\n"

        self._set_details(text)

    def clear(self) -> None:
        """Clear treeview and details pane."""
        for row in self._tree.get_children():
            self._tree.delete(row)
        self._details_text.delete("1.0", tk.END)
        self._current_items = []

    # ── Internal helper ──────────────────────────────────────────────────────
    def _set_details(self, text: str) -> None:
        self._details_text.delete("1.0", tk.END)
        self._details_text.insert("1.0", text)
