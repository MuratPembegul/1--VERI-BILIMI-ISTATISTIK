from statistics import variance

# Bir veri seti tanımlayalım
veri = [10, 20, 20, 30, 30, 30, 40, 50]

# Varyansı hesaplayalım
try:
    varyans = variance(veri)
    print("Veri setinin varyansi:", varyans)
except:
    print("Varyans hesaplanamadi.")

Sonuç: 155.35714285714286