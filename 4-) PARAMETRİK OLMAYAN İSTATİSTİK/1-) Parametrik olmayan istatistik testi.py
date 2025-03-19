import numpy as np
import scipy.stats as stats

# Örnek veriler
np.random.seed(42)
group1 = np.random.randint(50, 100, 10)
group2 = np.random.randint(50, 100, 10)
group3 = np.random.randint(50, 100, 10)

def mann_whitney_test(group1, group2):
    stat, p = stats.mannwhitneyu(group1, group2)
    print(f"Mann-Whitney U Testi: U={stat}, p={p}")

def wilcoxon_test(group1, group2):
    stat, p = stats.wilcoxon(group1, group2)
    print(f"Wilcoxon Testi: W={stat}, p={p}")

def kruskal_wallis_test(group1, group2, group3):
    stat, p = stats.kruskal(group1, group2, group3)
    print(f"Kruskal-Wallis Testi: H={stat}, p={p}")

def friedman_test(group1, group2, group3):
    stat, p = stats.friedmanchisquare(group1, group2, group3)
    print(f"Friedman Testi: Q={stat}, p={p}")


# Testleri çalıştır
mann_whitney_test(group1, group2)
wilcoxon_test(group1, group2)
kruskal_wallis_test(group1, group2, group3)
friedman_test(group1, group2, group3)

