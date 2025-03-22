import pandas as pd

# Ürün ve yıllık satış miktarları
data = {'Ürün': ['A', 'B', 'C', 'D', 'E'], 'Satış': [5000, 1200, 800, 500, 300]}
df = pd.DataFrame(data)

# Satışları büyükten küçüğe sırala
df = df.sort_values(by='Satış', ascending=False)

# Kümülatif yüzde hesaplama
df['Kümülatif %'] = df['Satış'].cumsum() / df['Satış'].sum() * 100

# ABC sınıflandırması
df['Kategori'] = df['Kümülatif %'].apply(lambda x: 'A' if x <= 70 else ('B' if x <= 90 else 'C'))

print(df)
