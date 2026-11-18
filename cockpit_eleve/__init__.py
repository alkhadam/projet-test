"""Cockpit de l'élève — mission M-003.

Ce paquet construit le « contenant » (moteurs) du parcours P1 :
questionnaire -> profil -> roadmap -> site dédié. Le « contenu » de domaine
est chargé depuis des fichiers de configuration (emplacements A_DEFINIR_*).
"""

from pathlib import Path

CONFIG_DIR = Path(__file__).resolve().parent / "config"

__all__ = ["CONFIG_DIR"]
