import pytest

from cockpit_eleve import CONFIG_DIR
from cockpit_eleve.models import Milestone, Profile
from cockpit_eleve.roadmap import (
    MIN_MILESTONES,
    TooFewMilestonesError,
    generate_roadmap,
    load_milestones,
)


def test_roadmap_has_at_least_3_milestones():
    milestones = load_milestones(CONFIG_DIR / "roadmap.json")
    roadmap = generate_roadmap(Profile(child_name="John Doe"), milestones)
    assert len(roadmap.milestones) >= MIN_MILESTONES


def test_each_milestone_has_actions():
    milestones = load_milestones(CONFIG_DIR / "roadmap.json")
    for milestone in milestones:
        assert milestone.actions, f"jalon {milestone.id} sans action"


def test_roadmap_rejects_fewer_than_3_milestones():
    milestones = [Milestone(id="FICTIF_1", title="FICTIF", actions=["FICTIF"])]
    with pytest.raises(TooFewMilestonesError):
        generate_roadmap(Profile(child_name="John Doe"), milestones)
