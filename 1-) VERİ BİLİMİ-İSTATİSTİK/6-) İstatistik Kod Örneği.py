import numpy as np
from scipy import stats

# Örnek veri
data = [10, 15, 14, 16, 17, 15, 16, 19, 20, 17, 15, 16, 16]

# Ortalama (Mean)
mean = np.mean(data)
print("Ortalama:", mean)

# Medyan (Median)
median = np.median(data)
print("Medyan:", median)

# Mod (Mode)
mode_result = stats.mode(data, keepdims=True)
print("Mod:", mode_result.mode[0], "- Frekans:", mode_result.count[0])

# Varyans (Variance)
variance = np.var(data)
print("Varyans:", variance)

# Standart Sapma (Standard Deviation)
std_dev = np.std(data)
print("Standart Sapma:", std_dev)

Ortalama: 15.846153846153847
Medyan: 16.0
Mod: 16  
Frekans: 4
Varyans: 5.360946745562131
StandartSapma: 2.315371837429602


