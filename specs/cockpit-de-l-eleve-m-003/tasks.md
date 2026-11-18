# Tâches cockpit-de-l-eleve-m-003

## Découpage
1. Réaliser le périmètre de la spécification en **une seule PR**.
2. Tests automatisés couvrant chaque critère d’acceptation quand c’est possible.

## Règles
- Le besoin et le périmètre sont ceux de spec.md, au commit figé. Ne pas les étendre.
- S’arrêter et demander l’accord de l’opérateur avant : Modifier le besoin ou le périmètre validé ; Déployer en production ; Suppression irréversible ; Dépasser le budget fixé. Budget indicatif : 5 $.
- Aucun push sur main, aucune fusion, aucun déploiement.

## Règle de contenu (contrat d'exécution)
Tu ne crées **aucun contenu de domaine** (catégorie, question posée, libellé, seuil, recommandation, conseil) qui ne soit pas dans la spécification avec un **identifiant d'élément décidé** (voir `decisions.json`).
Si tu en as besoin pour avancer : place un **emplacement** nommé `A_DEFINIR_<SUJET>`, charge-le depuis un **fichier de configuration** (jamais écrit en dur dans le code), et liste-le dans la PR sous « Questions ouvertes ».
Dans le rapport, déclare **chaque constante de domaine** présente dans ta PR avec la référence de l'élément décidé qui la justifie, ou avec le nom de son emplacement. Une constante sans référence est un écart.
Inventer est interdit. T'arrêter et poser la question est autorisé.

## Domaine sensible : tu construis le contenant, jamais le contenu
Ce projet touche des mineurs, la santé ou le droit. Aucun contenu inventé ne doit atteindre un utilisateur réel, même étiqueté provisoire.
- Tu peux livrer : le moteur (par exemple un moteur de questionnaire), des catégories **chargées depuis un fichier de configuration**, des emplacements `A_DEFINIR_…`, un écran avec gabarit vide, des données fictives marquées `FICTIF` dans un environnement non exposé.
- Tu ne livres pas : les catégories ou les seuils eux-mêmes, des valeurs « plausibles » pour un emplacement, des formulations de conseil destinées aux parents ou aux personnes concernées, ni aucune mise en ligne accessible à de vrais utilisateurs.
- Tant qu'un emplacement reste ouvert, la livraison à de vrais utilisateurs est refusée.

## Rapport obligatoire
La description de la PR contient « Mission cockpit-de-l-eleve-m-003 » et « Suivi : #8 », puis ce bloc, complété :

```cockpit-rapport
{"mission": "cockpit-de-l-eleve-m-003", "statut": "termine", "resume": "ce qui a été fait",
 "criteres": [{"id": "8c6b7f37", "statut": "conforme | non_conforme | non_verifie", "preuve": "test ou fichier"}, {"id": "5d04a7da", "statut": "conforme | non_conforme | non_verifie", "preuve": "test ou fichier"}, {"id": "00107720", "statut": "conforme | non_conforme | non_verifie", "preuve": "test ou fichier"}, {"id": "6f7b35fa", "statut": "conforme | non_conforme | non_verifie", "preuve": "test ou fichier"}],
 "constantes_domaine": [{"libelle": "catégorie, question, seuil… présent dans ta PR", "ref": "<identifiant d'un élément décidé, ou A_DEFINIR_…>"}],
 "questions_ouvertes": ["ce qui manquait et que tu n'as pas inventé"],
 "hypotheses_infirmees": []}
```
Le champ « constantes_domaine » est obligatoire (liste vide si ta PR n'en contient aucune).

Pour une demande d’accord ou un blocage : "statut": "demande_accord" (avec "demande": {"type": "perimetre | production | suppression | budget", "justification": "…"}) ou "bloque", et le CTO le rapporte en fin de mission.
