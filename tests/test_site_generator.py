import time

import pytest

from cockpit_eleve import CONFIG_DIR
from cockpit_eleve.content_filter import is_clean, load_forbidden_terms
from cockpit_eleve.models import Milestone, Profile, Roadmap
from cockpit_eleve.roadmap import generate_roadmap, load_milestones
from cockpit_eleve.site_generator import ForbiddenContentError, generate_site


def _build_roadmap() -> Roadmap:
    milestones = load_milestones(CONFIG_DIR / "roadmap.json")
    return generate_roadmap(Profile(child_name="John Doe"), milestones)


def test_site_contains_roadmap_milestones():
    roadmap = _build_roadmap()
    terms = load_forbidden_terms(CONFIG_DIR / "forbidden_terms.json")
    site = generate_site(Profile(child_name="John Doe"), roadmap, terms)
    for milestone in roadmap.milestones:
        assert milestone.title in site.html


def test_site_has_no_forbidden_terms():
    roadmap = _build_roadmap()
    terms = load_forbidden_terms(CONFIG_DIR / "forbidden_terms.json")
    site = generate_site(Profile(child_name="John Doe"), roadmap, terms)
    assert is_clean(site.html, terms)


def test_site_generation_under_5_minutes():
    terms = load_forbidden_terms(CONFIG_DIR / "forbidden_terms.json")
    start = time.monotonic()
    generate_site(Profile(child_name="John Doe"), _build_roadmap(), terms)
    elapsed = time.monotonic() - start
    assert elapsed < 300


def test_site_refuses_forbidden_content():
    milestones = [
        Milestone(id="FICTIF_1", title="TDAH", actions=["FICTIF"]),
        Milestone(id="FICTIF_2", title="FICTIF", actions=["FICTIF"]),
        Milestone(id="FICTIF_3", title="FICTIF", actions=["FICTIF"]),
    ]
    roadmap = Roadmap(milestones=milestones)
    terms = load_forbidden_terms(CONFIG_DIR / "forbidden_terms.json")
    with pytest.raises(ForbiddenContentError):
        generate_site(Profile(child_name="John Doe"), roadmap, terms)
