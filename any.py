enemies = [
    {'type': 'Orc', 'health': 0},
    {'type': 'Orc', 'health': 0},
    {'type': 'Orc', 'health': 4},
    {'type': 'Orc', 'health': 1},
]

if any([enemy['health'] for enemy in enemies]):
    print('The battle is not over!')
else:
    print('No more enemies remain!')

"""
any() fonksiyonu, verilen bir iterable (tekrarlanabilir) nesnenin en az bir doğru (True) değer içerip içermediğini kontrol eder. 
Eğer en az bir doğru değer varsa, any() fonksiyonu True döner. Eğer iterable nesne boş ise, False döner.
"""