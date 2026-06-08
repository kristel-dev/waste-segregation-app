"""Waste Segregation App - Clean GUI with green welcoming design + live autocomplete."""

import sys
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

APP_DIR = os.path.join(ROOT, "application")
if APP_DIR not in sys.path:
    sys.path.insert(0, APP_DIR)

import tkinter as tk
from tkinter import ttk, messagebox

from models.waste_category import WasteCategory
from repositories.waste_repository import WasteRepository
from services.waste_service import WasteService
from strategies.input.gui_input import GUIInput
from strategies.output.gui_display import GUIDisplay
from controller import WasteSegregationApp

# ── Colour palette ───────────────────────────────────────────────────────────
BG         = "#f1f8f1"
PANEL_BG   = "#e8f5e9"
HEADER_BG  = "#2e7d32"
HEADER_FG  = "#ffffff"
HEADER_SUB = "#c8e6c9"
BTN_SEARCH = "#43a047"
BTN_BROWSE = "#1e88e5"
BTN_ALL    = "#00897b"
BTN_CLEAR  = "#e53935"
BTN_COPY   = "#546e7a"
FRAME_FG   = "#2e7d32"
STATUS_BG  = "#c8e6c9"
STATUS_FG  = "#1b5e20"
TREE_HDR   = "#388e3c"
TREE_ROW1  = "#f9fbe7"
TREE_ROW2  = "#e8f5e9"
DETAIL_BG  = "#ffffff"

# Autocomplete dropdown colours
AC_BG      = "#ffffff"
AC_FG      = "#1b5e20"
AC_SEL_BG  = "#a5d6a7"
AC_SEL_FG  = "#1b5e20"
AC_BORDER  = "#81c784"


