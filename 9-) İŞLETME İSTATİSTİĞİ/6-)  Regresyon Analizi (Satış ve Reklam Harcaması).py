import numpy as np
import statsmodels.api as sm

# Örnek veri (Reklam bütçesi ve satışlar)
X = np.array([500, 700, 800, 900, 1200])
y = np.array([10, 15, 18, 20, 25])

# Sabit terim ekleme
X = sm.add_constant(X)

# Modeli oluştur ve eğit
model = sm.OLS(y, X).fit()

# Sonuçları yazdır
print(model.summary())
