import numpy as np

initial_rain = np.array([1, 0, 0])
# initial_sun = np.array([1, 0])

transition_matrix = np.array([[2/3, 1/3, 0],[1/4, 1/2, 1/4], [1/2, 1/2, 0]])
# values, vectors = np.linalg.eig(transition_matrix)

# v = np.array([0.8, 0.2])
# print(f'stabilité ?? ', np.dot(v, transition_matrix))

# print(f'P² = {np.linalg.matrix_power(transition_matrix, 2)}')
# print(f'P^3 = {np.linalg.matrix_power(transition_matrix, 3)}')

# print(f'Matrice de transition, valeurs propres: {values} \n vecteurs propres: {vectors}')


nb_state_to_compute = 100

def compute_state(initial, transition_matrix, nb_state_to_compute: int):
    pn_1 = initial
    steps = []
    for i in range(1, nb_state_to_compute+1):
        pn = np.dot(pn_1, transition_matrix)
        # pn = pn_1 * transition_matrix
        pn_1 = pn
        steps.append(pn)

    return steps


steps_rain = compute_state(initial_rain, transition_matrix, nb_state_to_compute)
# steps_sun = compute_state(initial_sun, transition_matrix, nb_state_to_compute)

print(f'steps_rain: {steps_rain}')
# print(f'steps_sun: {steps_sun}')
