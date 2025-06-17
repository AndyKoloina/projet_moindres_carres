# 🎯 Projet : Moindres Carrés et Décomposition QR

Ce projet présente une implémentation **"maison"** en Python pour la résolution de systèmes linéaires surdéterminés. La méthode s'appuie sur la technique des moindres carrés via une décomposition **QR**, calculée avec l'algorithme de Gram-Schmidt modifié.

L'objectif est de démontrer une compréhension pratique des concepts d'algèbre linéaire en construisant un solveur fonctionnel à partir de principes de base, puis de le valider par rapport aux bibliothèques standards et de l'appliquer à un cas d'usage concret.

---

## 👥 Auteurs du Projet

* Andriantsalama Rijamampianina
* Raharimanitra-Mala T. Jason H.
* RAKOTONIRINA Mendrika Itokiana
* Ranaivo Nirina Andy Nantenaina

---

## ✅ Objectifs

-   **Implémenter** des concepts clés d'algèbre linéaire, notamment la décomposition QR.
-   **Résoudre** un système surdéterminé `Ax=b` de manière numériquement stable.
-   **Comparer** la solution obtenue avec la solution de référence de `numpy.linalg.lstsq`.
-   **Appliquer** la méthode à un problème de **régression polynomiale**.

---

## 📂 Structure du Projet
├── src/
│   ├── init.py
│   ├── matrix_utils.py      # Fonctions pour générer les systèmes (Ax=b, Vandermonde)
│   └── qr_solver.py         # Décomposition QR et solveur de moindres carrés
├── main.py                  # Script principal pour exécuter les démonstrations
├── requirements.txt         # Dépendances du projet
└── README.md                # Ce fichier


## 🚀 Installation

1.  Clonez le dépôt :
    ```sh
    git clone [https://github.com/VOTRE_NOM_UTILISATEUR/projet_moindres_carres.git](https://github.com/VOTRE_NOM_UTILISATEUR/projet_moindres_carres.git)
    cd projet_moindres_carres
    ```

2.  Installez les dépendances :
    ```sh
    pip install -r requirements.txt
    ```

## ▶️ Utilisation

Pour lancer la démonstration complète (résolution de `Ax=b` et régression polynomiale), exécutez le script principal :

```sh
python main.py