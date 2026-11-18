# Spécification cockpit-de-l-eleve-m-003

> Mission M-003 du projet « COckpit de l'eleve », générée par le cockpit à partir de la version **v1.1** validée par l'opérateur (P1).
> Ce fichier est figé par le commit indiqué dans le commentaire de validation de l’issue.
> Les éléments portent leur identifiant (`xxxxxxxx`) : c’est lui qui sert de référence dans `decisions.json` et dans ton rapport.

> **Domaine sensible** (mineurs, santé ou droit) : tu construis le contenant, jamais le contenu. Voir `tasks.md`.

## Objectif

- `759b3f8e` (P1) Une plateforme d'accompagnement personalisé pour les enfants , l'idée creer des parcours dediés en analysant les profils des enfants sans proposer de diagnostique , pour produire un site dedié adapaté aux besoin et difficulté de l'enfant , definir les critéres en colaboration avec de vrai ergo et neuropsy et pourquoi pas proposer des analyses reeles par des professionel de santé remunéré a part de l'abonnement de base l'idée et de capitaliser au fur et a musure pour diminuer les frais d'appel a l'ia pour proposez un tarfis le plus bas possible , vigiclance sur les données proposer un max d'anom=nimastion et securoté plus plus pas de BDD central piratable site complet en mode standalone dedié pour le client
- `e4a84469` (P1) Prproposer une customisation du site a l'nenfant clouerr logo ambiance en DAY 2 → l'idée est qu'une fois que les parents valident lorsque l'enfant prend possession on lui prpose des themes un logo un style un accompagnateur etc

## Utilisateurs

- `1c09d720` (P1) EN V1 les parent et enfant uniquement

## Résultat attendu

- `56ca950c` (P1) Pour P1, quel résultat observable attends-tu → effet waouh identification rapide de la maniere d'accompagner l'enfant proposez une roadmap aux parents avec jalon claire sans entre dans des diagnostics psy ou aute
- `27d396a6` (P1) Pour P1, quel indicateur observable confirmera l'effet waouh ? (ex : temps avant affichage d'un site John Doe, taux de complétion du profil, nombre de parents qui consultent la roadmap) → ok pour la reco
- `2fb1c69d` (P1) Moment de vérité : l'étape où le parent voit le site généré pour son enfant et consulte la roadmap (effet waouh).

## Périmètre

- `8ce11298` (P1) Quel est le parcours minimal de bout en bout pour P1 ? (étapes clés et sortie) → arrivé avec une demo d'un vrai site dedié pour un enfant jonh doe → arrivé avec une demo d'un vrai site dedié pour un enfant jonh doe
- `b4974018` (P1) Quelles étapes concrètes le parent traverse-t-il, de l'arrivée sur la plateforme à la consultation du site dédié John Doe → ok
- `20d5f4d6` (P1) En tant que parent, je veux créer un profil pour mon enfant en renseignant ses besoins et difficultés afin d'obtenir un accompagnement personnalisé.
- `9161a13e` (P1) En tant que parent, je veux accéder à un site dédié généré automatiquement pour mon enfant afin de disposer d'un outil adapté à ses besoins.
- `35dfb3de` (P1) En tant que parent, je veux consulter une roadmap avec des jalons clairs afin de savoir comment accompagner mon enfant au quotidien.
- `e4c20164` (P1) Étape 1 : Arrivée sur la plateforme → le parent remplit le questionnaire profil enfant → Sortie : profil enregistré avec les besoins identifiés.
- `aaa1a997` (P1) Étape 2 : Validation du profil → génération automatique du site John Doe → Sortie : site dédié accessible et fonctionnel.
- `d25ef2c2` (P1) Étape 3 : Le parent consulte le site et la roadmap → Sortie : roadmap affichée avec jalons clairs, sans diagnostic.

## Exclusions

- `30db99af` (P1) pas de diagnostic medical

## Contraintes

- `9fbb1a3c` (P1) maitrise des couts d'api IA

## Hypothèses et questions transverses

- `6de19722` Quelle hypothèse, si elle est fausse, rend le premier parcours impossible ? (ex : capacité à produire un site standalone sans base centrale, génération de recommandations non diagnostiques) → ok
- `6f997497` (P1) Hypothèse : générer un site standalone sans base centrale est techniquement faisable et maîtrisable en coût. Risque : si faux, P1 tombe. Test : prototyper une génération minimale et mesurer temps/coût.
- `c5ff5871` (P1) Hypothèse : les parents acceptent de remplir un questionnaire sur les difficultés sans attendre un diagnostic. Risque : si faux, pas de profil. Test : tester avec l'entourage.
- `db4eda78` Quels professionnels (ergothérapeute, neuropsychologue) seront impliqués pour valider les critères de personnalisation et la non-diagnosticité des contenus générés → En P1 filtre de terme qui ne doivent jamais etre produite vers les parents ou l'enfants DYSxxx TDAH , etc
- `97de4583` Sur quelle base de connaissances (référentiels, guides, données sourcées) les recommandations et jalons de la roadmap seront-ils générés → On va pour la P1 creer un persona eleve dedié a un des difficulté precise pour tester le modele
- `c965c2e6` Quelles mesures précises garantissent l'anonymisation complète et l'absence de base centrale (hébergement, traitement des données, consentement parental pour mineurs) → en P1 pas de données medical
- `1b64f839` Le questionnaire profil enfant collecte-t-il des données de santé (difficultés, besoins spécifiques) ? Si oui, cela contredit « en P1 pas de données médicales » et impose des obligations légales (consentement, minimisation, sécurité renforcée). → Non pas de données de santé , en P1 sinon c'est qu'on c'est mal compris , Mauvaise note en math copie des 3 derniers controles pour post mortem par exemple
- `d39ecaf4` Le filtre de termes interdits (DYS, TDAH, etc.) suffit-il à garantir l'absence de contenu à caractère diagnostique ou de recommandations inappropriées dans le site et la roadmap → LA p1 ne sera pas ouverte au public mais testé par la famille
- `d1ae6976` Quel est le budget maximal acceptable de coût API IA par génération de site, pour tester la viabilité économique de P1 → ok avec la reco

## Critères d’acceptation (vérifiables, à rapporter un par un)

- `8c6b7f37` (P1) : Après validation du profil, le site dédié est disponible en moins de 5 minutes.
- `5d04a7da` (P1) : La roadmap affichée contient au moins 3 jalons avec des actions concrètes.
- `00107720` (P1) : Les contenus générés (site et roadmap) ne contiennent aucun terme médical ou diagnostic (ex : TDAH, dyslexie, autisme).
- `6f7b35fa` (P1) : Le parent peut remplir le questionnaire profil en moins de 10 minutes, avec un maximum de 15 questions. → pour l'effet waouh il faut une collecte minium d'information , copie d'une copie d'un controle ,ca ca va devenir un point sensible

Les éléments marqués [Hypothèse] sont des hypothèses de travail : signale dans le rapport celles qui s’avèrent fausses.
