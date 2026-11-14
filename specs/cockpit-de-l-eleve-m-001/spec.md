# Spécification cockpit-de-l-eleve-m-001

> Mission M-001 du projet « COckpit de l'eleve », générée par le cockpit à partir de la version **v1.0** validée par l'opérateur (P1).
> Ce fichier est figé par le commit indiqué dans le commentaire de validation de l’issue.

## Objectif

- (P1) Une plateforme d'accompagnement personalisé pour les enfants , l'idée creer des parcours dediés en analysant les profils des enfants sans proposer de diagnostique , pour produire un site dedié adapaté aux besoin et difficulté de l'enfant , definir les critéres en colaboration avec de vrai ergo et neuropsy et pourquoi pas proposer des analyses reeles par des professionel de santé remunéré a part de l'abonnement de base l'idée et de capitaliser au fur et a musure pour diminuer les frais d'appel a l'ia pour proposez un tarfis le plus bas possible , vigiclance sur les données proposer un max d'anom=nimastion et securoté plus plus pas de BDD central piratable site complet en mode standalone dedié pour le client
- [Question ouverte] (P1) Prproposer une customisation du site a l'nenfant clouerr logo ambiance en DAY 2

## Utilisateurs

- (P1) EN V1 les parent et enfant uniquement

## Résultat attendu

- (P1) Pour P1, quel résultat observable attends-tu → effet waouh identification rapide de la maniere d'accompagner l'enfant proposez une roadmap aux parents avec jalon claire sans entre dans des diagnostics psy ou aute
- (P1) Pour P1, quel indicateur observable confirmera l'effet waouh ? (ex : temps avant affichage d'un site John Doe, taux de complétion du profil, nombre de parents qui consultent la roadmap) → ok pour la reco
- (P1) Moment de vérité : l'étape où le parent voit le site généré pour son enfant et consulte la roadmap (effet waouh).

## Périmètre

- (P1) Quel est le parcours minimal de bout en bout pour P1 ? (étapes clés et sortie) → arrivé avec une demo d'un vrai site dedié pour un enfant jonh doe → arrivé avec une demo d'un vrai site dedié pour un enfant jonh doe
- (P1) Quelles étapes concrètes le parent traverse-t-il, de l'arrivée sur la plateforme à la consultation du site dédié John Doe → ok
- (P1) En tant que parent, je veux créer un profil pour mon enfant en renseignant ses besoins et difficultés afin d'obtenir un accompagnement personnalisé.
- (P1) En tant que parent, je veux accéder à un site dédié généré automatiquement pour mon enfant afin de disposer d'un outil adapté à ses besoins.
- (P1) En tant que parent, je veux consulter une roadmap avec des jalons clairs afin de savoir comment accompagner mon enfant au quotidien.
- (P1) Étape 1 : Arrivée sur la plateforme → le parent remplit le questionnaire profil enfant → Sortie : profil enregistré avec les besoins identifiés.
- (P1) Étape 2 : Validation du profil → génération automatique du site John Doe → Sortie : site dédié accessible et fonctionnel.
- (P1) Étape 3 : Le parent consulte le site et la roadmap → Sortie : roadmap affichée avec jalons clairs, sans diagnostic.

## Exclusions

- (P1) pas de diagnostic medical

## Contraintes

- (P1) maitrise des couts d'api IA

## Hypothèses et questions transverses

- Quelle hypothèse, si elle est fausse, rend le premier parcours impossible ? (ex : capacité à produire un site standalone sans base centrale, génération de recommandations non diagnostiques) → ok

## Critères d’acceptation (vérifiables, à rapporter un par un)

- `8c6b7f37` (P1) : Après validation du profil, le site dédié est disponible en moins de 5 minutes.
- `5d04a7da` (P1) : La roadmap affichée contient au moins 3 jalons avec des actions concrètes.
- `00107720` (P1) : Les contenus générés (site et roadmap) ne contiennent aucun terme médical ou diagnostic (ex : TDAH, dyslexie, autisme).
- `6f7b35fa` (P1) : Le parent peut remplir le questionnaire profil en moins de 10 minutes, avec un maximum de 15 questions. → pour l'effet waouh il faut une collecte minium d'information , copie d'une copie d'un controle ,ca ca va devenir un point sensible

Les éléments marqués [Hypothèse] sont des hypothèses de travail : signale dans le rapport celles qui s’avèrent fausses.
