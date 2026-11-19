"""Chargement de la configuration de domaine depuis des fichiers JSON."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


class ConfigError(Exception):
    """Erreur de chargement ou de validation d'un fichier de configuration."""


def load_json(path: Path) -> dict[str, Any]:
    """Charge un fichier JSON et retourne son contenu décodé."""
    if not path.is_file():
        raise ConfigError(f"fichier de configuration introuvable : {path}")
    try:
        with path.open(encoding="utf-8") as handle:
            data = json.load(handle)
    except json.JSONDecodeError as exc:
        raise ConfigError(f"JSON invalide dans {path} : {exc}") from exc
    if not isinstance(data, dict):
        raise ConfigError(f"configuration attendue sous forme d'objet JSON : {path}")
    return data
