"""
Bu kodda, kullanıcıya "Do this or that?" şeklinde bir giriş yapılması beklenir. 
Kullanıcının verdiği giriş, "match" ifadesiyle karşılaştırılır. 
Eğer giriş "this" ise, "do_this()" fonksiyonu çağrılır ve "Doing this" mesajı yazdırılır. 
Eğer giriş "that" ise, "do_that()" fonksiyonu çağrılır ve "Doing that" mesajı yazdırılır. 
Eğer giriş herhangi bir duruma uymuyorsa (yani "_" durumu), "Invalid input!" mesajı yazdırılır. 
Bu kod, kullanıcının girişine bağlı olarak "do_this()" veya "do_that()" fonksiyonlarının çalıştırılmasını sağlar 
ve geçersiz bir giriş durumunda kullanıcıya bir hata mesajı verir.
"""

def do_this():
    print('Doing this')

def do_that():
    print("Doing that")

match input('Do this or that? '):
    case 'this':
        do_this()
    case 'that':
        do_that()
    case _:
        print('Invalid input!')
