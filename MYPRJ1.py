import math                                                             # Импортириуем библиотеку математических вычислений

print("Работа с числами\n---------------------------------\n")
a = 2
b = 28
print (a + b)
c = (a*2+b/b)
print (c)
d= c+15
print (d)
print (math.sqrt(d))                                                    # Вычисляем квадратный корень с помощью библиотеки math
print (math.sin(d))                                                     # Вычисляем синус с помощью библиотеки math
print("END\n---------------------------------\n")

print("Работа со строчками\n---------------------------------\n")
f_name="Dmitry"
s_name="Zarzhitsky"
t_name="aleksanrovich"
full_name=(f_name + ' ' + s_name + ' '+ t_name)
print(f_name + ' ' + s_name + ' ' + t_name)
print(f_name + ' ' + s_name + ' ' + t_name.title())                     # Все начинаются с заглавной
print(full_name.upper())                                                # Все заглавные
print(full_name.lower())                                                # Все строчные
trash="     |     ghdu Denis huev.,.,        |       "
print(trash)
print(trash.rstrip())                                                   # Удалить пробелы справа
print(trash.lstrip())                                                   # Удалить пробелы слева
print(trash.strip())                                                    # Удалить пробелы с двух сторон
print(trash.strip(" " + "|" + "," + "." + "huev" + "ghdu"))             # Удалить контент в выводе
print("END\n---------------------------------\n")

print("Работа вывод строк и чисел\n---------------------------------\n")
print(str(a)+f_name)                                                    # связать цифры с именем
e=(str(a) + "_" + s_name)
print(e)
print("END\n---------------------------------\n")

print("Работа с циклами\n---------------------------------\n")
for per01 in range(0,6):                                                # Вывести от нуля до шести (в range) для per01
    print(b)
    print(per01)
print ("END")
for per02 in range(-50,3,4):                                            # Вывести от -5 до 3 с шагом 4 (в range) для per02
    print("Number x="+ str(per02))
    if per02 == -10:                                                    # если per02 будет точно равна -40
        print("END_of_loop")
        break                                                           # Остановить программу
per03=1
while True:                                                             # Запустить и продолжить цикл пока True
    print(per03)
    per03+=1                                                            # К переменной per03 прибавлять 1

print("END\n---------------------------------\n")

