# Üç farklı grup verisi
group1 = np.random.normal(loc=50, scale=10, size=100)
group2 = np.random.normal(loc=55, scale=10, size=100)
group3 = np.random.normal(loc=60, scale=10, size=100)

# Tek yönlü ANOVA testi
f_stat, p_value = stats.f_oneway(group1, group2, group3)

print(f"F-Statistiği: {f_stat}")
print(f"P-Değeri: {p_value}")
