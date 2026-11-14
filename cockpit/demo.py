"""Démo : génère le site John Doe dans le dossier site-demo."""

from pathlib import Path

from cockpit.profile import demo_profile
from cockpit.site import generate_site


def main() -> None:
    """Génère le site de démonstration John Doe."""
    output_path, duration = generate_site(demo_profile(), Path("site-demo"))
    print(f"Site généré : {output_path} ({duration:.3f} s)")


if __name__ == "__main__":
    main()
