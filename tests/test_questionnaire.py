"""Tests du questionnaire profil enfant (critère 6f7b35fa)."""

from cockpit.questionnaire import (
    MAX_QUESTIONS,
    QUESTIONS,
    create_profile,
    question_count,
)


def test_questionnaire_has_at_most_fifteen_questions():
    assert question_count() <= MAX_QUESTIONS
    assert len(QUESTIONS) <= 15


def test_create_profile_records_name_and_age():
    answers = {
        "name": "John Doe",
        "age": "8",
        "main_need": "Progresser en lecture",
        "daily_difficulty": "La lecture",
    }
    profile = create_profile(answers)
    assert profile.name == "John Doe"
    assert profile.age == "8"
    assert profile.needs
    assert profile.difficulties