# ── Autocomplete Listbox (floating Toplevel) ─────────────────────────────────
class AutocompleteDropdown:
    """
    A floating Toplevel that displays matching suggestions below the Entry
    widget as the user types.  Keyboard (↑ ↓ Enter Esc Tab) and mouse
    selection both work.
    """

    MAX_VISIBLE = 7   # rows shown before scrolling

    def __init__(self, entry: tk.Entry, string_var: tk.StringVar,
                 all_names: list[str], on_select_cb):
        self._entry       = entry
        self._var         = string_var
        self._all_names   = all_names          # full sorted item name list
        self._on_select   = on_select_cb       # called when user picks a name
        self._popup: tk.Toplevel | None = None
        self._listbox: tk.Listbox | None = None
        self._ignore_trace = False             # guard to stop feedback loops

        # Watch the StringVar for every keystroke
        self._var.trace_add("write", self._on_var_change)

        # Close dropdown on focus-out
        self._entry.bind("<FocusOut>", self._on_focus_out)

    # ── Public ───────────────────────────────────────────────────────────────
    def hide(self):
        if self._popup:
            self._popup.destroy()
            self._popup   = None
            self._listbox = None

    # ── Internal ─────────────────────────────────────────────────────────────
    def _on_var_change(self, *_):
        if self._ignore_trace:
            return
        typed = self._var.get()
        if not typed.strip():
            self.hide()
            return
        matches = [n for n in self._all_names
                   if typed.lower() in n.lower()]
        if matches:
            self._show(matches)
        else:
            self.hide()

    def _show(self, matches: list[str]):
        # Build / rebuild popup
        if self._popup is None:
            self._popup = tk.Toplevel(self._entry.winfo_toplevel())
            self._popup.wm_overrideredirect(True)   # borderless
            self._popup.attributes("-topmost", True)

            frame = tk.Frame(self._popup, bg=AC_BORDER, bd=1)
            frame.pack(fill=tk.BOTH, expand=True)

            sb = tk.Scrollbar(frame, orient=tk.VERTICAL)
            self._listbox = tk.Listbox(
                frame,
                yscrollcommand=sb.set,
                bg=AC_BG, fg=AC_FG,
                selectbackground=AC_SEL_BG,
                selectforeground=AC_SEL_FG,
                font=("Segoe UI", 9),
                relief=tk.FLAT,
                bd=0,
                activestyle="none",
                exportselection=False,
            )
            sb.config(command=self._listbox.yview)
            self._listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            sb.pack(side=tk.RIGHT, fill=tk.Y)

            # Mouse click selects
            self._listbox.bind("<ButtonRelease-1>", self._pick)
            self._listbox.bind("<Double-Button-1>",  self._pick)

            # Keyboard events on the Entry are forwarded here
            self._entry.bind("<Down>",   self._move_down)
            self._entry.bind("<Up>",     self._move_up)
            self._entry.bind("<Return>", self._on_entry_return)
            self._entry.bind("<Tab>",    self._on_tab)
            self._entry.bind("<Escape>", lambda _: self.hide())

        # Populate
        self._listbox.delete(0, tk.END)
        for name in matches:
            self._listbox.insert(tk.END, f"  {name}")

        # Resize height
        visible = min(len(matches), self.MAX_VISIBLE)
        self._listbox.config(height=visible)

        # Position below the Entry
        self._entry.update_idletasks()
        ex = self._entry.winfo_rootx()
        ey = self._entry.winfo_rooty() + self._entry.winfo_height()
        ew = self._entry.winfo_width()
        self._popup.geometry(f"{ew}x{visible * 22 + 4}+{ex}+{ey}")
        self._popup.deiconify()

    # ── Selection helpers ────────────────────────────────────────────────────
    def _pick(self, _event=None):
        if self._listbox is None:
            return
        sel = self._listbox.curselection()
        if not sel:
            return
        name = self._listbox.get(sel[0]).strip()
        self._ignore_trace = True
        self._var.set(name)
        self._ignore_trace = False
        self.hide()
        self._entry.icursor(tk.END)
        self._on_select(name)   # immediately show the item

    def _move_down(self, _event=None):
        if self._listbox is None:
            return "break"
        size = self._listbox.size()
        if size == 0:
            return "break"
        cur = self._listbox.curselection()
        nxt = 0 if not cur else min(cur[0] + 1, size - 1)
        self._listbox.selection_clear(0, tk.END)
        self._listbox.selection_set(nxt)
        self._listbox.see(nxt)
        return "break"

    def _move_up(self, _event=None):
        if self._listbox is None:
            return "break"
        cur = self._listbox.curselection()
        if not cur:
            return "break"
        prv = max(cur[0] - 1, 0)
        self._listbox.selection_clear(0, tk.END)
        self._listbox.selection_set(prv)
        self._listbox.see(prv)
        return "break"

    def _on_entry_return(self, _event=None):
        if self._listbox and self._listbox.curselection():
            self._pick()
            return "break"   # swallow the event so search isn't also triggered
        # Nothing highlighted – let normal search run
        self.hide()
        return None

    def _on_tab(self, _event=None):
        """Tab completes the top/highlighted suggestion."""
        if self._listbox is None:
            return None
        sel = self._listbox.curselection()
        idx = sel[0] if sel else 0
        if self._listbox.size() > 0:
            self._listbox.selection_clear(0, tk.END)
            self._listbox.selection_set(idx)
            self._pick()
            return "break"
        return None

    def _on_focus_out(self, _event=None):
        # Small delay so a click on the listbox registers before hiding
        self._entry.after(150, self.hide)


