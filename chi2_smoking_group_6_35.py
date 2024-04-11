import numpy as np
from scipy.stats import chi2, chi2_contingency


# load the data
patch_support_quit = 40
patch_support_smoke = 110
patch_no_support_quit = 30
patch_no_support_smoke = 120

# print the percent that quit in each group
print(f"Percent that quit with support group: {round(patch_support_quit / (patch_support_quit + patch_support_smoke) * 100)}%")
print(f"Percent that quit without support group: {round(patch_no_support_quit / (patch_no_support_quit + patch_no_support_smoke) * 100)}%")

# create the contingency table
obs = np.array([[patch_support_quit, patch_support_smoke],
                [patch_no_support_quit, patch_no_support_smoke]])

# perform the chi-square test
chi2_stat, p_val, dof, ex = chi2_contingency(obs)
print(f"Chi2 Stat: {chi2_stat}")
print(f"Degrees of Freedom: {dof}")
print(f"P-Value: {p_val}")

# determine the critical value
alpha = 0.05
critical_value = chi2.ppf(1 - alpha, dof)
print(f"Critical Value: {critical_value}")
