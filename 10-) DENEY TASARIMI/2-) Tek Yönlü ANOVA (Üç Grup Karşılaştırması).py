import scipy.stats as stats

# Üç farklı grup için veri (Satış kampanyaları)
kampanya_A = [120, 130, 125, 140, 135]
kampanya_B = [150, 160, 155, 145, 170]
kampanya_C = [100, 110, 105, 115, 120]

# ANOVA testi
f_stat, p_value = stats.f_oneway(kampanya_A, kampanya_B, kampanya_C)

print(f"F-İstatistiği: {f_stat:.4f}, P-Değeri: {p_value:.4f}")

if p_value < 0.05:
    print("Sonuç: Gruplar arasında anlamlı fark var.")
else:
    print("Sonuç: Gruplar arasında anlamlı fark yok.")
