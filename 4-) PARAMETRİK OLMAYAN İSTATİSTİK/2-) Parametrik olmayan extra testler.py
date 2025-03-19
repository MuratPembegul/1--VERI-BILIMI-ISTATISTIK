import numpy as np
import scipy.stats as stats

# Örnek veriler
np.random.seed(42)
data1 = np.random.randint(50, 100, 12)
data2 = np.random.randint(50, 100, 12)
data3 = np.random.randint(50, 100, 12)

# Mood's Median Test
def moods_median_test(data1, data2, data3):
    stat, p, _, _ = stats.median_test(data1, data2, data3)
    print(f"Mood's Median Test: Chi2={stat}, p={p}")

# Kolmogorov-Smirnov Testi
def kolmogorov_smirnov_test(data1, data2):
    stat, p = stats.ks_2samp(data1, data2)
    print(f"Kolmogorov-Smirnov Testi: D={stat}, p={p}")

# Spearman Korelasyon Testi
def spearman_test(data1, data2):
    stat, p = stats.spearmanr(data1, data2)
    print(f"Spearman Korelasyon Testi: rho={stat}, p={p}")

# Kendall Tau Korelasyon Testi
def kendall_tau_test(data1, data2):
    stat, p = stats.kendalltau(data1, data2)
    print(f"Kendall Tau Korelasyon Testi: tau={stat}, p={p}")

# Testleri çalıştır
moods_median_test(data1, data2, data3)
kolmogorov_smirnov_test(data1, data2)
spearman_test(data1, data2)
kendall_tau_test(data1, data2)
