"""Parcours minimal de bout en bout (étapes 1 à 3 de la spécification)."""

from __future__ import annotations

from pathlib import Path

from cockpit_eleve.content_filter import load_forbidden_terms
from cockpit_eleve.models import Site
from cockpit_eleve.questionnaire import QuestionnaireEngine, load_questions
from cockpit_eleve.roadmap import generate_roadmap, load_milestones
from cockpit_eleve.site_generator import generate_site

# Persona de démonstration fourni par la spécification (éléments 8ce11298 / 2fb1c69d).
# Donnée FICTIVE, jamais destinée à un utilisateur réel.
DEMO_CHILD_NAME = "John Doe"


def run_pipeline(
    config_dir: Path,
    answers: dict[str, str] | None = None,
    child_name: str = DEMO_CHILD_NAME,
) -> Site:
    """Exécute le parcours complet : questionnaire -> profil -> roadmap -> site."""
    answers = answers or {}

    questions = load_questions(config_dir / "questionnaire.json")
    engine = QuestionnaireEngine(questions)
    for question_id, value in answers.items():
        engine.answer(question_id, value)
    profile = engine.build_profile(child_name)

    milestones = load_milestones(config_dir / "roadmap.json")
    roadmap = generate_roadmap(profile, milestones)

    forbidden_terms = load_forbidden_terms(config_dir / "forbidden_terms.json")
    return generate_site(profile, roadmap, forbidden_terms)
