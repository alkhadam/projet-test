"""Modèle de profil enfant."""

from dataclasses import dataclass


@dataclass(frozen=True)
class ChildProfile:
    """Profil d'un enfant renseigné par son parent."""

    name: str
    age: str
    needs: tuple[str, ...]
    difficulties: tuple[str, ...]


def demo_profile() -> ChildProfile:
    """Retourne le profil de démonstration John Doe."""
    return ChildProfile(
        name="John Doe",
        age="8",
        needs=("organisation", "concentration", "lecture"),
        difficulties=("routine du matin", "devoirs à la maison", "écriture"),
    )
