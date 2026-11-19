"""Filtre des termes interdits : garantit l'absence de contenu diagnostique."""

from __future__ import annotations

from pathlib import Path

from cockpit_eleve.config import load_json


def load_forbidden_terms(config_path: Path) -> list[str]:
    """Charge la liste des termes interdits depuis la configuration."""
    data = load_json(config_path)
    return [str(item["term"]).lower() for item in data.get("terms", [])]


def find_forbidden_terms(text: str, terms: list[str]) -> list[str]:
    """Retourne les termes interdits présents dans text (insensible à la casse)."""
    lowered = text.lower()
    return [term for term in terms if term in lowered]


def is_clean(text: str, terms: list[str]) -> bool:
    """Vrai si text ne contient aucun terme interdit."""
    return not find_forbidden_terms(text, terms)
