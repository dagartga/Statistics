from scipy import stats

# Revenue data
cntrl_avg_rev = 74.1
test_avg_rev = 79.4

# Standard deviations
cntrl_std = 20
test_std = 14

# Sample sizes
cntrl_size = 100
test_size = 100

small_ctrl = 50
small_test = 50

# Perform two-sample t-test
t_statistic, p_value = stats.ttest_ind_from_stats(
    mean1=cntrl_avg_rev,
    std1=cntrl_std,
    nobs1=cntrl_size,
    mean2=test_avg_rev,
    std2=test_std,
    nobs2=test_size,
)

# Perform two-sample t-test
t_statistic_small, p_value_small = stats.ttest_ind_from_stats(
    mean1=cntrl_avg_rev,
    std1=cntrl_std,
    nobs1=small_ctrl,
    mean2=test_avg_rev,
    std2=test_std,
    nobs2=small_test,
)



# Print results
print("Sample Sizes of 100")
print("T-Statistic:", t_statistic)
print("P-Value:", p_value)

# Print results
print("\n\nSample Sizes of 50")
print("T-Statistic:", t_statistic_small)
print("P-Value:", p_value_small)
