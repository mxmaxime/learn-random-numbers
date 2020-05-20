import numpy as np
from typing import List

"""
Generate Weibull law from given uniform values.
"""
def generate_weibull_law(alpha: float, beta: float, uniform_values: List[float]) -> List[float]:
    a = -np.log(1 - uniform_values) / np.power(alpha, beta)
    b = 1 / beta

    return a / b

def weibull_cdf(alpha: float, beta: float, x: float) -> float:
    return 1 - np.exp(-(alpha * x) ** beta)

def weibull_probability(alpha: float, beta: float, a: float, b: float) -> float:
    return weibull_cdf(alpha, beta, b) - weibull_cdf(alpha, beta, a)
