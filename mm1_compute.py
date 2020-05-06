from waiting_phenomenon.mm1 import *

alpha = 2
mu = 3
psi = alpha/mu

clients = 'clients'


nbs = e_nbs(psi)
print(f'E(nbs) = {nbs} clients dans le système')

N = 6
print(f"Probabilité d'avoir > {N} clients dans le système = Pr(NbS > {N}) = {pr_nbs_inverse(psi, N)}")

N = 6
condition = 5/100

r = pr_nbs_inverse_inequation(None, mu, N, condition)
print(f'Pr(NbS > {N}) <= {condition} <=> lambda <= {r}')

alpha = 2.7
mu = 3
condition = 1/100

solutions = pr_nbs_search_n(alpha, mu, condition)

print(f'Pr(Nbs <= N) <= {condition} <=> N = {solutions}')

N = 6
alpha = 5
mu = None
condition = 5/100
solutions = pr_nbs_inequation(alpha, mu, N, condition)
print(f'Pr(Nbs <= {N}) <= {condition} <=> mu = {solutions}')
