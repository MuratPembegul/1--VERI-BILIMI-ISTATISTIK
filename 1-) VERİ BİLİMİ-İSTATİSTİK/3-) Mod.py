from statistics import mode

# Bir veri seti tanımlayalım
veri = [10, 20, 20, 30, 30, 30, 40, 50]

# Modu hesaplayalım
try:
    mod = mode(veri)
    print("Veri setinin modu:", mod)
except:
    print("Veri setinde mod bulunmuyor veya çoklu mod var.")

Sonuç : 30