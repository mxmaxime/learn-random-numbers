import numpy as np
import scipy

"""
"""
def generate_poisson_law(lamb: float, size: int):
    return scipy.stats.poisson.rvs(lamb, size=size)

def poisson(lamb: float, k: int) -> float:
    return (lamb**k) * np.exp(-lamb) / math.factorial(k)

"""
Probability([a;b])
"""
def poisson_probability(lamb: float, a: float, b: float):
    return scipy.stats.poisson.cdf(b, lamb) - scipy.stats.poisson.cdf(a, lamb)
