"""Moteur de questionnaire : contenant, contenu chargé depuis la configuration."""

from __future__ import annotations

from pathlib import Path

from cockpit_eleve.config import load_json
from cockpit_eleve.models import MAX_QUESTIONS, Profile, Question


class TooManyQuestionsError(ValueError):
    """Levée quand le questionnaire dépasse le nombre maximal de questions."""


def load_questions(config_path: Path) -> list[Question]:
    """Charge les questions depuis le fichier de configuration et les valide."""
    data = load_json(config_path)
    questions = [
        Question(
            id=str(item["id"]),
            label=str(item["label"]),
            type=str(item.get("type", "text")),
        )
        for item in data.get("questions", [])
    ]
    validate_questionnaire(questions)
    return questions


def validate_questionnaire(questions: list[Question]) -> None:
    """Garantit le critère 6f7b35fa : au plus MAX_QUESTIONS questions."""
    if len(questions) > MAX_QUESTIONS:
        raise TooManyQuestionsError(
            f"le questionnaire contient {len(questions)} questions "
            f"(maximum autorisé : {MAX_QUESTIONS})"
        )


class QuestionnaireEngine:
    """Collecte les réponses d'un questionnaire sans en détenir le contenu."""

    def __init__(self, questions: list[Question]) -> None:
        validate_questionnaire(questions)
        self.questions = questions
        self._answers: dict[str, str] = {}

    def answer(self, question_id: str, value: str) -> None:
        """Enregistre la réponse à une question existante."""
        if question_id not in {question.id for question in self.questions}:
            raise ValueError(f"question inconnue : {question_id}")
        self._answers[question_id] = value

    def build_profile(self, child_name: str) -> Profile:
        """Construit le profil à partir des réponses collectées."""
        return Profile(child_name=child_name.strip(), answers=dict(self._answers))
