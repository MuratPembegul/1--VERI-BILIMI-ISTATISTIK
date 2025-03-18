import scipy.stats as stats
import numpy as np

# Rastgele 3 grup oluştur
np.random.seed(42)
grup1 = np.random.normal(50, 10, 30)
grup2 = np.random.normal(55, 10, 30)
grup3 = np.random.normal(60, 10, 30)

# ANOVA testi uygula
f_stat, p_value = stats.f_oneway(grup1, grup2, grup3)

print(f"F-istatistiği: {f_stat:.3f}")
print(f"p-değeri: {p_value:.3f}")

if p_value < 0.05:
    print("Gruplar arasında anlamlı fark var.")
else:
    print("Gruplar arasında anlamlı fark yok.")
