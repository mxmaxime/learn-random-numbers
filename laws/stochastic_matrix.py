import numpy as np

def generate_stochastic_matrix(matrix_size):
    matrix = np.random.rand(matrix_size, matrix_size)
    stochastique_matrix = matrix / matrix.sum(axis=1)[:, None]
    return stochastique_matrix
