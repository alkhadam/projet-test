"""Questionnaire profil enfant (P1), limité à 15 questions."""

from dataclasses import dataclass

from cockpit.profile import ChildProfile

MAX_QUESTIONS = 15

_NEED_KEYS = {
    "S'organiser au quotidien": "organisation",
    "Rester concentré": "concentration",
    "Progresser en lecture": "lecture",
    "Progresser en écriture": "écriture",
    "Gagner en autonomie": "autonomie",
    "Gérer ses émotions": "émotions",
}


@dataclass(frozen=True)
class Question:
    """Une question du questionnaire, avec ses options de réponse."""

    key: str
    text: str
    options: tuple[str, ...] = ()


QUESTIONS: tuple[Question, ...] = (
    Question("name", "Quel est le prénom de l'enfant ?"),
    Question("age", "Quel est l'âge de l'enfant ?"),
    Question(
        "main_need",
        "Quel besoin d'accompagnement est le plus important ?",
        (
            "S'organiser au quotidien",
            "Rester concentré",
            "Progresser en lecture",
            "Progresser en écriture",
            "Gagner en autonomie",
            "Gérer ses émotions",
        ),
    ),
    Question(
        "daily_difficulty",
        "Quelle situation revient le plus souvent au quotidien ?",
        (
            "La routine du matin",
            "Les devoirs à la maison",
            "La lecture",
            "L'écriture",
            "Les transitions entre activités",
            "L'expression des émotions",
        ),
    ),
    Question(
        "homework",
        "Comment se passent les devoirs à la maison ?",
        ("Plutôt facilement", "Avec de l'aide régulière", "C'est souvent compliqué"),
    ),
    Question(
        "morning_routine",
        "La routine du matin est-elle facile à suivre ?",
        ("Oui, sans difficulté", "Parfois", "Souvent difficile"),
    ),
    Question(
        "reading",
        "L'enfant lit-il volontiers seul ?",
        ("Oui, souvent", "Parfois", "Rarement"),
    ),
    Question(
        "writing",
        "L'écriture est-elle fluide au quotidien ?",
        ("Oui", "Moyennement", "Non"),
    ),
    Question(
        "attention",
        "L'enfant reste-t-il concentré sur une activité ?",
        ("Oui, longtemps", "Quelques minutes", "Difficilement"),
    ),
    Question(
        "emotions",
        "L'enfant exprime-t-il facilement ce qu'il ressent ?",
        ("Oui, avec des mots", "Parfois", "Difficilement"),
    ),
    Question(
        "autonomy",
        "L'enfant fait-il certaines choses seul ?",
        ("Oui, beaucoup", "Quelques-unes", "Très peu"),
    ),
    Question(
        "favorite_activities",
        "Quelles activités plaisent le plus à l'enfant ?",
        ("Dessiner", "Construire", "Écouter des histoires", "Bouger et jouer dehors"),
    ),
)


def question_count() -> int:
    """Retourne le nombre de questions du questionnaire."""
    return len(QUESTIONS)


def create_profile(answers: dict[str, str]) -> ChildProfile:
    """Construit un profil enfant à partir des réponses du parent."""
    name = (answers.get("name") or "").strip()
    age = (answers.get("age") or "").strip()
    need_key = _NEED_KEYS.get(answers.get("main_need") or "")
    needs = (need_key,) if need_key else ()
    difficulty = (answers.get("daily_difficulty") or "").strip()
    difficulties = (difficulty,) if difficulty else ()
    return ChildProfile(name=name, age=age, needs=needs, difficulties=difficulties)
