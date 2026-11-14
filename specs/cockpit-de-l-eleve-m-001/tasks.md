# Tâches cockpit-de-l-eleve-m-001

## Découpage
1. Réaliser le périmètre de la spécification en **une seule PR**.
2. Tests automatisés couvrant chaque critère d’acceptation quand c’est possible.

## Règles
- Le besoin et le périmètre sont ceux de spec.md, au commit figé. Ne pas les étendre.
- S’arrêter et demander l’accord de l’opérateur avant : Modifier le besoin ou le périmètre validé ; Déployer en production ; Suppression irréversible ; Dépasser le budget fixé. Budget indicatif : 5 $.
- Aucun push sur main, aucune fusion, aucun déploiement.

## Rapport obligatoire
La description de la PR contient « Mission cockpit-de-l-eleve-m-001 » et « Suivi : #4 », puis ce bloc, complété :

```cockpit-rapport
{"mission": "cockpit-de-l-eleve-m-001", "statut": "termine", "resume": "ce qui a été fait",
 "criteres": [{"id": "8c6b7f37", "statut": "conforme | non_conforme | non_verifie", "preuve": "test ou fichier"}, {"id": "5d04a7da", "statut": "conforme | non_conforme | non_verifie", "preuve": "test ou fichier"}, {"id": "00107720", "statut": "conforme | non_conforme | non_verifie", "preuve": "test ou fichier"}, {"id": "6f7b35fa", "statut": "conforme | non_conforme | non_verifie", "preuve": "test ou fichier"}],
 "hypotheses_infirmees": []}
```

Pour une demande d’accord ou un blocage : "statut": "demande_accord" (avec "demande": {"type": "perimetre | production | suppression | budget", "justification": "…"}) ou "bloque", et le CTO le rapporte en fin de mission.
