from scipy.stats import norm
import numpy as np
from typing import List


"""
Génération de deux v.a normales à partir de deux v.a indépendantes uniformes.
Utilisation de la méthode de Box et Müller.
Obtention d'une variable centrée réduite.
"""
def generate_normale_law(uniform_values1: List[float], uniform_values2: List[float]):
    U = uniform_values1
    V = uniform_values2

    theta = 2 * np.pi * V
    R = -2 * np.log(U)

    X = np.sqrt(R) * np.cos(theta)
    Y = np.sqrt(R) * np.sin(theta)

    return X, Y

"""
Probabilité([a,b]) d'une loi normale.
"""
def normale_probability(mu: float, sigma: float, a: float, b: float) -> float:
    return norm.cdf(b, mu, sigma) - norm.cdf(a, mu, sigma)
