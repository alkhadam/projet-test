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

## Cockpit de l'élève (M-001)

Parcours P1 : un parent remplit un questionnaire profil enfant (12 questions,
maximum 15), le profil est enregistré, puis un site dédié standalone (HTML
statique) est généré automatiquement avec une feuille de route d'au moins
3 jalons, chacun avec des actions concrètes.

- cockpit/questionnaire.py : questionnaire et profil enfant.
- cockpit/roadmap.py : feuille de route (jalons + actions concrètes).
- cockpit/site.py : génération du site HTML standalone.
- cockpit/safety.py : blocklist des termes médicaux ou de diagnostic.

Démo (génère le site John Doe dans site-demo/) :

    python -m cockpit.demo
