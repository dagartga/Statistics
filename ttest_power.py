import numpy as np
import statsmodels.stats.power as smp

# Control group data
CONTROL_SIZE = 100
CONTROL_MEAN = 74.1
CONTROL_STD = 20

# Treatment group data
TREATMENT_SIZE = 100
TREATMENT_MEAN = 79.4
TREATMENT_STD = 14

# Significance level (alpha)
ALPHA = 0.05

# Calculating pooled standard deviation
pooled_std = np.sqrt(
    ((CONTROL_SIZE - 1) * CONTROL_STD**2 + (TREATMENT_SIZE - 1) * TREATMENT_STD**2)
    / (CONTROL_SIZE + TREATMENT_SIZE - 2)
)

# Calculating effect size
effect_size = (TREATMENT_MEAN - CONTROL_MEAN) / pooled_std


# Calculating power
power = smp.tt_ind_solve_power(
    effect_size=effect_size,
    nobs1=CONTROL_SIZE,
    alpha=ALPHA,
    ratio=TREATMENT_SIZE / CONTROL_SIZE,
    alternative="larger",
)

print("Power of the t-test:", power)
print(
    "The power of the t-test is the probability \nof correctly rejecting the null hypothesis \nwhen the alternative hypothesis is true."
)
print(
    "The probability of incorrectly failing to \nreject the null hypothesis is {0:.2f}".format(
        1 - power
    )
)
