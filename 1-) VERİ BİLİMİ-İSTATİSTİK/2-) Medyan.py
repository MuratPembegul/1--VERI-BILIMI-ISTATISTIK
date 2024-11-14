""" MEDYAN NEDİR?
Medyan, bir veri setindeki ortanca değeri ifade eder. 
Bir veri setindeki sayılar küçükten büyüğe sıralandıktan sonra, ortadaki sayı medyan olarak adlandırılır. 
Eğer veri setindeki eleman sayısı tek ise ortadaki değer doğrudan medyan olur. 
Ancak eleman sayısı çift ise, ortadaki iki sayının aritmetik ortalaması medyan olarak alınır. 
Medyan, özellikle uç değerlerin (aşırı büyük ya da küçük değerlerin) veri setindeki etkisini azaltmak için kullanılır, 
çünkü bu tür uç değerler aritmetik ortalamayı çarpıtabilir.
"""
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

Sonuç: 30
