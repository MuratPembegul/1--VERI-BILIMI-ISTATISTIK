from sklearn.naive_bayes import GaussianNB
import numpy as np

# Örnek veriler (özellikler)
X = np.array([[1.5, 2.3], [2.1, 3.2], [1.1, 0.8], [3.5, 2.7]])
# Sınıflar (0 veya 1)
y = np.array([0, 1, 0, 1])

# Gaussian Naive Bayes modeli oluştur
gnb = GaussianNB()
gnb.fit(X, y)

# Yeni bir örnek tahmin et
yeni_ornek = np.array([[2.0, 2.5]])
tahmin = gnb.predict(yeni_ornek)

print(f"Yeni örneğin tahmini sınıfı: {tahmin[0]}")
