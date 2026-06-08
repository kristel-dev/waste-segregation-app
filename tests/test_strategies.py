"""Unit Tests for Strategies."""

import pytest
from strategies.input.console_input import ConsoleInput
from strategies.output.screen_display import ScreenDisplay


class TestConsoleInput:
    def test_get_user_input(self, monkeypatch):
        monkeypatch.setattr("builtins.input", lambda x: "test")
        strategy = ConsoleInput()
        result = strategy.get_user_input("Enter: ")
        assert result == "test"


class TestScreenDisplay:
    def test_display(self, capsys):
        strategy = ScreenDisplay()
        strategy.display("Hello")
        captured = capsys.readouterr()
        assert "Hello" in captured.out