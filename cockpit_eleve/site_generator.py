"""Génération du site dédié standalone (contenant, HTML statique)."""

from __future__ import annotations

import html

from cockpit_eleve.content_filter import find_forbidden_terms
from cockpit_eleve.models import Profile, Roadmap, Site


class ForbiddenContentError(ValueError):
    """Levée quand le contenu généré contient un terme interdit."""


def generate_site(profile: Profile, roadmap: Roadmap, forbidden_terms: list[str]) -> Site:
    """Génère le site dédié et refuse tout terme interdit (critère 00107720)."""
    title = f"Site dédié — {html.escape(profile.child_name)}"
    body = _render_roadmap(roadmap)
    document = (
        "<!doctype html>\n"
        '<html lang="fr">\n'
        '<head><meta charset="utf-8"><title>'
        f"{title}</title></head>\n"
        f"<body><h1>{title}</h1>\n{body}</body>\n</html>\n"
    )
    forbidden = find_forbidden_terms(document, forbidden_terms)
    if forbidden:
        raise ForbiddenContentError(
            f"contenu généré avec termes interdits : {', '.join(forbidden)}"
        )
    return Site(html=document)


def _render_roadmap(roadmap: Roadmap) -> str:
    """Rend les jalons de la roadmap dans le document HTML."""
    sections = []
    for milestone in roadmap.milestones:
        actions = "".join(
            f"<li>{html.escape(action)}</li>" for action in milestone.actions
        )
        sections.append(
            "<section>"
            f"<h2>{html.escape(milestone.title)}</h2>"
            f"<ul>{actions}</ul>"
            "</section>"
        )
    return "\n".join(sections)
