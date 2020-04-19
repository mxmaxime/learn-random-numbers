import numpy as np
from typing import List


"""
# génération de deux v.a indépendantes, uniformes sur [0;1]
"""
def generate_normale_law(uniform_values1: List[float], uniform_values2: List[float]):
    U = uniform_values1
    V = uniform_values2

    theta = 2 * np.pi * V
    R = -2 * np.log(U)

    X = np.sqrt(R) * np.cos(theta)
    Y = np.sqrt(R) * np.sin(theta)

    return X, Y
