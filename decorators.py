"""
Dekoratörler, Python programında işlevsellik eklemek veya değiştirmek için kullanılan bir yapıdır. 
Bir fonksiyonu veya sınıfı dekore etmek, onun davranışını değiştirmek veya ek işlevler eklemek için kullanılabilir. 
Dekoratörler, varolan bir fonksiyonun işlevselliğini korurken, üzerine ekstra kodlar ekleyerek fonksiyonun çalışmasını sarmalar. 
Böylece, kod tekrarını önlemek, işlevsellik eklemek veya fonksiyonun giriş/çıkışlarını değiştirmek gibi amaçlar için kullanılabilirler.
"""
def my_decorator(func):
    def wrapper():
        print(f"Running {func.__name__}")
        func()
        print("Complete")
    return wrapper

@my_decorator
def do_this():
    print('Doing that')

@my_decorator
def do_that():
    print('Doing that')

do_this()
do_that()