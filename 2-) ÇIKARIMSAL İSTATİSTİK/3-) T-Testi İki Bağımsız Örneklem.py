# İki bağımsız örneklem verisi
group1 = np.random.normal(loc=50, scale=10, size=100)  # Grup 1
group2 = np.random.normal(loc=55, scale=10, size=100)  # Grup 2

# T testi
t_stat, p_value = stats.ttest_ind(group1, group2)

print(f"T-Statistiği: {t_stat}")
print(f"P-Değeri: {p_value}")
