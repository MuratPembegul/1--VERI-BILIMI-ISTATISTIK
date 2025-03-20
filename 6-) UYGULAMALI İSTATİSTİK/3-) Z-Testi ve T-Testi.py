import numpy as np
import scipy.stats as stats

# Örnek veri
np.random.seed(42)
group1 = np.random.normal(50, 10, 30)
group2 = np.random.normal(55, 10, 30)

# Bağımsız iki örneklem t-testi
t_stat, t_pval = stats.ttest_ind(group1, group2)
print(f"T-Testi: t={t_stat:.4f}, p={t_pval:.4f}")

# Z-Testi (Eğer örneklem büyükse kullanılır)
z_stat, z_pval = stats.ranksums(group1, group2)
print(f"Z-Testi: z={z_stat:.4f}, p={z_pval:.4f}")
