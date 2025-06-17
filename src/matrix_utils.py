import numpy as np

def generate_overdetermined_system(m, n, noise_level=0.0, random_seed=None):
    """
    Génère un système surdéterminé Ax = b avec bruit optionnel.
    
    Paramètres:
        m (int): Nombre d'équations (doit être > n).
        n (int): Nombre d'inconnues.
        noise_level (float): Amplitude du bruit gaussien (défaut: 0).
        random_seed (int): Seed pour la reproductibilité (défaut: None).
    
    Retourne:
        A (np.ndarray): Matrice (m, n).
        x_true (np.ndarray): Solution vraie (n,).
        b (np.ndarray): Vecteur (m,) = Ax_true + bruit.
    """
    if random_seed is not None:
        np.random.seed(random_seed)
    
    # Génération de A (valeurs entre -1 et 1)
    A = np.random.uniform(low=-1.0, high=1.0, size=(m, n))
    
    # Solution vraie (valeurs entre -10 et 10)
    x_true = np.random.uniform(low=-10.0, high=10.0, size=n)
    
    # Calcul de b = Ax + bruit
    b = A @ x_true
    if noise_level > 0:
        b += np.random.normal(loc=0.0, scale=noise_level, size=m)
    
    return A, x_true, b

def build_vandermonde(x, degree):
    """
    Construit la matrice de Vandermonde pour la régression polynomiale.
    """
    return np.column_stack([x**i for i in range(degree + 1)])