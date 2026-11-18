from cockpit_eleve import CONFIG_DIR
from cockpit_eleve.content_filter import is_clean, load_forbidden_terms
from cockpit_eleve.pipeline import run_pipeline
from cockpit_eleve.questionnaire import load_questions


def test_pipeline_end_to_end():
    questions = load_questions(CONFIG_DIR / "questionnaire.json")
    answers = {question.id: "FICTIF" for question in questions}
    site = run_pipeline(CONFIG_DIR, answers=answers)
    assert "<html" in site.html.lower()
    assert "john doe" in site.html.lower()


def test_pipeline_output_has_no_forbidden_terms():
    questions = load_questions(CONFIG_DIR / "questionnaire.json")
    answers = {question.id: "FICTIF" for question in questions}
    site = run_pipeline(CONFIG_DIR, answers=answers)
    terms = load_forbidden_terms(CONFIG_DIR / "forbidden_terms.json")
    assert is_clean(site.html, terms)
