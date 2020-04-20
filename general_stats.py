import numpy as np
from typing import Callable, List
import matplotlib.pyplot as plt
import itertools

"""
sing range is perfectly fine. However, programming (like maths) is about building on abstractions.
Consecutive pairs [(x0, x1), (x1, x2), ..., (xn-2, xn-1)], are called pairwise combinations.
"""
def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)


"""
Second return: the ddof, degree of freedom.
Simplified version of this formula:
dof = (len(df.columns)-1)*(len(df.index)-1)
Because I have two columns (empirical_values, theoritical_values)
2 - 1 -> 1, so ignore it.
"""
def chi2_test(empirical_values: List[float], theoritical_values: List[float]) -> [float, int]:
    ni = [((empirical - theory)**2)/theory for empirical, theory in zip(empirical_values, theoritical_values)]
    return np.sum(ni), len(empirical_values) - 1

"""
f = la fonction qui permet de calculer, à partir de la fonction de répartition,
la probabilité d'être dans l'intervalle [a,b].
@todo, trouver un bon nom pour cette fonction.
n = le nombre de valeurs aléatoires tirées
bins = les intervalles, ex [0.1, 0.2, 0.3...]
"""
def bins_expected_frequency(compute_probability: Callable[[float, float], float], n: int, bins: List[float]) -> List[float]:
    return [compute_probability(a, b) * n for a,b in pairwise(bins)]


def perform_chi2_test(empirical_values: List[float], compute_probability: Callable[[float, float], List[float]]):
    empirical_values_by_bins, bins, patches = plt.hist(empirical_values)

    expected_values_by_bins = bins_expected_frequency(compute_probability, len(empirical_values), bins)

    return chi2_test(empirical_values_by_bins, expected_values_by_bins), empirical_values, expected_values_by_bins, bins
