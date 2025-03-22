import numpy as np
import scipy.stats as stats

# A ve B grubu verileri (Dönüşüm oranları)
grup_A = np.array([0.12, 0.14, 0.10, 0.13, 0.15, 0.11, 0.13])
grup_B = np.array([0.18, 0.19, 0.17, 0.20, 0.16, 0.21, 0.19])

# Bağımsız iki örneklem t-testi
t_stat, p_value = stats.ttest_ind(grup_A, grup_B)

print(f"T-İstatistiği: {t_stat:.4f}, P-Değeri: {p_value:.4f}")

if p_value < 0.05:
    print("Sonuç: A ve B grupları arasında istatistiksel olarak anlamlı bir fark var.")
else:
    print("Sonuç: A ve B grupları arasında anlamlı bir fark yok.")
