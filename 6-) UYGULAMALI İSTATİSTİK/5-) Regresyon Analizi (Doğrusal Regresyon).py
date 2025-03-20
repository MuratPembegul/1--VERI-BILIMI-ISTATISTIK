import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Örnek veri
np.random.seed(42)
X = np.random.randint(1, 100, 20).reshape(-1, 1)
y = 3 * X.flatten() + np.random.normal(0, 10, 20)

# Model oluştur
model = LinearRegression()
model.fit(X, y)

# Tahmin yap
y_pred = model.predict(X)

# Görselleştirme
plt.scatter(X, y, label="Gerçek Değerler")
plt.plot(X, y_pred, color='red', label="Regresyon Doğrusu")
plt.legend()
plt.xlabel("Bağımsız Değişken")
plt.ylabel("Bağımlı Değişken")
plt.title("Doğrusal Regresyon Analizi")
plt.show()
