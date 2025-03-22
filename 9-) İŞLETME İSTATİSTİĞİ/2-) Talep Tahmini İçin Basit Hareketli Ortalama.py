import numpy as np

# Talep verisi
talep = [120, 130, 125, 140, 150, 160, 155]

# 3 periyotluk hareketli ortalama
N = 3
hareketli_ortalama = np.convolve(talep, np.ones(N)/N, mode='valid')
print(hareketli_ortalama)
