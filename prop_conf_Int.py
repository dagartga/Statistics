import numpy as np

# number of users who visited the site
n = 752

# number of users who registered
n_registered = 64

# get the proportion of users who registered
prop_registered = n_registered / n

# get the standard error
se = np.sqrt(prop_registered * (1 - prop_registered) / n)

# use a z-score of 1.645 for a 90% confidence interval
z = 1.645

# calculate the margin of error
moe = z * se

# calculate the lower and upper bounds of the confidence interval
ci_lower = prop_registered - moe
ci_upper = prop_registered + moe

print(f"Proportion of users who registered: {round(prop_registered, 3)}")
print(f"With a confidence interval of 90%: {round(ci_lower, 3)} to {round(ci_upper, 3)}")


from statsmodels.stats.proportion import proportion_confint

ci_low, ci_upp = proportion_confint(n_registered, n, alpha=0.1, method='normal')

print(f"90% Confidence Interval: {round(ci_low, 3)} to {round(ci_upp, 3)}")