# Projet : Moindres Carrés et Décomposition QR

Ce projet est une implémentation "maison" en Python de la résolution de systèmes linéaires surdéterminés par la méthode des moindres carrés, en utilisant une décomposition QR basée sur l'algorithme de Gram-Schmidt modifié.

## Objectifs
- Implémenter des concepts clés d'algèbre linéaire.
- Résoudre un système `Ax=b` surdéterminé.
- Comparer la solution obtenue à celle de `numpy.linalg.lstsq`.
- Appliquer la méthode à un problème de régression polynomiale.

## Structure du projet
├── src/
│   ├── init.py
│   ├── matrix_utils.py      # Fonctions pour générer les systèmes (Ax=b, Vandermonde)
│   └── qr_solver.py         # Décomposition QR et solveur de moindres carrés
├── main.py                  # Script principal pour exécuter les démonstrations
├── requirements.txt         # Dépendances du projet
└── README.md                # Ce fichier


## Installation

1.  Clonez le dépôt :
    ```sh
    git clone [https://github.com/VOTRE_NOM_UTILISATEUR/projet_moindres_carres.git](https://github.com/VOTRE_NOM_UTILISATEUR/projet_moindres_carres.git)
    cd projet_moindres_carres
    ```

2.  Installez les dépendances :
    ```sh
    pip install -r requirements.txt
    ```

## Utilisation

Pour lancer la démonstration complète (résolution de `Ax=b` et régression polynomiale), exécutez le script principal :

```sh
python main.py