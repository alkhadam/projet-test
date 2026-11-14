"""Tests de génération du site (critère 8c6b7f37)."""

from cockpit.profile import demo_profile
from cockpit.roadmap import build_roadmap
from cockpit.site import generate_site, render_site


def test_site_generated_within_time_limit(tmp_path):
    output_path, duration = generate_site(demo_profile(), tmp_path)
    assert output_path.exists()
    assert output_path.is_file()
    assert output_path.read_text(encoding="utf-8").startswith("<!doctype html>")
    assert duration < 300


def test_site_is_standalone_html_containing_roadmap():
    profile = demo_profile()
    site = render_site(profile, build_roadmap(profile))
    assert "<!doctype html>" in site
    assert "Feuille de route" in site
    assert profile.name in site
