import scipy.stats as stats
import numpy as np

# Rastgele iki grup oluştur
np.random.seed(42)
grup1 = np.random.normal(50, 10, 30)  # Ortalama 50, standart sapma 10, 30 örnek
grup2 = np.random.normal(55, 10, 30)  # Ortalama 55, standart sapma 10, 30 örnek

# İki grup için t-testini uygula
t_stat, p_value = stats.ttest_ind(grup1, grup2)

print(f"t-istatistiği: {t_stat:.3f}")
print(f"p-değeri: {p_value:.3f}")

# Sonucu yorumlayalım
if p_value < 0.05:
    print("Gruplar arasında anlamlı bir fark var.")
else:
    print("Gruplar arasında anlamlı bir fark yok.")
