# Besoin Client 2 — Prédiction de l’âge des arbres

## Description du projet

Ce projet a pour objectif de développer un modèle d’intelligence artificielle capable de prédire la classe d’âge d’un arbre (jeune, moyen, vieux) à partir de ses caractéristiques (hauteur, diamètre, situation, etc.).

Le modèle repose sur une approche d’apprentissage supervisé et a été entraîné à partir d’un jeu de données nettoyé issu de la partie Big Data du projet.

---

## Méthodologie

Le pipeline de traitement se décompose en plusieurs étapes :

1. Préparation des données (sélection des variables, traitement des valeurs manquantes)
2. Encodage des variables catégorielles (One-Hot Encoding)
3. Normalisation des variables numériques
4. Création de nouvelles variables (feature engineering)
5. Transformation de la cible en classes d’âge
6. Entraînement de plusieurs modèles de classification :

   * Logistic Regression
   * Random Forest
   * Gradient Boosting
7. Optimisation des hyperparamètres avec `GridSearchCV`
8. Évaluation des performances (accuracy, précision, recall, f1-score)
9. Sauvegarde du modèle final au format `.pkl`

---

## Performances

Le modèle final présente de très bonnes performances, avec une précision élevée.
La matrice de confusion montre que les erreurs sont principalement des confusions entre classes proches (jeune/moyen et moyen/vieux), ce qui est cohérent avec la nature progressive de l’âge.

---

##  Structure du projet

```text
besoinClient_2/
│
├── models/
│   └── model_age_classification_pipeline.pkl
│
├── besoin_client_2_classification.ipynb
├── predict_age.py
└── README.md
```

---

## Installation

Installer les dépendances nécessaires :

```bash
pip install numpy pandas scikit-learn
```

---

## Utilisation

### Lancement du script

```bash
python predict_age.py
```

Utilise des valeurs par défaut

---

### Exemple avec paramètres personnalisés

```bash
python predict_age.py --model models/model_age_classification_pipeline.pkl --haut_tot 18 --tronc_diam 45 --nomfrancais "Erable plane"
```

---

### Exemple complet

```bash
python predict_age.py --model models/model_age_classification_pipeline.pkl --haut_tot 12 --haut_tronc 4 --tronc_diam 30 --clc_nbr_diag 0 --clc_quartier "Centre Ville" --clc_secteur "Centre" --fk_arb_etat "En place" --fk_stadedev "Adulte" --fk_situation "Isole" --feuillage "Caduc" --remarquable "Oui" --nomfrancais "Erable plane" --show-input
```

---

## Fonctionnement

Le script :

1. Charge le modèle `.pkl`
2. Récupère les données utilisateur
3. Génère automatiquement les variables dérivées :

   * `remarquable_bin`
   * `ratio_tronc_haut`
   * `ratio_diam_haut`
4. Applique le pipeline de transformation
5. Retourne la classe d’âge prédite

---

## Conclusion

Ce projet met en œuvre une chaîne complète de traitement des données et de modélisation en apprentissage supervisé. Il permet de transformer des données brutes en un outil prédictif exploitable, pouvant être intégré dans une application plus large (Web ou décisionnelle).
