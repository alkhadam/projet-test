from cockpit_eleve import CONFIG_DIR
from cockpit_eleve.content_filter import (
    find_forbidden_terms,
    is_clean,
    load_forbidden_terms,
)


def test_forbidden_terms_loaded():
    terms = load_forbidden_terms(CONFIG_DIR / "forbidden_terms.json")
    assert terms


def test_detects_forbidden_terms_case_insensitive():
    terms = load_forbidden_terms(CONFIG_DIR / "forbidden_terms.json")
    assert find_forbidden_terms("Mon enfant a un TDAH.", terms) == ["tdah"]


def test_clean_text_has_no_forbidden_terms():
    terms = load_forbidden_terms(CONFIG_DIR / "forbidden_terms.json")
    assert is_clean("jalon d'accompagnement sans contenu diagnostique", terms)
