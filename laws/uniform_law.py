import numpy as np

"""
Generate uniform law, from the computer system, defined on [a;b].
"""
def generate_uniform_law(a: float, b: float, n: int) -> float:
    return np.random.uniform(a, b, size=n)

def uniform_cdf(a: float, b: float, x: float) -> float:
    if x >= a and x <= b:
        cdf = (x - a) / (b - a)
    elif x >= b:
        cdf = 1
    else:
        cdf = 0
    return cdf

def uniform_pdf(x, a, b):
    return [ 1/(b-a) if a <= x <= b else 0 for x in x]

"""
a_def, b_def = domaine de définition de la loi uniforme.
Probabilité([a;b]) d'une loi uniforme.
"""
def uniform_probability(a_def: float, b_def: float, a: float, b: float) -> float:
    return uniform_cdf(a_def, b_def, b) - uniform_cdf(a_def, b_def, a)
