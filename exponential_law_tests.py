import numpy as np
import pandas as pd
import scipy.stats
from functools import partial

from laws.exponential_law import generate_exponential_law, exponential_probability
from general_stats import perform_chi2_test


def zz():
    N = 20000
    U = np.random.uniform(size=N)

    lamb = 1/5
    exponential_values = generate_exponential_law(lamb, U)
    chi2, empirical_values, expected_values, bins = perform_chi2_test(exponential_values, partial(exponential_probability, lamb))

    chi2_value, ddof = chi2

    df = pd.DataFrame({'empirical_values': empirical_values, 'expected_values': expected_values}, bins[:-1])


    tstat_scipy, pval_scipy, ddof_scipy, exp_scipy = scipy.stats.chi2_contingency(df, correction=False)
    print(f"Chi-squared test statistic without Yates correction (Scipy): {tstat_scipy}")
    print("Value from test_perso:", chi2_value)
    print(f"pval from scypi: {pval_scipy}")
    print(f"ddof_scipy: {ddof_scipy} vs ddof: {ddof}")

zz()