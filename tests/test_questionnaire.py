import pytest

from cockpit_eleve import CONFIG_DIR
from cockpit_eleve.models import Question
from cockpit_eleve.questionnaire import (
    MAX_QUESTIONS,
    QuestionnaireEngine,
    TooManyQuestionsError,
    load_questions,
)


def test_questionnaire_config_within_limit():
    questions = load_questions(CONFIG_DIR / "questionnaire.json")
    assert len(questions) <= MAX_QUESTIONS


def test_questionnaire_accepts_exactly_15_questions():
    questions = [
        Question(id=f"FICTIF_Q{i}", label=f"FICTIF question {i}") for i in range(15)
    ]
    engine = QuestionnaireEngine(questions)
    assert len(engine.questions) == MAX_QUESTIONS


def test_questionnaire_rejects_more_than_15_questions():
    questions = [
        Question(id=f"FICTIF_Q{i}", label=f"FICTIF question {i}") for i in range(16)
    ]
    with pytest.raises(TooManyQuestionsError):
        QuestionnaireEngine(questions)


def test_engine_collects_answers_and_builds_profile():
    questions = load_questions(CONFIG_DIR / "questionnaire.json")
    engine = QuestionnaireEngine(questions)
    for question in questions:
        engine.answer(question.id, f"réponse FICTIVE pour {question.id}")
    profile = engine.build_profile("  John Doe  ")
    assert profile.child_name == "John Doe"
    assert len(profile.answers) == len(questions)


def test_engine_rejects_unknown_question():
    questions = load_questions(CONFIG_DIR / "questionnaire.json")
    engine = QuestionnaireEngine(questions)
    with pytest.raises(ValueError):
        engine.answer("question_inconnue", "x")
