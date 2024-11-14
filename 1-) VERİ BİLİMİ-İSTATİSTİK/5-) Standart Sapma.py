""" STANDART SAPMA NEDİR?
Standart sapma, bir veri setindeki değerlerin ortalamadan ne kadar sapma gösterdiğini, yani yayılımını ölçen bir istatistiksel ölçüdür. 
Standart sapma, varyansın kareköküdür ve daha çok kullanılan bir yayılma ölçüsüdür çünkü verilerle aynı birime sahiptir. 
Standart sapma küçükse, veriler ortalamaya yakın; büyükse, veriler ortalamadan uzak dağılmış demektir.
"""
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
