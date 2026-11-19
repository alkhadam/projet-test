# projet-test

Projet d'essai pour valider la chaîne de l'agence : développement, tests, revue sécurité, pull request.

## Utilisation

```bash
python -m venv .venv
source .venv/bin/activate        # Windows : .venv\Scripts\activate
pip install -r requirements-dev.txt
pytest
```

## Contenu

- `hello.py` : fonctions `greet(name)` (bonjour) et `farewell(name)` (au revoir). Les deux retirent les espaces autour du nom et lèvent `ValueError` si le nom est vide.
- `tests/` : tests `pytest`.
- `.github/workflows/ci.yml` : lint (ruff), analyse de sécurité (bandit) et tests à chaque pull request.

## Règles

- Aucun secret dans le dépôt (voir `.gitignore`). Les clés passent par des variables d'environnement.
- Le développement se fait sur une branche dédiée, jamais directement sur `main`.
- Toute fusion dans `main` passe par une pull request approuvée par un humain.

## Cockpit de l'élève — mission M-003

Parcours P1 (contenant uniquement, aucun contenu de domaine codé en dur) :

- cockpit_eleve/ : moteurs (questionnaire, roadmap, filtre de termes interdits, génération de site, pipeline).
- cockpit_eleve/config/ : contenu de domaine chargé depuis des fichiers JSON.
  - questionnaire.json : questions (emplacements A_DEFINIR_QUESTION_*).
  - roadmap.json : jalons (emplacements A_DEFINIR_MILESTONE_* et A_DEFINIR_ACTION_*).
  - forbidden_terms.json : termes interdits (référence 00107720).
- tests/ : tests couvrant les critères d'acceptation (8c6b7f37, 5d04a7da, 00107720, 6f7b35fa).

Exécution du parcours :

    .venv/bin/python -c "from cockpit_eleve import CONFIG_DIR; from cockpit_eleve.pipeline import run_pipeline; print(run_pipeline(CONFIG_DIR).html)"

Le contenu de domaine (questions, jalons, actions) est volontairement laissé en
emplacements A_DEFINIR_* : il sera renseigné par des professionnels, hors du
périmètre de cette mission (domaine sensible, mineurs/santé).
