import numpy as np
import scipy.stats as stats
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Temel Tanımlayıcı İstatistikler
data = np.random.normal(loc=50, scale=10, size=100)
print("Ortalama:", np.mean(data))
print("Medyan:", np.median(data))
print("Varyans:", np.var(data))
print("Standart Sapma:", np.std(data))

# 2. T-Testi (Bağımsız Örneklem)
data1 = np.random.normal(50, 10, 30)
data2 = np.random.normal(55, 10, 30)
t_stat, p_value = stats.ttest_ind(data1, data2)
print(f"T-Testi: t={t_stat:.2f}, p={p_value:.4f}")

# 3. ANOVA (Varyans Analizi)
group1 = np.random.normal(50, 10, 30)
group2 = np.random.normal(55, 10, 30)
group3 = np.random.normal(60, 10, 30)
anova_stat, anova_p = stats.f_oneway(group1, group2, group3)
print(f"ANOVA Testi: F={anova_stat:.2f}, p={anova_p:.4f}")

# 4. Korelasyon Analizi
data_x = np.random.normal(50, 10, 100)
data_y = data_x + np.random.normal(0, 5, 100)
corr_coeff, corr_p = stats.pearsonr(data_x, data_y)
print(f"Pearson Korelasyon Katsayısı: r={corr_coeff:.2f}, p={corr_p:.4f}")

# 5. Lojistik Regresyon
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

df = pd.DataFrame({
    'yaş': np.random.randint(20, 60, 100),
    'kolesterol': np.random.randint(150, 250, 100),
    'hastalık': np.random.randint(0, 2, 100)
})
X = df[['yaş', 'kolesterol']]
y = df['hastalık']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LogisticRegression()
model.fit(X_train, y_train)
preds = model.predict(X_test)
print("Lojistik Regresyon Doğruluk:", accuracy_score(y_test, preds))

# 6. Kaplan-Meier Sağkalım Analizi
from lifelines import KaplanMeierFitter

df_survival = pd.DataFrame({
    'süre': np.random.exponential(365, 100),
    'durum': np.random.randint(0, 2, 100)
})
kmf = KaplanMeierFitter()
kmf.fit(df_survival['süre'], event_observed=df_survival['durum'])
kmf.plot_survival_function()
plt.title("Kaplan-Meier Sağkalım Eğrisi")
plt.show()
