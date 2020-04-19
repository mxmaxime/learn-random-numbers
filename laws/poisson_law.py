import numpy as np

def poisson(lamb: float, k: int) -> float:
    return (lamb**k) * np.exp(-lamb) / math.factorial(k)
