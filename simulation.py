"""
Je vais simuler les pannes suivant l'exercice
"XIX" équipement d'un vaisseau spatial.
"""

import numpy as np
import scipy.stats as stats

"""
Pr(Durée de vie > t)
"""
def loi_de_survie(alpha, t):
    return np.exp(-alpha * t)

alpha_ad = 1/2e6

t = 87600

N = 1000
uniform_values = np.random.uniform(size=N)

# values = generate_exponential_law(alpha_ad, uniform_values)


fiabilite = loi_de_survie(alpha_ad, t)

print(f'{fiabilite*100}% probabilité de fiabilité théorique')
print(f'proba de panne théorique: {(1 - fiabilite)*100}%')

en_panne = uniform_values[uniform_values < 1 - fiabilite]

nb_pannes = len(en_panne)

print(f'réelle proba de panne: {(nb_pannes / N)*100}%')

# print(stats.t.interval(0.95, len(en_panne)-1, loc=np.mean(en_panne), scale=stats.sem(en_panne)))