# ── Main GUI ─────────────────────────────────────────────────────────────────
class WasteSegregationGUI:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("♻ Waste Segregation Guide")
        self.root.configure(bg=BG)
        self.root.resizable(True, True)

        # ── Back-end ─────────────────────────────────────────────────────────
        self.repository = WasteRepository()
        self.service    = WasteService(self.repository)

        self.input_strategy  = GUIInput()
        self.output_strategy = None

        self.controller = WasteSegregationApp(
            self.input_strategy,
            None,
            self.service,
        )

        # Sorted item names for autocomplete
        self._all_names: list[str] = sorted(
            [item.name for item in self.repository.get_all_items()],
            key=str.lower,
        )

        # ── Build UI ─────────────────────────────────────────────────────────
        self._build_ui()
        self._wire_strategies()

        # Attach autocomplete AFTER search_entry and search_var exist
        self._autocomplete = AutocompleteDropdown(
            self.search_entry,
            self.search_var,
            self._all_names,
            on_select_cb=self._autocomplete_selected,
        )

        self._center_window(820, 640)
        self._show_welcome_message()
        self.controller.run()

    # ── Autocomplete callback ────────────────────────────────────────────────
    def _autocomplete_selected(self, name: str):
        """Called when user picks a suggestion – show that item immediately."""
        self.controller._handle_search(name)
        self._update_status(f"  Showing: {name}")

    # ────────────────────────────────────────────────────────────────────────
    def _center_window(self, w: int, h: int):
        self.root.update_idletasks()
        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()
        x  = (sw - w) // 2
        y  = (sh - h) // 2
        self.root.geometry(f"{w}x{h}+{x}+{y}")
        self.root.minsize(700, 560)

    def _wire_strategies(self):
        self.output_strategy = GUIDisplay(
            self.tree,
            self.details_text,
            self._update_status,
        )
        self.controller._output_strategy = self.output_strategy
        self.controller._gui_mode        = True

        self.input_strategy.set_search_variable(self.search_var)
        self.input_strategy.set_category_variable(self.category_var)

    # ── UI construction ──────────────────────────────────────────────────────
    def _build_ui(self):
        self._build_header()
        self._build_body()
        self._build_status_bar()

    def _build_header(self):
        hdr = tk.Frame(self.root, bg=HEADER_BG, height=72)
        hdr.pack(fill=tk.X)
        hdr.pack_propagate(False)

        tk.Label(
            hdr, text="♻  Waste Segregation Guide",
            font=("Segoe UI", 20, "bold"),
            bg=HEADER_BG, fg=HEADER_FG,
        ).pack(pady=(14, 2))

        tk.Label(
            hdr, text="Make the right disposal choice for our environment",
            font=("Segoe UI", 9),
            bg=HEADER_BG, fg=HEADER_SUB,
        ).pack()

    def _build_body(self):
        body = tk.Frame(self.root, bg=BG)
        body.pack(fill=tk.BOTH, expand=True, padx=14, pady=12)
        body.columnconfigure(1, weight=1)
        body.rowconfigure(0, weight=1)

        self._build_left_panel(body)
        self._build_right_panel(body)

    # ── Left panel ──────────────────────────────────────────────────────────
    def _build_left_panel(self, parent):
        left = tk.Frame(parent, bg=PANEL_BG, bd=0)
        left.grid(row=0, column=0, sticky="ns", padx=(0, 12))

        self.search_var   = tk.StringVar()
        self.category_var = tk.StringVar()

        self._build_search_section(left)
        self._build_browse_section(left)
        self._build_action_section(left)

    def _lf(self, parent, title: str) -> tk.LabelFrame:
        return tk.LabelFrame(
            parent, text=title,
            font=("Segoe UI", 10, "bold"),
            bg=PANEL_BG, fg=FRAME_FG,
            padx=8, pady=6,
            relief=tk.GROOVE, bd=1,
        )

    def _btn(self, parent, text: str, cmd, color: str) -> tk.Button:
        return tk.Button(
            parent, text=text, command=cmd,
            bg=color, fg="white",
            font=("Segoe UI", 9, "bold"),
            cursor="hand2",
            relief=tk.FLAT,
            activebackground=color,
            activeforeground="white",
            padx=8, pady=6,
            bd=0,
        )

    def _build_search_section(self, parent):
        sf = self._lf(parent, "🔍  Search Item")
        sf.pack(fill=tk.X, pady=(0, 10))

        tk.Label(
            sf, text="Type to search (suggestions appear automatically):",
            bg=PANEL_BG, fg="#388e3c",
            font=("Segoe UI", 8, "italic"),
            wraplength=190, justify=tk.LEFT,
        ).pack(anchor=tk.W, pady=(0, 2))

        self.search_entry = tk.Entry(
            sf, textvariable=self.search_var,
            font=("Segoe UI", 10), width=22,
            relief=tk.SOLID, bd=1,
        )
        self.search_entry.pack(fill=tk.X, pady=(0, 6))
        # Return key: autocomplete handles it first; falls through to search_item
        self.search_entry.bind("<Return>", lambda _: self.search_item())

        self._btn(sf, "Search", self.search_item, BTN_SEARCH).pack(fill=tk.X)

    def _build_browse_section(self, parent):
        bf = self._lf(parent, "📂  Browse by Category")
        bf.pack(fill=tk.X, pady=(0, 10))

        tk.Label(bf, text="Category:", bg=PANEL_BG,
                 font=("Segoe UI", 9)).pack(anchor=tk.W)

        categories = [cat.value for cat in self.service.get_all_categories()]
        self.category_combo = ttk.Combobox(
            bf, textvariable=self.category_var,
            values=categories, state="readonly",
            font=("Segoe UI", 9), width=21,
        )
        self.category_combo.pack(fill=tk.X, pady=(3, 6))

        self._btn(bf, "Browse", self.browse_category, BTN_BROWSE).pack(fill=tk.X)

    def _build_action_section(self, parent):
        af = self._lf(parent, "⚡  Actions")
        af.pack(fill=tk.X)

        self._btn(af, "📋  View All Items", self.view_all_items, BTN_ALL  ).pack(fill=tk.X, pady=(0, 5))
        self._btn(af, "🗑  Clear Display",  self.clear_display,  BTN_CLEAR).pack(fill=tk.X, pady=(0, 5))
        self._btn(af, "🔄  Refresh",        self.refresh,        "#78909c").pack(fill=tk.X)

    # ── Right panel ─────────────────────────────────────────────────────────
    def _build_right_panel(self, parent):
        right = tk.Frame(parent, bg=BG)
        right.grid(row=0, column=1, sticky="nsew")
        right.rowconfigure(0, weight=3)
        right.rowconfigure(1, weight=2)
        right.columnconfigure(0, weight=1)

        self._build_results_tree(right)
        self._build_details_panel(right)

    def _build_results_tree(self, parent):
        rf = tk.LabelFrame(
            parent, text="📋  Results",
            font=("Segoe UI", 10, "bold"),
            bg=BG, fg=FRAME_FG,
            padx=6, pady=6,
            relief=tk.GROOVE, bd=1,
        )
        rf.grid(row=0, column=0, sticky="nsew", pady=(0, 8))
        rf.rowconfigure(0, weight=1)
        rf.columnconfigure(0, weight=1)

        tree_wrap = tk.Frame(rf, bg=BG)
        tree_wrap.pack(fill=tk.BOTH, expand=True)

        vsb = tk.Scrollbar(tree_wrap, orient=tk.VERTICAL)
        hsb = tk.Scrollbar(tree_wrap, orient=tk.HORIZONTAL)
        vsb.pack(side=tk.RIGHT, fill=tk.Y)
        hsb.pack(side=tk.BOTTOM, fill=tk.X)

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Green.Treeview",
            background=TREE_ROW1, fieldbackground=TREE_ROW1,
            foreground="#1b5e20", rowheight=26, font=("Segoe UI", 9))
        style.configure("Green.Treeview.Heading",
            background=TREE_HDR, foreground="white",
            font=("Segoe UI", 9, "bold"), relief=tk.FLAT)
        style.map("Green.Treeview",
            background=[("selected", "#a5d6a7")],
            foreground=[("selected", "#1b5e20")])

        self.tree = ttk.Treeview(
            tree_wrap,
            columns=("Category", "Instructions"),
            yscrollcommand=vsb.set,
            xscrollcommand=hsb.set,
            selectmode="browse",
            style="Green.Treeview",
        )
        self.tree.pack(fill=tk.BOTH, expand=True)

        vsb.config(command=self.tree.yview)
        hsb.config(command=self.tree.xview)

        self.tree.heading("#0",           text="Item Name",    anchor=tk.W)
        self.tree.heading("Category",     text="Category",     anchor=tk.W)
        self.tree.heading("Instructions", text="Instructions", anchor=tk.W)

        self.tree.column("#0",           width=180, minwidth=130, stretch=True)
        self.tree.column("Category",     width=140, minwidth=110, stretch=False)
        self.tree.column("Instructions", width=320, minwidth=180, stretch=True)

        self.tree.tag_configure("odd",  background=TREE_ROW1)
        self.tree.tag_configure("even", background=TREE_ROW2)

        self.tree.bind("<<TreeviewSelect>>", self._on_item_select)

    def _build_details_panel(self, parent):
        df = tk.LabelFrame(
            parent, text="📄  Disposal Guide Details",
            font=("Segoe UI", 10, "bold"),
            bg=BG, fg=FRAME_FG,
            padx=6, pady=6,
            relief=tk.GROOVE, bd=1,
        )
        df.grid(row=1, column=0, sticky="nsew")
        df.rowconfigure(0, weight=1)
        df.columnconfigure(0, weight=1)

        text_wrap = tk.Frame(df, bg=BG)
        text_wrap.pack(fill=tk.BOTH, expand=True)

        dsb = tk.Scrollbar(text_wrap)
        dsb.pack(side=tk.RIGHT, fill=tk.Y)

        self.details_text = tk.Text(
            text_wrap,
            height=7, wrap=tk.WORD,
            font=("Segoe UI", 9),
            yscrollcommand=dsb.set,
            bg=DETAIL_BG, fg="#1b5e20",
            relief=tk.FLAT, bd=0,
            padx=8, pady=6,
        )
        self.details_text.pack(fill=tk.BOTH, expand=True)
        dsb.config(command=self.details_text.yview)

        self._btn(df, "📋  Copy to Clipboard", self._copy_to_clipboard, BTN_COPY).pack(
            pady=(6, 0), anchor=tk.E,
        )

    def _build_status_bar(self):
        self.status_bar = tk.Label(
            self.root,
            text="  Ready",
            relief=tk.SUNKEN, anchor=tk.W,
            bg=STATUS_BG, fg=STATUS_FG,
            font=("Segoe UI", 8),
            padx=8,
        )
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    # ── Event handlers ───────────────────────────────────────────────────────
    def search_item(self):
        """Triggered by the Search button or Enter key (when no suggestion is active)."""
        query = self.input_strategy.get_search_query()
        if not query:
            messagebox.showwarning("Empty Search", "Please enter an item name to search.")
            return
        self._autocomplete.hide()
        self.controller._handle_search(query)

    def browse_category(self):
        category_name = self.input_strategy.get_selected_category()
        if not category_name:
            messagebox.showwarning("No Category", "Please select a category first.")
            return
        self.controller._handle_browse(category_name)

    def view_all_items(self):
        self.controller._handle_view_all()

    def _on_item_select(self, _event):
        selection = self.tree.selection()
        if not selection:
            return
        item_name = self.tree.item(selection[0])["text"]
        if item_name in ("No items found", ""):
            return
        self.controller.get_item_details(item_name)

    def _copy_to_clipboard(self):
        text = self.details_text.get("1.0", tk.END).strip()
        if text and "No items" not in text:
            self.root.clipboard_clear()
            self.root.clipboard_append(text)
            self._update_status("Copied to clipboard!")
            messagebox.showinfo("Copied", "Disposal guide copied to clipboard.")
        else:
            messagebox.showwarning("Nothing to copy", "Select an item first to see its disposal guide.")

    def clear_display(self):
        if self.output_strategy:
            self.output_strategy.clear()
        self.search_var.set("")
        self.category_var.set("")
        self._autocomplete.hide()
        self._update_status("Display cleared.")
        self.details_text.insert("1.0", "Display cleared.\nUse Search, Browse, or View All Items to show results.")

    def refresh(self):
        if self.search_var.get():
            self.search_item()
        elif self.category_var.get():
            self.browse_category()
        else:
            self.view_all_items()

    def _update_status(self, message: str):
        self.status_bar.config(text=f"  {message}")
        self.root.after(3000, lambda: self.status_bar.config(text="  Ready"))

    def _show_welcome_message(self):
        """Display a welcome prompt in the details pane on first launch."""
        welcome = (
            "Welcome to the Waste Segregation Guide! ♻\n\n"
            "Get started:\n\n"
            "  🔍  Type an item name in the search box — suggestions\n"
            "       will appear as you type.\n\n"
            "  📂  Pick a category from the dropdown and click Browse\n"
            "       to filter items by type.\n\n"
            "  📋  Click  View All Items  to see the full A–Z list.\n\n"
            "──────────────────────────────────────────────────────\n"
            f"  {len(self._all_names)} items available across all categories."
        )
        self.details_text.delete("1.0", tk.END)
        self.details_text.insert("1.0", welcome)


# ── Entry point ──────────────────────────────────────────────────────────────
def main():
    root = tk.Tk()
    WasteSegregationGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
