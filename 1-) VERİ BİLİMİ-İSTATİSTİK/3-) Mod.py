""" MOD NEDİR?
Mod, bir veri setindeki en sık tekrarlanan değerdir. İstatistikte, veri setinin en yaygın değerini bulmak için kullanılır. 
Mod, veri setindeki en yüksek frekansa sahip değeri temsil eder. Eğer veri setinde her değer bir kez tekrarlanıyorsa, mod yoktur. 
Mod, özellikle nominal (kategorik) verilerde en sık görülen kategoriyi belirlemek için kullanışlıdır.
"""
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
