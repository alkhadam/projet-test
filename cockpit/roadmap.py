"""Feuille de route générée à partir du profil, sans diagnostic."""

from dataclasses import dataclass

from cockpit.profile import ChildProfile


@dataclass(frozen=True)
class Milestone:
    """Un jalon de la feuille de route, avec des actions concrètes."""

    title: str
    actions: tuple[str, ...]


_MILESTONES_BY_NEED: dict[str, Milestone] = {
    "organisation": Milestone(
        "Mettre en place une routine quotidienne claire",
        (
            "Établir un planning visuel de la journée avec des images",
            "Fixer des horaires réguliers pour le lever, les repas et le coucher",
            "Préparer les affaires la veille au soir",
        ),
    ),
    "concentration": Milestone(
        "Aménager un espace de travail calme et adapté",
        (
            "Choisir un endroit calme et bien éclairé pour les devoirs",
            "Réduire les distractions (écrans, bruit) pendant le travail",
            "Prévoir des pauses courtes toutes les vingt minutes",
        ),
    ),
    "lecture": Milestone(
        "Soutenir la lecture au quotidien",
        (
            "Lire ensemble dix minutes chaque soir",
            "Proposer des livres courts et illustrés",
            "Encourager la lecture à voix haute",
        ),
    ),
    "écriture": Milestone(
        "Soutenir l'écriture au quotidien",
        (
            "Utiliser des supports grands et espacés pour écrire",
            "S'entraîner avec des activités courtes et régulières",
            "Encourager la relecture à voix haute",
        ),
    ),
    "autonomie": Milestone(
        "Renforcer l'autonomie pas à pas",
        (
            "Confier une petite responsabilité chaque semaine",
            "Découper les consignes en étapes simples",
            "Valoriser chaque progrès avec un compliment précis",
        ),
    ),
    "émotions": Milestone(
        "Créer des temps d'échange et de détente",
        (
            "Instaurer un moment d'échange quotidien sans écran",
            "Proposer des activités calmes (dessin, construction, musique)",
            "Nommer les émotions avec des mots simples",
        ),
    ),
}

_FALLBACK_MILESTONES: tuple[Milestone, ...] = (
    _MILESTONES_BY_NEED["organisation"],
    _MILESTONES_BY_NEED["concentration"],
    _MILESTONES_BY_NEED["autonomie"],
)


def build_roadmap(profile: ChildProfile) -> tuple[Milestone, ...]:
    """Construit une feuille de route d'au moins trois jalons pour le profil."""
    selected: list[Milestone] = []
    for need in profile.needs:
        milestone = _MILESTONES_BY_NEED.get(need)
        if milestone is not None and milestone not in selected:
            selected.append(milestone)
    for milestone in _FALLBACK_MILESTONES:
        if len(selected) >= 3:
            break
        if milestone not in selected:
            selected.append(milestone)
    return tuple(selected)
