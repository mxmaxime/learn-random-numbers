from waiting_phenomenon.mms import e_nbs, compute_p0, e_nbf, e_taf

def decimal_to_date(number: float, unit = 'minutes')-> str:
    if (unit == 'minutes'):
        minutes = int(number)
        seconds = (number*3600) % 60
        return f'{minutes} minutes, {seconds} seconds'
    elif (unit == 'hours'):
        hours = int(number)
        minutes = (number*60) % 60
        seconds = (number*3600) % 60
        return f'{hours} hours, {minutes} minutes, {seconds} seconds'
"""
In some rare cases, the wording doesn't give mu or alpha, just psi.
In that case, we can compute alpha or mu if necessary.
"""
alpha = 2.7
mu = 3

psi = alpha/mu
unit = 'minutes'

clients = 'taxis'

nb_stations = 1

p0_precision = 3
nbf_precision = 2


p0 = compute_p0(nb_stations, psi)
p0 = round(p0, p0_precision)

print(f'p0 = {p0} = {p0*100}%')

nbf = e_nbf(psi, p0, nb_stations)
nbf = round(nbf, nbf_precision)

print(f'{nbf} {clients} en attente en moyenne.')


"""
MM/1
"""

def etaf(psi, alpha, mu):
    a = psi ** 2
    b = alpha * (1-psi)
    return a/b

taf = etaf(psi, alpha, mu)
taf = round(taf, 3)
print(f"{decimal_to_date(taf)} d'attente moyenne")
