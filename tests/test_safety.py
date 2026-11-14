"""Tests de sécurité des contenus générés (critère 00107720)."""

from cockpit.profile import demo_profile
from cockpit.roadmap import build_roadmap
from cockpit.safety import (
    FORBIDDEN_TERMS,
    ensure_no_forbidden_terms,
    find_forbidden_terms,
)
from cockpit.site import render_site

REQUIRED_TERMS = (
    "tdah",
    "adhd",
    "dyslexie",
    "dyslexia",
    "autisme",
    "autism",
    "diagnostic",
    "diagnose",
)


def test_blocklist_covers_required_terms():
    for term in REQUIRED_TERMS:
        assert term in FORBIDDEN_TERMS


def test_find_forbidden_terms_detects_required_terms():
    for term in REQUIRED_TERMS:
        assert find_forbidden_terms(f"phrase avec {term} dedans") == [term]


def test_generated_site_and_roadmap_have_no_forbidden_terms():
    profile = demo_profile()
    roadmap = build_roadmap(profile)
    site = render_site(profile, roadmap)
    tokens: list[str] = []
    for milestone in roadmap:
        tokens.append(milestone.title)
        tokens.extend(milestone.actions)
    roadmap_text = " ".join(tokens)
    assert find_forbidden_terms(site) == []
    assert find_forbidden_terms(roadmap_text) == []
    ensure_no_forbidden_terms(site)
    ensure_no_forbidden_terms(roadmap_text)
