import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

# Faktöriyel tasarım: Fiyat (Düşük/Yüksek) ve Reklam (Az/Çok)
data = pd.DataFrame({
    'Fiyat': ['Düşük', 'Düşük', 'Yüksek', 'Yüksek', 'Düşük', 'Düşük', 'Yüksek', 'Yüksek'],
    'Reklam': ['Az', 'Çok', 'Az', 'Çok', 'Az', 'Çok', 'Az', 'Çok'],
    'Satış': [200, 250, 180, 220, 210, 260, 190, 230]
})

# Faktöriyel ANOVA modeli
model = ols('Satış ~ C(Fiyat) + C(Reklam) + C(Fiyat):C(Reklam)', data=data).fit()
anova_table = sm.stats.anova_lm(model, typ=2)

print(anova_table)
