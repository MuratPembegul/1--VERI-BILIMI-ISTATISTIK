import numpy as np
import scipy.stats as stats

# Örnek veri
data = [12, 15, 14, 10, 13, 17, 16, 15, 14, 13]

# Ortalama ve standart hata
mean = np.mean(data)
std_error = stats.sem(data)  # Standart hata

# %95 güven aralığı hesaplama
confidence_interval = stats.t.interval(0.95, len(data)-1, loc=mean, scale=std_error)

print("Ortalama:", mean)
print("Güven Aralığı (%95):", confidence_interval)
