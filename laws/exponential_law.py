import numpy as np
from typing import List

"""
Generate exponential law from given uniform values.
"""
def generate_exponential_law(alpha: float, uniform_values: List[float]) -> List[float]:
    return (-1/alpha) * np.log(uniform_values)

def exponential_cdf(alpha: float, x: float)-> float:
    return 1 - np.exp(-alpha * x)

def exponential_pdf(alpha: float):
    return alpha * np.exp(-alpha*x)

"""
Probabilité([a,b]) d'une loi exponentielle définie par son paramètre alpha.
"""
def exponential_probability(alpha: float, a: float, b: float) -> float:
    return exponential_cdf(alpha, b) - exponential_cdf(alpha, a)
