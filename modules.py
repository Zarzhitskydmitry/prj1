
print("=========================================================================================\nРабота с функциями\n=========================================================================================\n")

def privetstvie():                                                                  # Создаем функцию через def, они задаются в начале программы или выносятся в отдельный
    """Privet moy dorogoy drug"""
    print("Privet moy dorogoy drug!")
    print("Chem segodnya zaymemsya")
    print("======================================\n")      
privetstvie()                                                                       # Для вызова этой функции используем его название

def kak_dela(name):                                                                 # Можно подставить переменную для связки с функцией
    print(name+ " kak tvoi dela?")
kak_dela("Dmitriy")

def summa(x, y):                                                                    # Так же можно считать числа которые были посланны для функции
    print(x+y)   
summa(10, 20)

def delenie(x, y):
    z = x / y
    return z                                                                        # для работы вычесления нужно вернуть значение
per01=delenie(35, 5)    
print (per01)

def factorial(x):
    """Calculate factorial"""
    otvet = 1                                                                       # Задаем 1 для начала счета факториала т.к. факториал 1 или 0 равен 1
    for i in range(1, x+1):                                                         # в промежутке range для x прибавляем +1 потому что счет идет с 0
        otvet = otvet * i
    return otvet 
print(factorial(0))

for i in range(4, 20):                                                              # Вызовем цикл факториалов
    print("Factorial chisla "+ str(i) + "! = "+ str(factorial(i)))                  # цикл промежутка числа i от 4 до 20, посчитать факториал этого числа i
    
def users(name, email, phone):
    record_user = {                                                                 # так же можно функции задать объект
        'name' : name,
        'email': email,
        'phone': phone,
    }    
    return record_user
user1 = users('Petya', 'pet1995@yandex.ru', '+932945367')
user2 = users('Andrey', 'and1997@yandex.ru', '+7932945367')
user3 = users('Anna', 'annet@mail.ru', '+3453645367')
print(str(user1) + "\n" + str(user2) + "\n" + str(user3))

def awards(medal, *persons):                                                        # звездочка(*) перед persons означает что их много будет в функции
    for person in persons:
        print("Medaliyu " + medal.upper() + " nagrazhdaetsya " + person.title())
awards("Za otvagu", "Petya", "Vasya", "Masha")
print("=========================================================================================\nEND\n=========================================================================================\n")
