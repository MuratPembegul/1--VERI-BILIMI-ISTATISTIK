import numpy as np
import scipy.stats as stats

# Örnek veri
data = np.random.normal(loc=50, scale=10, size=100)

# Güven aralığı hesaplama
confidence_level = 0.95
mean = np.mean(data)
std_err = stats.sem(data)  # Standart hata
confidence_interval = stats.t.interval(confidence_level, len(data)-1, loc=mean, scale=std_err)

print(f"{confidence_level*100}% Güven Aralığı: {confidence_interval}")
