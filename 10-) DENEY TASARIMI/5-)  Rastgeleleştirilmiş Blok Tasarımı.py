import statsmodels.api as sm
from statsmodels.formula.api import ols
import pandas as pd

# Veri seti: 3 farklı mağaza ve 3 fiyat seviyesi
data = pd.DataFrame({
    'Mağaza': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C'],
    'Fiyat': ['Düşük', 'Orta', 'Yüksek', 'Düşük', 'Orta', 'Yüksek', 'Düşük', 'Orta', 'Yüksek'],
    'Satış': [150, 130, 110, 170, 140, 120, 160, 135, 115]
})

# ANOVA modeli (Rastgeleleştirilmiş blok tasarımı)
model = ols('Satış ~ C(Mağaza) + C(Fiyat)', data=data).fit()
anova_table = sm.stats.anova_lm(model, typ=2)

print(anova_table)
