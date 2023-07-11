"""
Bu kod, Python'da çoklu iş parçacığı (thread) kullanarak eşzamanlı çalışmayı göstermektedir.
İki fonksiyon tanımlanır: "do_this" ve "do_that".
İş parçacıkları oluşturulur, her biri bir fonksiyonu hedef alır ve başlatılır.
Fonksiyonlar eşzamanlı olarak çalışırken, beklemeleri sırasında diğer iş parçacığı da çalışır.
Sonuç olarak, başlangıç mesajları hemen ardından yazdırılır, fonksiyonlar belirli süreler boyunca bekler ve sonuç mesajları sırasıyla yazdırılır.
Bu kullanım, paralel işleme imkan tanır ve kodun daha hızlı tamamlanmasını sağlar.
"""

import time
from threading import Thread

def do_this():
    print('Starting this!')
    time.sleep(2)
    print('Did this!')

def do_that():
    print('Starting that')
    time.sleep(3)
    print('Did that')

#do_this()
#do_that()

t1 = Thread(target=do_this)
t1.start()

t2=Thread(target=do_that)
t2.start()