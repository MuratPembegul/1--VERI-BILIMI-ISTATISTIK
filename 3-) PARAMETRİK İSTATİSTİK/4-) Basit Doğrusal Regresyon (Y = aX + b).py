import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Rastgele veri oluştur
np.random.seed(42)
x = np.random.rand(50, 1) * 10  # 0 ile 10 arasında rastgele x değerleri
y = 2.5 * x + 5 + np.random.randn(50, 1) * 2  # Doğrusal bir ilişki

# Modeli oluştur ve eğit
model = LinearRegression()
model.fit(x, y)

# Tahmin yap
y_pred = model.predict(x)

# Grafiği çiz
plt.scatter(x, y, color="blue", label="Gerçek Veriler")
plt.plot(x, y_pred, color="red", linewidth=2, label="Regresyon Çizgisi")
plt.xlabel("Bağımsız Değişken (X)")
plt.ylabel("Bağımlı Değişken (Y)")
plt.legend()
plt.show()
