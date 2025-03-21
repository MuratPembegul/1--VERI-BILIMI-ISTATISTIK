import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Bernoulli Dağılımı
p = 0.5  # Başarı olasılığı
bernoulli_rv = stats.bernoulli(p)
bernoulli_samples = bernoulli_rv.rvs(size=1000)

plt.figure(figsize=(5, 3))
sns.histplot(bernoulli_samples, bins=2, discrete=True, stat="probability")
plt.title("Bernoulli Dağılımı (p=0.5)")
plt.show()

# 2. Binom Dağılımı
n, p = 10, 0.5
binom_rv = stats.binom(n, p)
x = np.arange(0, n+1)
plt.bar(x, binom_rv.pmf(x))
plt.title("Binom Dağılımı (n=10, p=0.5)")
plt.show()

# 3. Poisson Dağılımı
lambda_ = 3
poisson_rv = stats.poisson(lambda_)
x = np.arange(0, 15)
plt.bar(x, poisson_rv.pmf(x))
plt.title("Poisson Dağılımı (λ=3)")
plt.show()

# 4. Normal Dağılım
mu, sigma = 0, 1
x = np.linspace(-4, 4, 1000)
y = stats.norm.pdf(x, mu, sigma)
plt.plot(x, y)
plt.title("Normal Dağılım (μ=0, σ=1)")
plt.show()

# 5. Merkezi Limit Teoremi Simülasyonu
sample_size = 30
num_samples = 1000
samples = np.mean(np.random.exponential(scale=2, size=(num_samples, sample_size)), axis=1)
sns.histplot(samples, kde=True, bins=30)
plt.title("Merkezi Limit Teoremi Simülasyonu")
plt.show()

# 6. Ki-Kare Testi
observed = np.array([50, 30, 20])  # Gözlenen değerler
expected = np.array([40, 40, 20])  # Beklenen değerler
chi2_stat, p_value = stats.chisquare(observed, expected)
print(f"Ki-Kare Testi: Test istatistiği = {chi2_stat:.2f}, p-değeri = {p_value:.4f}")
