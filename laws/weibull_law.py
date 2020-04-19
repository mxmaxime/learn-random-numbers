"""
Generate Weibull law from given uniform values.
"""
def generate_weibull_law(alpha: float, beta: float, uniform_values: List[float]) -> List[float]:
    a = -np.log(1 - uniform_values) / np.power(alpha, beta)
    b = 1 / beta

    return a / b
