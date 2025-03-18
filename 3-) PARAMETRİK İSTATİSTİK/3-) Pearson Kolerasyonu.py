import scipy.stats as stats
import numpy as np

# Rastgele iki değişken oluştur
np.random.seed(42)
x = np.random.normal(50, 10, 30)
y = x + np.random.normal(0, 5, 30)  # x ile ilişkili bir y oluşturduk

# Korelasyon hesapla
corr_coef, p_value = stats.pearsonr(x, y)

print(f"Korelasyon Katsayısı: {corr_coef:.3f}")
print(f"p-değeri: {p_value:.3f}")

if p_value < 0.05:
    print("İki değişken arasında anlamlı bir ilişki var.")
else:
    print("İki değişken arasında anlamlı bir ilişki yok.")
