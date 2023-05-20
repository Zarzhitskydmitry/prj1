import math                                                             # Импортириуем библиотеку математических вычислений

print("=========================================================================================\nРабота с числами\n=========================================================================================\n")
a = 2
b = 28
print (a + b)
c = (a*2+b/b)
print (c)
d= c+15
print (d)
print (math.sqrt(d))                                                    # Вычисляем квадратный корень с помощью библиотеки math
print (math.sin(d))                                                     # Вычисляем синус с помощью библиотеки math
print("=========================================================================================\nEND\n=========================================================================================\n")

print("=========================================================================================\nРабота со строчками\n=========================================================================================\n")
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
print(str(a)+f_name)                                                    # связать цифры с именем
e=(str(a) + "_" + s_name)
print(e)
print("=========================================================================================\nEND\n=========================================================================================\n")

print("=========================================================================================\nРабота с циклами\n=========================================================================================\n")
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
# == точно равно, != не равно, <= меньше или равно, >= больше или равно
    if per03 == 10:                                                      # если per03 не равна, то остановить
        print("END_of_loop")
        break
print("=========================================================================================\nEND\n=========================================================================================\n")

print("=========================================================================================\nРабота с массивами\n=========================================================================================\n")

cities = [ 'Kazan','Kiev', 'New York','Izhevsk', 'Sankt-Petersburg', 'Moscow', 'Perm']     # Создаем массив значений  
print(cities)                                                           # Вывод всех значений в массиве
print(len(cities))                                                      # Вывод количества значений в массиве
print(cities [0])                                                       # Вывод значения в массиве, по его порядковому номеру начиная с 0. 
# Также можно использовать отрицательный порядок для вывода с конца массива
mycities = cities[3:6]                                                  # вывести из массива с индекса 3 по 6 не включая 6 значение
print(mycities)
mycities = cities[-5:-1]
print(mycities)
print(cities [-2].upper())
mynumber_list = list(range(0, 14))                                      # задать массив из чисел в промежутке(range) от 0 до 14
print(mynumber_list)
cities [4] = 'Ekaterinburg'                                             # Заменить в массиве значение
print(cities) 
cities.append ('Glazov')                                                # Добавить в конец массива значение
print(cities)
cities.insert (2, 'Uva')                                                # Добавить в массив значение внутри перед порядковым номером 2
print(cities)
del cities [-3]                                                         # Удалить из массива значение порядкового номера 3 с конца
for per05 in cities:
    print (per05.lower())                                               # можно использовать for для вывод значений в троку, также применяя форматирование
new_cities = [per04.upper() for per04 in cities]                        # Новая переменная, что для каждого значения в массиве применить форматирование ЗАГЛВАНЫЕ
print(new_cities)
cities.remove('Kazan')                                                  # Удалить значение из массива
print(cities)
del_cities = cities.pop()                                               # Метод pop удаляет элемент по индексу, а если не назначен, то с конца и возвращает его
print("Удалили: "+del_cities)
print(cities)
cities.sort()                                                           # Сортирует массив по наименованию
print(cities)
# так же можно указать сортировку в обратном порядке с помощью cities.sort(reverse=True) или указать вместо сорт cities.reverse()
mynumber_list.sort(reverse=True)
print(mynumber_list)
print(max(mynumber_list))                                               # Найти в массиве самое большое число
print(min(mynumber_list))                                               # Найти в массиве самое маленькое число
print(sum(mynumber_list))                                               # Найти сумму массива
mynumber_list2 = mynumber_list[:]                                       # [:] отделяет массивы по их памяти
mynumber_list2 = ['Mozhga', mynumber_list]
print(mynumber_list2)
print(mynumber_list)
print("=========================================================================================\nEND\n=========================================================================================\n")

print("=========================================================================================\nРабота с условными операторами\n=========================================================================================\n")
per06 = 20
if per06 == 24:                                                         # Если переменная per06 точно равна 24 то напечатать("YES you right")
    print("YES you right")
else:
    print("NO you are wrong")                                           # Иначе ("NO you are wrong") 
if (per06 <= 18):                                                       # Если переменная меньше или равна 18, то ("Ты слишком молод")
    print ("Ты слишком молод")
elif (per06 >=19) and (per06 < 20):                                     # и если переменная больше или равна 19 и меньше или равна 21, то ("you teenager")
    print ("you teenager")
else:
    print("You are old")                                                # Иначе ("You are old") 
