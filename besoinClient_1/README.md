# Besoin Client 1 - Prediction de categorie d'arbre

## Objectif
Ce projet predit une categorie d'arbre a partir de deux mesures:
- hauteur totale (m)
- diametre du tronc (cm)

La prediction utilise des modeles de clustering pre-entraines (k=2 ou k=3).

## Prerequis
- Python 3.11 recommande
- pip

## Installation
Depuis le dossier du projet:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Lancement

```powershell
python .\script.py
```

Au demarrage:
1. Le script lance un petit serveur HTTP local sur le port 8080.
2. Il affiche l'URL de la carte:
   - http://127.0.0.1:8080/carte_arbres_interactive.html
3. Il demande les valeurs de prediction dans le terminal.

Ensuite, pour chaque prediction:
1. Saisir la hauteur totale.
2. Saisir le diametre du tronc.
3. Choisir le mode de clustering:
   - 1 = petit - grand (k=2)
   - 2 = petit - moyen - grand (k=3)
4. Lire la categorie retournee.

