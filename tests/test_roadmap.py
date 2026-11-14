"""Tests de la feuille de route (critère 5d04a7da)."""

from cockpit.profile import ChildProfile, demo_profile
from cockpit.roadmap import build_roadmap


def test_roadmap_has_at_least_three_milestones():
    roadmap = build_roadmap(demo_profile())
    assert len(roadmap) >= 3


def test_each_milestone_has_concrete_non_empty_actions():
    roadmap = build_roadmap(demo_profile())
    for milestone in roadmap:
        assert milestone.title.strip()
        assert len(milestone.actions) >= 2
        for action in milestone.actions:
            assert action.strip()


def test_roadmap_fallback_for_empty_needs():
    profile = ChildProfile(name="Jane", age="7", needs=(), difficulties=())
    roadmap = build_roadmap(profile)
    assert len(roadmap) >= 3
