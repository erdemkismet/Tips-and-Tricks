full_files = [
    'info.txt',
    'image.png',
    'script.c',
    'image2.jpg',
    'info.3.txt'
]

for file in full_files:
    name = '.'.join(file.split('.')[0:-1])
    print(name)

"""
Bu satır, bir dosya adını alır ve nokta karakteri ('.') kullanarak dosya adını noktadan önceki kısmına ayırır. 
Yani, dosya adının sonundaki dosya uzantısını çıkarır. 
Ardından, elde edilen parçaları birleştirerek yeni bir isim oluşturur. 
Bu işlem, dosya adının uzantısını çıkarmak ve sadece dosyanın adını elde etmek için kullanılabilir.
"""