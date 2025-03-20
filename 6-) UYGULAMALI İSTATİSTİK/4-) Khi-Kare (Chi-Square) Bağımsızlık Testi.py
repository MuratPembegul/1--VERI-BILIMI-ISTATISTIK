import numpy as np
import scipy.stats as stats

# Örnek çapraz tablo
observed = np.array([[50, 30], [20, 40]])

# Khi-kare testi
chi2, p, dof, expected = stats.chi2_contingency(observed)

print(f"Khi-Kare Değeri: {chi2}")
print(f"P-Değeri: {p}")
print(f"Beklenen Değerler:\n {expected}")
