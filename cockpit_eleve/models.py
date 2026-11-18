"""Gabarits de données du cockpit. Aucun contenu de domaine n'est codé en dur."""

from __future__ import annotations

from dataclasses import dataclass, field

# Critère d'acceptation 6f7b35fa : au maximum 15 questions.
MAX_QUESTIONS = 15

# Critère d'acceptation 5d04a7da : au moins 3 jalons dans la roadmap.
MIN_MILESTONES = 3


@dataclass
class Question:
    """Une question du questionnaire (libellé fourni par la configuration)."""

    id: str
    label: str
    type: str = "text"


@dataclass
class Profile:
    """Profil de l'enfant : identité et réponses collectées."""

    child_name: str
    answers: dict[str, str] = field(default_factory=dict)


@dataclass
class Milestone:
    """Un jalon de la roadmap (titre et actions fournis par la configuration)."""

    id: str
    title: str
    actions: list[str] = field(default_factory=list)


@dataclass
class Roadmap:
    """Roadmap d'accompagnement personnalisée."""

    milestones: list[Milestone]


@dataclass
class Site:
    """Site dédié généré (document HTML standalone)."""

    html: str
