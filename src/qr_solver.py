# src/qr_solver.py
import numpy as np

def modified_gram_schmidt_qr(A):
    """
    Décomposition QR via Gram-Schmidt modifié (stable).
    
    Retourne:
        Q (np.ndarray): Matrice orthogonale (m, n).
        R (np.ndarray): Matrice triangulaire supérieure (n, n).
    """
    m, n = A.shape
    Q = np.zeros((m, n))
    R = np.zeros((n, n))
    
    for j in range(n):
        v = A[:, j].copy()
        
        for i in range(j):
            R[i, j] = Q[:, i] @ v
            v -= R[i, j] * Q[:, i]
        
        R[j, j] = np.linalg.norm(v)
        if R[j, j] < 1e-10:
            raise ValueError("Matrice A a des colonnes linéairement dépendantes")
        Q[:, j] = v / R[j, j]
    
    return Q, R

def solve_least_squares_qr(A, b):
    """
    Résout le problème des moindres carrés Ax ≈ b via décomposition QR.
    """
    Q, R = modified_gram_schmidt_qr(A)
    # Résout Rx = Q^T * b
    b_proj = Q.T @ b
    x = np.linalg.solve(R, b_proj)
    return x