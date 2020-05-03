import numpy as np
import math
from fractions import Fraction
from decimal import *

def e_nbs(psi: float, p0: float, nb_stations: int):
    b = (nb_stations / (nb_stations - psi ** 2)) * ((psi ** (nb_stations+1)) / math.factorial(nb_stations)) * p0
    return psi + b

"""
Nb moyen en attente.
"""
def e_nbf(psi: float, p0: float, nb_stations: int):
    a = nb_stations / ((nb_stations - psi) ** 2)
    b = psi ** (nb_stations +1) / math.factorial(nb_stations)
    return a * b * p0

"""
Inputs
"""
# attention!! Si j'ai 120.2 le programme me donne bêtement 120
# precision = 3
# getcontext().prec = precision

# cadence d'arrivée
alpha = 120
# cadence de traitement
mu = 66.6

nb_stations = 2

"""
General compute
"""
# facteur de charge
psi = Decimal(alpha)/Decimal(mu)
psi = round(psi, 2)

# print(f'Facteur de charge: {psi}')

"""
M/M/s Systems formulas
"""

def compute_p0(nb_stations: int, psi: float):
    second_part = (psi**nb_stations)/(math.factorial(nb_stations) * (1 - psi/nb_stations))
    first_part = sum([ (psi**n)/math.factorial(n) for n in range(nb_stations) ])

    return 1/(first_part + second_part)

def compute_ps(psi: float, p0: float, s: int,):
    return (psi**s / math.factorial(s)) * p0

# p0 = compute_p0(2, psi)
# p0 = round(p0, 4)

# print(f'p0 = {p0 * 100}%')

# print(f'p1 = {compute_ps(psi, p0, 1) *100}%')
# print(f'p2 = {compute_ps(psi, p0, 2) *100}%')

# # p0 should be 5.26% -> OK
