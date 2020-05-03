from decimal import *

getcontext().prec = 2

alpha = 120
mu = 66.6

nb_stations = 2

psi = Decimal(alpha)/Decimal(mu)


print(f'Facteur de charge: {psi}')

from fractions import Fraction
print(Fraction(psi))
