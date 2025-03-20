import numpy as np
import pandas as pd

# Örnek veri
data = np.random.randint(10, 100, 20)

# Betimsel istatistikleri hesapla
df = pd.DataFrame(data, columns=["Değerler"])
print(df.describe())  # Pandas'ın hazır betimsel istatistik fonksiyonu

# Manuel hesaplamalar
mean = np.mean(data)
median = np.median(data)
variance = np.var(data, ddof=1)
std_dev = np.std(data, ddof=1)

print(f"Ortalama: {mean}")
print(f"Medyan: {median}")
print(f"Varyans: {variance}")
print(f"Standart Sapma: {std_dev}")
