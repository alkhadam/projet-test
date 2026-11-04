import pytest

from hello import farewell, greet


def test_greet_returns_message():
    assert greet("Alice") == "Bonjour, Alice !"


def test_greet_strips_whitespace():
    assert greet("  Bob ") == "Bonjour, Bob !"


def test_greet_rejects_empty_name():
    with pytest.raises(ValueError):
        greet("   ")


def test_farewell_returns_message():
    assert farewell("Alice") == "Au revoir, Alice !"


def test_farewell_strips_whitespace():
    assert farewell("  Bob ") == "Au revoir, Bob !"


def test_farewell_rejects_empty_name():
    with pytest.raises(ValueError):
        farewell("   ")