cities = [ 'Kazan','Kiev', 'New York','Izhevsk', 'Sankt-Petersburg', 'Moscow', 'Perm']
mycities = ['Izhevsk']
if 'Izhevsk' in cities:                                                 # Если город Ижевск есть в массиве cities, то напечатать 
    print("my city if:"+ str(mycities))
else:
    print("this city is not my")
for xxxx in cities:                                                     # For проверяет каждое значение в массиве cities
    if xxxx in mycities:                                                # если в массиве cities есть mycities, то напечатать (xxxx+" - Is my city")
        print (xxxx+" - Is my city")
    else:
        print(xxxx+" - Not my city")                                    # Иначе (xxxx+" - Not my city")
print("=========================================================================================\nEND\n=========================================================================================\n")

print("=========================================================================================\nРабота со словарями/объектами\n=========================================================================================\n")
enemy = {                                                               # создаем объект enemy с его параметрами/свойтсвами
    'health': 100,
    'armor': 100,
    'strange': 40,
    'intelenge': 10,
    'color': 'green',
    'name': 'Browser',
    'awards': ['Perviy', 'Vtoroy', 'etc'],                              # можно добавить массив из значений
    'image': ['iamge1.png', 'image2.png', 'iamge3.png', 'image4.png'],
}
print(enemy)
print(enemy.keys())                                                     # Вывести название параметров
print(enemy.values())                                                   # Вывести значение параметров
print("Health enemy: "+str(enemy['health']))                            # вывести отдельный параметр enemy
print("Name enemy: "+enemy['name'])                                     # вывести отдельный параметр enemy
enemy['rank'] = 'silver'                                                # добавить еще параметр enemy
print(enemy)
del enemy ['intelenge']                                                 # удаляем параметр
print(enemy)
enemy['armor'] = enemy['armor'] - 20                                    # вычесть из параметра 
enemy['health'] = enemy['health'] - 40
if enemy['health'] <= 65:
    enemy['color'] = 'yellow'
print(enemy)
print ("END")
all_enemies = []                                                        # создаем массив из enemy
for x_enemy in range(0,4):                                              # создает цикл от 0 до 4
    all_enemies.append(enemy)                                           # делает добавление enemy в массив all_enemies(Создаются клоны)
for for_enemies in all_enemies:                                         # выведем построчно каждого enemy
    print(for_enemies)
print('=========================================')
enemy2 = {                                                               # создаем объект enemy2 с его параметрами/свойтсвами
    'health': 100,
    'armor': 100,
    'strange': 40,
    'intelenge': 10,
    'color': 'green',
    'name': 'Browser',
    'awards': ['Perviy', 'Vtoroy', 'etc'],                              # можно добавить массив из значений
    'image': ['iamge1.png', 'image2.png', 'iamge3.png', 'image4.png'],
}
all2_enemies = []
for y_enemy in range(0,6):                                              # создает цикл от 0 до 4 
    all2_enemies.append(enemy2.copy())                                  # делает добавление enemy в массив all2_enemies(Создаются копии со своими параметрами)
for for2_enemies in all2_enemies:                                       # выведем построчно каждого enemy2
    print(for2_enemies)
print('========================================')
all2_enemies[3]['health'] += -40                                        # счет идет с 0 индекса
for for3_enemies in all2_enemies:                                       # выведем построчно каждого enemy2
    print(for3_enemies)
print("=========================================================================================\nEND\n=========================================================================================\n")

print("=========================================================================================\nРабота с вводом данных\n=========================================================================================\n")
per_old = input ("Vvedite vash vozrast: ")                              # создаем переменную которую введет пользователь
per_name = input ("Vvedite vashe imya: ")                                        
if (int(per_old) <= 18):                                                # Введенные числа нужно конвертировать в числа int чтобы их сравнивать или складывать                                            
    print ("Privet - " + per_name + " " + str(per_old) + " you are kid")
elif (int(per_old) >=19) and (int(per_old) < 20):                                 
    print ("Privet - " + per_name + " "  + str(per_old) + " you are teenager")
else:
    print("Privet - " + per_name + " " + str(per_old) + " you are old")
message01 = ''
while True:                                                             # создаем цикл ввода слова до тех пор пока пользователь не введет sekret
    message01 = input ("Enter your password ")  
    if message01 == 'sekret':
        print("succes")
        break
    else:
        print(message01 + "\nPassword is not correct")
mylist01 = []
msg = ''
while msg != 'STOP':
    msg = input("\nEnter new item or STOP for finish\n") 
    mylist01.append(msg)
print("=====================")
mylist01.remove('STOP')
print(mylist01)                                            
print("=========================================================================================\nEND\n=========================================================================================\n")
