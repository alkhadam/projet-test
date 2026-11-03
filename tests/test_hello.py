import pytest

from hello import greet


def test_greet_returns_message():
    assert greet("Alice") == "Bonjour, Alice !"


def test_greet_strips_whitespace():
    assert greet("  Bob ") == "Bonjour, Bob !"


def test_greet_rejects_empty_name():
    with pytest.raises(ValueError):
        greet("   ")
