import numpy as np

initial = np.array([50/100, 40/100, 10/100])

print(f'PI(0) = {initial}')

transition_matrix = np.array([[30/100, 50/100, 20/100],[30/100, 40/100, 30/100], [0, 60/100, 40/100]])

print(f'Matrice de transition: \n {transition_matrix}')
# values, vectors = np.linalg.eig(transition_matrix)
# print(f'Matrice de transition, valeurs propres: {values} \n vecteurs propres: {vectors}')

# print(f'P² = {np.linalg.matrix_power(transition_matrix, 2)}')
# print(f'P^3 = {np.linalg.matrix_power(transition_matrix, 3)}')

nb_state_to_compute = 1000

def compute_state(initial, transition_matrix, nb_state_to_compute: int):
    pn_1 = initial
    steps = []
    for i in range(1, nb_state_to_compute+1):
        pn = np.dot(pn_1, transition_matrix)
        # pn = pn_1 * transition_matrix
        pn_1 = pn
        steps.append(pn)

    return steps

steps = compute_state(initial, transition_matrix, nb_state_to_compute)

nb_steps_to_show = 4
print(f'Affichage de PI(1) to PI({nb_steps_to_show})')
for n in range(nb_steps_to_show):
    print(f'PI({n+1}) = {steps[n]}')

print(f'État permanent: {steps[nb_state_to_compute-1]}')

# print(f'steps_sun: {steps_sun}')
