import numpy as np
import scipy.stats as stats

# A ve B seçeneklerinin başarı oranları
A_başarı = 30
A_toplam = 100
B_başarı = 25
B_toplam = 100

# Beta dağılımı (Bayesçi olasılık dağılımı)
A_posterior = stats.beta(A_başarı + 1, A_toplam - A_başarı + 1)
B_posterior = stats.beta(B_başarı + 1, B_toplam - B_başarı + 1)

# Rastgele örnekler alarak hangisinin daha iyi olduğunu tahmin et
A_örnekler = A_posterior.rvs(10000)
B_örnekler = B_posterior.rvs(10000)

# A seçeneğinin B'den daha iyi olma olasılığı
A_daha_iyi = np.mean(A_örnekler > B_örnekler)

print(f"A seçeneğinin B'den daha iyi olma olasılığı: {A_daha_iyi:.2%}")
