import statsmodels.stats.power as smp

# Parametreler
effect_size = 0.5  # Etki büyüklüğü (Cohen's d)
alpha = 0.05       # Hata payı
power = 0.8        # Test gücü

# Örneklem büyüklüğü hesaplama
sample_size = smp.TTestIndPower().solve_power(effect_size, power=power, alpha=alpha)

print(f"Gerekli Örneklem Büyüklüğü: {round(sample_size)} kişi")
