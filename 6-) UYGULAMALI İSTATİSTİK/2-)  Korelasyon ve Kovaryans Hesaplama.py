import numpy as np
import pandas as pd

# Örnek veri
np.random.seed(42)
x = np.random.randint(10, 100, 10)
y = np.random.randint(10, 100, 10)

# Veri çerçevesi oluştur
df = pd.DataFrame({"X": x, "Y": y})

# Korelasyon ve kovaryans hesapla
correlation = df.corr()
covariance = df.cov()

print("Korelasyon Matrisi:\n", correlation)
print("\nKovaryans Matrisi:\n", covariance)
