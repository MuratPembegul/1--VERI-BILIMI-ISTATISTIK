from statistics import stdev

# Bir veri seti tanımlayalım
veri = [10, 20, 20, 30, 30, 30, 40, 50]

# Standart sapmayı hesaplayalım
try:
    standart_sapma = stdev(veri)
    print("Veri setinin standart sapmasi:", standart_sapma)
except:
    print("Standart sapma hesaplanamadi.")

Sonuç: 12.46423454758225