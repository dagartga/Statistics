import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.stats import ttest_ind, mannwhitneyu

# create a non-normal distribution
np.random.seed(0)
data_1 = np.random.exponential(scale=2, size=10)
data_2 = np.random.exponential(scale=2, size=10) + 1

print(data_1.mean(), data_2.mean())

# plot the data
sns.histplot(data_1, kde=True)
sns.histplot(data_2, kde=True)
plt.show()

# perform a t-test
t_stat, p_val = ttest_ind(data_1, data_2)

print("Non-normal distribution t-test results:")
print("P-value:", p_val)

# perform a mann-whitney test
stat_val, p_val = mannwhitneyu(data_1, data_2)

print("Non-normal distribution Mann-Whitney results:")
print("P-value:", p_val)

# perform central limit theorem
sample_means_1 = []
sample_means_2 = []

for i in range(1000):
    sample_1 = np.random.choice(data_1, size=5)
    sample_2 = np.random.choice(data_2, size=5)
    sample_means_1.append(sample_1.mean())
    sample_means_2.append(sample_2.mean())

# plot the sample means
sns.histplot(sample_means_1, kde=True)
sns.histplot(sample_means_2, kde=True)
plt.show()

# perform a t-test
t_stat, p_val = ttest_ind(sample_means_1, sample_means_2)

print("Central Limit Theorem t-test results:")
print("P-value:", p_val)
