# main.py
import numpy as np
import matplotlib.pyplot as plt
from src.matrix_utils import generate_overdetermined_system, build_vandermonde
from src.qr_solver import solve_least_squares_qr, modified_gram_schmidt_qr

def run_phase_1_2_3():
    print("=== Phase 1, 2 & 3: Résolution d'un système surdéterminé Ax=b ===")
    
    # 1. Génération des données
    A, x_true, b = generate_overdetermined_system(m=10, n=4, noise_level=0.1, random_seed=42)
    print(f"Système généré : Matrice A ({A.shape}), Vecteur b ({b.shape})")

    # 2. Résolution avec notre solveur QR
    x_qr = solve_least_squares_qr(A, b)

    # 3. Comparaison avec les solutions de référence
    x_np = np.linalg.lstsq(A, b, rcond=None)[0]
    
    print("\n--- Comparaison des solutions ---")
    print(f"Solution vraie (x_true) : {np.round(x_true, 4)}")
    print(f"Solution QR maison (x_qr) : {np.round(x_qr, 4)}")
    print(f"Solution NumPy (lstsq)  : {np.round(x_np, 4)}")

    # 4. Calcul des erreurs
    error_vs_true = np.linalg.norm(x_qr - x_true) / np.linalg.norm(x_true)
    error_vs_np = np.linalg.norm(x_qr - x_np) / np.linalg.norm(x_np)
    print(f"\nErreur relative (QR vs Vraie): {error_vs_true:.4f}")
    print(f"Erreur relative (QR vs NumPy): {error_vs_np:.4e}")
    
    # 5. Visualisation
    plt.figure(figsize=(10, 5))
    plt.plot(x_true, 'o-', label="x_true (solution exacte)", markersize=8, zorder=3)
    plt.plot(x_qr, 's--', label="x_qr (solution QR)", alpha=0.8, zorder=2)
    plt.plot(x_np, 'x:', label="x_np (solution NumPy)", alpha=0.8, zorder=1)
    plt.xlabel("Index de la variable")
    plt.ylabel("Valeur")
    plt.title("Comparaison des solutions pour Ax=b")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.savefig("solution_comparison.png")
    print("\nGraphique de comparaison sauvegardé dans 'solution_comparison.png'")
    plt.close()


def run_phase_4():
    print("\n=== Phase 4: Tâche avancée - Régression Polynomiale ===")
    
    # 1. Génération des données polynomiales
    true_coeffs = [1.0, -2.0, 0.5]  # Polynôme vrai : 1 - 2x + 0.5x²
    x_data = np.linspace(-4, 4, 30)
    y_data = np.polyval(true_coeffs[::-1], x_data) + np.random.normal(0, 0.8, len(x_data))
    
    # 2. Régression avec notre solveur
    degree = 2
    A_vandermonde = build_vandermonde(x_data, degree)
    coeffs_qr = solve_least_squares_qr(A_vandermonde, y_data)
    
    print(f"\nCoefficients vrais    : {np.round(true_coeffs, 4)}")
    print(f"Coefficients trouvés (QR): {np.round(coeffs_qr, 4)}")
    
    # 3. Visualisation
    plt.figure(figsize=(10, 6))
    plt.scatter(x_data, y_data, label="Données bruitées", color="red", zorder=3)
    x_fit = np.linspace(-4, 4, 200)
    y_true_fit = np.polyval(true_coeffs[::-1], x_fit)
    y_qr_fit = np.polyval(coeffs_qr[::-1], x_fit)
    
    plt.plot(x_fit, y_true_fit, "k--", label="Modèle vrai", linewidth=2)
    plt.plot(x_fit, y_qr_fit, "b-", label=f"Régression QR (degré {degree})", linewidth=2)
    
    plt.title("Régression Polynomiale avec le solveur QR")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.savefig("polynomial_regression.png")
    print("Graphique de régression sauvegardé dans 'polynomial_regression.png'")
    plt.close()


if __name__ == "__main__":
    run_phase_1_2_3()
    run_phase_4()