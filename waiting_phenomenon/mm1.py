from sympy.solvers import solve, nsolve
from sympy import Symbol

"""
Pr(Nbs <= N) <= wanted
Return the N value.
"""
def pr_nbs_search_n(alpha: float, mu: float, wanted: float):
    N = Symbol('N', real=True)

    solutions = solve((alpha/mu)**(N) - wanted, N)
    return solutions

"""
Pr(NbS > N) <= wanted
"""
def pr_nbs_inverse_inequation(alpha: float, mu: float, N: int, wanted: float):
    x = Symbol('x', real=True)

    if (alpha is None):
        solutions = solve((x/mu)**(N+1) - wanted, x)
        return solutions
    
    if (mu is None):
        solutions = solve((alpha/x)**(N+1) - wanted, x)
        return solutions

    return None

def pr_nbs_inequation(alpha: float, mu: float, N: int, wanted: float):
    x = Symbol('x', real=True)

    if (alpha is None):
        solutions = solve(1 - (x/mu)**(N+1) - wanted, x)
        return solutions
    
    if (mu is None):
        solutions = solve(1 - (alpha/x)**(N+1) - wanted, x)
        return solutions


"""
Pr(NbS <= N)
N clients dans le système.
Warning: inclus les clients en attente
"""
def pr_nbs(psi: float, N: int) -> float:
    return 1 - psi ** (N+1)

"""
Pr(NbS > N)
Plus que N clients dans le système.
Warning: inclus les clients en attente
"""
def pr_nbs_inverse(psi: float, N: int) -> float:
    return psi ** (N+1)

"""
nbs = nb de clients dans le système
"""
def e_nbs(psi: float) -> float:
    return psi / (1-psi)


"""
tas = temps d'attente dans le système
"""
def e_tas(psi: float, alpha: float) -> float:
    return psi / (alpha * (1 - psi))


"""
nbf = nombre de clients dans la file d'attente
"""
def e_nbf(psi: float) -> float:
    return (psi ** 2) / (1-psi)


"""
taf = temps d'attente dans la fille
"""
def e_taf(psi: float, alpha: float) -> float:
    return (psi**2) / (alpha * (1 - psi))

"""
nbsi = nombre de stations inocupées
"""
def e_nbsi(psi: float) -> float:
    return 1 - psi
