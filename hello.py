"""Module d'exemple pour le projet de test."""


def greet(name: str) -> str:
    """Retourne un message de bienvenue pour `name`."""
    name = name.strip()
    if not name:
        raise ValueError("name must not be empty")
    return f"Bonjour, {name} !"


def farewell(name: str) -> str:
    """Retourne un message d'au revoir pour `name`."""
    name = name.strip()
    if not name:
        raise ValueError("name must not be empty")
    return f"Au revoir, {name} !"


if __name__ == "__main__":
    print(greet("monde"))
