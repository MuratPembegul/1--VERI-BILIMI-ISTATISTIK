import scipy.stats as stats
import numpy as np

# Örnek çapraz tablo (Müşteri memnuniyet anketi)
veri = np.array([[50, 30], [20, 40]])

# Ki-kare testi
chi2, p, dof, expected = stats.chi2_contingency(veri)

print(f"Ki-Kare Değeri: {chi2:.2f}, p-değeri: {p:.4f}")
