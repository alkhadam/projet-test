"""Génération du site dédié standalone (HTML statique, sans dépendance)."""

import html
import time
from pathlib import Path

from cockpit.profile import ChildProfile
from cockpit.roadmap import Milestone, build_roadmap


def render_roadmap_items(milestones: tuple[Milestone, ...]) -> str:
    """Retourne le HTML des jalons de la feuille de route."""
    parts: list[str] = []
    for milestone in milestones:
        items = "".join(
            f"<li>{html.escape(action)}</li>" for action in milestone.actions
        )
        parts.append(
            "<section>"
            f"<h3>{html.escape(milestone.title)}</h3>"
            f"<ul>{items}</ul>"
            "</section>"
        )
    return "".join(parts)


def render_site(profile: ChildProfile, milestones: tuple[Milestone, ...]) -> str:
    """Retourne le HTML standalone complet du site dédié."""
    name = html.escape(profile.name)
    age = html.escape(profile.age)
    needs = ", ".join(profile.needs) if profile.needs else "à préciser"
    difficulties = (
        ", ".join(profile.difficulties) if profile.difficulties else "à préciser"
    )
    roadmap = render_roadmap_items(milestones)
    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Espace dédié de {name}</title>
<style>
body {{ font-family: system-ui, sans-serif; max-width: 48rem; margin: 2rem auto; }}
section {{ border: 1px solid #ddd; border-radius: 8px; padding: 1rem; margin: 1rem 0; }}
h3 {{ margin-top: 0; }}
</style>
</head>
<body>
<header><h1>Espace de {name}</h1><p>Âge : {age} ans</p></header>
<main>
<h2>Points d'appui</h2><p>{html.escape(needs)}</p>
<h2>Situations du quotidien</h2><p>{html.escape(difficulties)}</p>
<h2>Feuille de route</h2>
{roadmap}
</main>
<footer><p>Cet espace propose des repères pratiques et des actions concrètes.</p></footer>
</body>
</html>
"""


def generate_site(profile: ChildProfile, output_dir: str | Path) -> tuple[Path, float]:
    """Génère le site et l'écrit sur disque ; retourne (chemin, durée en secondes)."""
    start = time.monotonic()
    milestones = build_roadmap(profile)
    content = render_site(profile, milestones)
    directory = Path(output_dir)
    directory.mkdir(parents=True, exist_ok=True)
    output_path = directory / "index.html"
    output_path.write_text(content, encoding="utf-8")
    duration = time.monotonic() - start
    return output_path, duration
