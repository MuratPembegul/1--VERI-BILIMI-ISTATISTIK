def bayes_teoremi(prior, likelihood, marginal_likelihood):
    """
    Bayes Teoremini hesaplar.
    prior: Önsel olasılık (P(A))
    likelihood: Veriye göre koşullu olasılık (P(B|A))
    marginal_likelihood: Bütün olayların toplam olasılığı (P(B))
    """
    posterior = (prior * likelihood) / marginal_likelihood
    return posterior

# Örnek kullanım:
prior = 0.01  # Hastalık taşıma olasılığı
likelihood = 0.9  # Testin doğru pozitif verme olasılığı
marginal_likelihood = 0.1  # Testin pozitif çıkma olasılığı

sonuc = bayes_teoremi(prior, likelihood, marginal_likelihood)
print(f"Bayes Teoremi Sonucu: {sonuc:.4f}")
