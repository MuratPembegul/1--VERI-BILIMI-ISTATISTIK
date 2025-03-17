# Bir veri seti tanımlayalım
veri = [10, 20, 30, 40, 50]

# Veriyi sıralayalım
veri.sort()

# Veri setindeki eleman sayısını bulalım
n = len(veri)

# Eğer eleman sayısı tekse, ortadaki değeri seçelim
if n % 2 == 1:
    medyan = veri[n // 2]
# Eğer eleman sayısı çiftse, ortadaki iki değerin ortalamasını alalım
else:
    medyan = (veri[(n // 2) - 1] + veri[n // 2]) / 2

# Sonucu ekrana yazdıralım
print("Veri setinin medyani:", medyan)

Çikti: 30