"""
Pr(NbS <= N)
N clients dans le système.
/!\ inclus les clients en attente
"""
def pr_nbs(psi: float, N: int):
    return 1 - psi ** (N+1)


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
