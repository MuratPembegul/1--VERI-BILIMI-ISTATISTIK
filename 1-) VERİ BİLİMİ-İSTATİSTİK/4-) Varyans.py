""" VARYANS NEDİR?
Varyans, bir veri setindeki değerlerin ortalamadan ne kadar sapma gösterdiğini ölçer. 
Varyans, veri setinin yayılımını anlamak için kullanılır. Matematiksel olarak, her bir değerin ortalamadan farkının karesi alınarak bu farkların ortalaması hesaplanır. 
Varyans ne kadar büyükse, veriler ortalamadan o kadar uzaklaşmıştır.
"""
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
