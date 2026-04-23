import pickle, json, numpy as np
from pathlib import Path
import pandas as pd

BASE = str(Path(__file__).parent) + "/"

def charger_modele(k: int):
    with open(BASE + "scaler.pkl", "rb") as f:
        scaler = pickle.load(f)
    with open(BASE + f"model_k{k}.pkl", "rb") as f:
        model = pickle.load(f)
    with open(BASE + f"model_k{k}.json", encoding="utf-8") as f:
        meta = json.load(f)
    return scaler, model, {int(c): v for c, v in meta["label_map"].items()}, meta["algorithme"]


def predire(haut_tot, tronc_diam, k):
    scaler, model, label_map, algo = charger_modele(k)
    X_sc = scaler.transform(pd.DataFrame([[haut_tot, tronc_diam]], columns=['haut_tot', 'tronc_diam']))
    cluster = int(model.predict(X_sc)[0])
    return label_map[cluster], cluster, algo


if __name__ == "__main__":
    print("\n── Prédiction de catégorie d'arbre ──────────────────────────")

    while True:
        try:
            haut_tot   = float(input("Hauteur totale (m)      : "))
            tronc_diam = float(input("Diamètre du tronc (cm)  : "))
            k          = int(input("Clustering k (2 ou 3)   : "))
            if k not in (2, 3):
                print("k doit être 2 ou 3\n")
                continue
        except ValueError:
            print("Valeur invalide\n")
            continue

        categorie, cluster, algo = predire(haut_tot, tronc_diam, k)

        print(f"\n  Catégorie : {categorie}")
        print(f"  Cluster   : n°{cluster}")
        print(f"  Algorithme: {algo}")
        print("─" * 50)

        again = input("\nNouvelle prédiction ? (o/n) : ").strip().lower()
        if again != "o":
            break

    print("Au revoir.\n")