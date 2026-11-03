import pytest

from hello import greet


def test_greet_returns_message():
    assert greet("Alice") == "Bonjour, Alice !"


def test_greet_strips_whitespace():
    assert greet("  Bob ") == "Bonjour, Bob !"


def test_greet_rejects_empty_name():
    with pytest.raises(ValueError):
        greet("   ")


def test_farewell_nominal():
    from hello import farewell

    assert farewell("Alice") == "Au revoir, Alice !"


def test_farewell_strips_spaces():
    from hello import farewell

    assert farewell("  Alice  ") == "Au revoir, Alice !"


def test_farewell_empty_raises():
    import pytest

    from hello import farewell

    for value in ("", "   "):
        with pytest.raises(ValueError):
            farewell(value)
