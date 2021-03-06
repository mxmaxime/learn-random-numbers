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
Using the Little formula.
Temps moyen dans le système.
"""
def e_tas(nb_tas: float, alpha: float):
    return nb_tas * alpha

"""
Using the Little formula.
Temps moyen dans dans la file d'attente.
"""
def e_taf(nb_taf: float, alpha: float):
    return nb_taf * alpha

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

"""
Pr(N <= x)
"""
def compute_pr_states(nb_stations: int, psi: float, x: int, round_precision = 3):
    # first step, compute p0* until p(s-1)*
    p0 = compute_p0(nb_stations, psi)
    p0 = round(p0, 3)

    # [1, nb_stations[
    p = [((psi ** n) / math.factorial(n)) * p0 for n in range(1, nb_stations)]

    p = [round(n, 4) for n in p]

    total_1 = sum(p) + p0
    total_1 = round(total_1, 4)

    print(f'p0* = {p0} = {p0*100}%')
    [print(f'p{n}* = {p} = {p*100}%') for n, p in enumerate(p, 1)]
    print(f'total 1 = {total_1} = {total_1*100}%')

    pn = ((psi ** nb_stations) / math.factorial(nb_stations)) * p0
    pn = round(pn, 4)
    print(f'p{nb_stations}* = {pn}')


    q = psi/nb_stations
    print(f'q = {q}')
    print(f'U0 = {pn}')

    n = x - (nb_stations -1)
    # sum k = nb_station to x
    total_2 = pn * (1 - q**(n)) / (1-q)
    total_2 = round(total_2, 3)
    print(f'total_2 = {total_2}')

    print(f'Voici la série numérique utilisée: {pn} * (1 - {q}^{n})) / (1-{q})')

    return total_1 + total_2

x = compute_pr_states(3, 2.7, 15)
print(x)

# x_bis = compute_pr_states(4, 2.7, 16)
# print(x_bis * 100)

# p0 = compute_p0(2, psi)
# p0 = round(p0, 4)

# print(f'p0 = {p0 * 100}%')

# print(f'p1 = {compute_ps(psi, p0, 1) *100}%')
# print(f'p2 = {compute_ps(psi, p0, 2) *100}%')

# # p0 should be 5.26% -> OK
