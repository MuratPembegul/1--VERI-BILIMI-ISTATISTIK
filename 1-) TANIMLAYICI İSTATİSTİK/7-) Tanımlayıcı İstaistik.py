import pandas as pd

# Örnek veri seti (data.csv) okuma
data = pd.read_csv('data.csv')  # Burada kendi veri dosyanızı kullanabilirsiniz.

# Tanımlayıcı istatistiksel özet
descriptive_stats = data.describe()  # Bu komut temel istatistiksel özetleri verir

# Sonuçları yazdırma
print("Tanımlayıcı İstatistiksel Özet:")
print(descriptive_stats)

# Ayrıca her sütunun ortalama, medyan, vb. istatistiklerini ayrı ayrı yazdırmak da mümkün:
mean = data.mean()
median = data.median()
std_dev = data.std()
min_values = data.min()
max_values = data.max()

print("\nOrtalama Değerler:")
print(mean)
print("\nMedyan Değerler:")
print(median)
print("\nStandart Sapma Değerleri:")
print(std_dev)
print("\nMinimum Değerler:")
print(min_values)
print("\nMaksimum Değerler:")
print(max_values)
