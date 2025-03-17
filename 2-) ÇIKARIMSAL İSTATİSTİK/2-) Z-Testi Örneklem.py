import numpy as np
from scipy import stats

# Örnek veri (örneklem)
data = np.random.normal(loc=50, scale=10, size=100)  # Ortalama: 50, Standart sapma: 10

# Popülasyon ortalaması
pop_mean = 52

# Z testi
z_stat, p_value = stats.ttest_1samp(data, pop_mean)

print(f"Z-Statistiği: {z_stat}")
print(f"P-Değeri: {p_value}")
