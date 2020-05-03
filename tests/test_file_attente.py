from file_attente import e_nbs, compute_p0, e_nbf

def test_compute_p0():
    alpha = 120
    mu = 66.6

    nb_stations = 2

    psi = alpha/mu
    psi = round(psi, 2)

    p0 = compute_p0(2, psi)
    p0 = round(p0, 4)


    assert p0 == 0.0526

    p0_bis = compute_p0(3, 2.7)
    p0_bis = round(p0_bis, 4)

    assert p0_bis == 0.0249

def test_e_nbf():
    p0 = compute_p0(3, 2.7)
    p0 = round(p0, 3)

    pr = e_nbf(2.7, p0, 3)
    pr = round(pr, 2)

    assert pr == 7.38

# def test_e_bns():
#     alpha = 2.7
#     mu = 3
#     psi = alpha / mu

#     p0 = compute_p0(1, psi)

#     pr = e_nbs(psi, p0, 1)
#     print(pr)