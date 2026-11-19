"""Générateur de roadmap : contenant, jalons chargés depuis la configuration."""

from __future__ import annotations

from pathlib import Path

from cockpit_eleve.config import load_json
from cockpit_eleve.models import MIN_MILESTONES, Milestone, Profile, Roadmap


class TooFewMilestonesError(ValueError):
    """Levée quand la roadmap contient moins de MIN_MILESTONES jalons."""


def load_milestones(config_path: Path) -> list[Milestone]:
    """Charge les jalons depuis le fichier de configuration."""
    data = load_json(config_path)
    return [
        Milestone(
            id=str(item["id"]),
            title=str(item["title"]),
            actions=[str(action) for action in item.get("actions", [])],
        )
        for item in data.get("milestones", [])
    ]


def generate_roadmap(profile: Profile, milestones: list[Milestone]) -> Roadmap:
    """Génère la roadmap en garantissant au moins MIN_MILESTONES jalons.

    Le paramètre profile documente la personnalisation future ; le choix des
    jalons en fonction du profil est un contenu de domaine non décidé (A_DEFINIR).
    """
    _ = profile  # pilotera la personnalisation quand le contenu sera décidé
    if len(milestones) < MIN_MILESTONES:
        raise TooFewMilestonesError(
            f"la roadmap contient {len(milestones)} jalons "
            f"(minimum requis : {MIN_MILESTONES})"
        )
    return Roadmap(milestones=list(milestones))
