from laws.stochastic_matrix import generate_stochastic_matrix
import numpy as np


def test_one_eig_value_is_one():
    stochastic_matrix = generate_stochastic_matrix(5)
    values, vectors = np.linalg.eig(stochastic_matrix)

    def is_true():
        for value in values:
            r = np.allclose([value], [1])
            if r is True:
                return True
        return False

    assert is_true() is True

def test_all_sum_rows_eq_one():
    matrix_size = 5
    stochastic_matrix = generate_stochastic_matrix(matrix_size)

    all_sum_rows_eq_one = np.allclose(stochastic_matrix.sum(axis=1), np.ones(matrix_size))
    assert all_sum_rows_eq_one is True