import numpy as np
import statsmodels.stats.power as smp

# Control group data
control_size = 100
control_mean = 74.1
control_std = 20

# Treatment group data
treatment_size = 100
treatment_mean = 79.4
treatment_std = 14

# Calculating pooled standard deviation
pooled_std = np.sqrt(
    ((control_size - 1) * control_std**2 + (treatment_size - 1) * treatment_std**2)
    / (control_size + treatment_size - 2)
)

# Calculating effect size
effect_size = (treatment_mean - control_mean) / pooled_std

# Significance level (alpha)
alpha = 0.05

# Calculating power
power = smp.tt_ind_solve_power(
    effect_size=effect_size,
    nobs1=control_size,
    alpha=alpha,
    ratio=treatment_size / control_size,
    alternative="larger",
)

print("Power of the t-test for sample sizes 100:", round(power, 3))

print(
    "The probability of incorrectly failing to \nreject the null hypothesis is {0:.2f}".format(
        1 - round(power, 3)
    )
)


print(
    "The power of the t-test is the probability \nof correctly rejecting the null hypothesis \nwhen the alternative hypothesis is true."
)
