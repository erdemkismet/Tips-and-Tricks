'''
Bu kod, "functools" modülünden "lru_cache" adlı bir dekoratör kullanılarak "increment" adında bir fonksiyon tanımlanmıştır.
"lru_cache" dekoratörü, önbelleğe alma (caching) işlemini gerçekleştirerek fonksiyonun tekrar tekrar çalıştırılmasını engeller
 ve daha hızlı bir şekilde sonuç döndürür.

"increment" fonksiyonu, bir sayıyı alır ve bu sayıyı 1 artırarak geri döndürür. Fonksiyonun içinde "Running 1000 lines of code" mesajı yazdırılır.
Ancak, fonksiyonun sonucu daha önce verilmişse, yani aynı giriş daha önce çağrılmışsa, fonksiyon tekrar çalıştırılmaz ve sonuç önbellekten alınır.

Kodun geri kalanında, "increment" fonksiyonu farklı parametrelerle çağrılır ve sonuçlar ekrana yazdırılır. 
İlk üç çağrıda "Running 1000 lines of code" mesajı her defasında yazdırılır çünkü bu girişler daha önce çağrılmamıştır.
Ancak, son çağrıda aynı giriş tekrar kullanıldığından, fonksiyon tekrar çalıştırılmaz ve sonuç önbellekten alınır. 
Bu sayede, kodun performansı artar ve gereksiz hesaplamaların önüne geçilir.
'''


from functools import lru_cache

#lru = "least recently used"
@lru_cache 
def increment(num):
    print('Running 1000 lines of code')
    return num+1

print(increment(1))
print(increment(2))
print(increment(3))
print(increment(1))