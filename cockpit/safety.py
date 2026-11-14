"""Contrôle des contenus générés : aucun terme médical ou de diagnostic."""

import re

FORBIDDEN_TERMS: tuple[str, ...] = (
    "tdah",
    "adhd",
    "tda",
    "dyslexie",
    "dyslexia",
    "dyslexique",
    "dysorthographie",
    "dyspraxie",
    "dyscalculie",
    "dysgraphie",
    "autisme",
    "autism",
    "autiste",
    "diagnostic",
    "diagnose",
    "diagnostique",
    "diagnosis",
    "diagnostiquer",
    "trouble",
    "syndrome",
    "handicap",
    "pathologie",
    "pathologique",
    "maladie",
    "deficit",
    "déficit",
    "deficience",
    "déficience",
)


def find_forbidden_terms(text: str) -> list[str]:
    """Retourne les termes interdits présents dans text (insensible à la casse)."""
    normalized = text.lower()
    found: list[str] = []
    for term in FORBIDDEN_TERMS:
        pattern = rf"\b{re.escape(term)}\b"
        if re.search(pattern, normalized):
            found.append(term)
    return found


def ensure_no_forbidden_terms(text: str) -> None:
    """Lève ValueError si text contient un terme interdit."""
    found = find_forbidden_terms(text)
    if found:
        raise ValueError("termes interdits détectés : " + ", ".join(found))
