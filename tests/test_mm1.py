from waiting_phenomenon.mm1 import *

def test_pr_nbs_search_n():
    # From ex: XVII Les parkings de l'Aéroport
    alpha = 2.7
    mu = 3
    condition = 1/100

    solutions = pr_nbs_search_n(alpha, mu, condition)
    sol = solutions[0]
    print('SOLUTION', sol)