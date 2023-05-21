import json
import sys
import os
import re

print("=========================================================================================\nРабота с JSON\n=========================================================================================\n")

filename = 'files/user_settings.txt'                                                            # Называем файл куда будет сохраняться наши настройки
myfile01 = open(filename, mode='w', encoding='utf-8')

player1 = {                                                                                     # Создаем наших игроков
    'PlayerName': 'Nikita',
    'Score': 10,
    'awards': ['First', 'Second', 'Thirty']
}
player2 = {
    'PlayerName': 'Vasya',
    'Score': 15,
    'awards': ['Fifty', 'Sixty', 'Seventy']
}

myplayers = []                                                                                  # Создаем массив из игроков, куда сразу их добавляем
myplayers.append(player1)
myplayers.append(player2)
json.dump(myplayers, myfile01)                                                                  # делаем сохранение myplaers в myfile01
myfile01.close()                                                                                # незабываем закрыть файл

myfile01 = open(filename, mode='r', encoding='utf-8')                                           # Чтобы прочитать нужно снова указать настройки mode
json_data = json.load(myfile01)                                                                 # Создадим переменную которая загружает(load) из файла (myfile01) информацию 
for show_json in json_data:
    print("Player_name = " + str(show_json['PlayerName']))
    print("Player_score = " + str(show_json['Score']))
    print("Player_awards = " + str(show_json['awards']))
    print("===============================================")

print("=========================================================================================\nEND\n=========================================================================================\n")

print("=========================================================================================\nРабота с аргументами\n=========================================================================================\n")
# Для начала работы нужно импортировать библиотеку sys
# Аргументы - это все ключи которые передаются при открытии файла из терминала например "myprogramm.py /open /save"
x = len(sys.argv)                                                                               # задаем переменную которая считывает длину агрументов в массиве
if x > 1:
    print('Your argument is:' + str(sys.argv[1:]))                                              # Выводим каждый аргумет кроме самого названия файла если их больше чем 1
    if sys.argv[1] == '/?':
        print ('Thanks for support')
        print('Usage this programm with: MYPRJ3.py kolya vasya ...')
else:
    print('Arguments is not found')
    
os.system("dir")                                                                                # С помощью команды os.system можно задавать команды как в командной строке 
os.system("dir > files/dir.txt")                                                                # таким образом монжо выполнить любую команду например записать из команды dir в текстовый файл
print("=========================================================================================\nEND\n=========================================================================================\n")

print("=========================================================================================\nРабота с регулярными выражениями\n=========================================================================================\n")
# Для начала работы нужно импортировать библиотеку re - Regular Expression
# Зададим массив текста который будем обрабатывать
mytext = "Kolya - 1993, Hfod@yandex.ru Operator, Anna annet@gmail.com, Vasilisa Samoylova - 2000 - vassam@ya.ru, " \
    "Petya dfsfnic, Hsom@say.com, Anton 1997, aaaaaaaaa, Password is trash, jerek@yandex.ru, Andrey - 21 - andrv@gmail.com, " \
    "Vladimir 1999, 2014332, whoami, Nikita@ya.ru" \

"""
\d = any number 0-9
\D = any symbol (, . / ... etc), non number 
\w = any alphabet a-z, A-Z
\W = any non alphabet a-z, A-Z
\s = breakspace (Probel)
\S = non breakspace (Probel)
"""
# примеры: \d\d\d искать 3 раза подряд цифры или [0-9][0-9][0-9], еще можно задать [0-9]{3}, можно задать определенное название yandex, указав [0-9]+ означает сколько угодно цифр
textlookfor = r"@\w+\.\w+"                                                                      # Создаем шаблон поиска для этого нужно перед началом того что ищем вставить букву r"text"
allresults = re.findall(textlookfor, mytext)                                                    # тут задаем переменную который принимает textlookfor, то что ищем и mytext откуда
print(allresults)

filename01 = "files/email.txt"                                                                  # Давайте попробуем найти все email из файла    
resultfile = "files/email_new.txt"
readfile01 = open(filename01, mode='r', encoding='utf-8')                                       # считаем информацию
writefile01 = open(resultfile, mode='w', encoding='utf-8')                                      # запишем в другой файл
myfile02 = readfile01.read()                                                                    # включим файл для чтения
emaillookfor = r"[\w._-]+@[\w._-]+\.[\w.]+"                                                     # вот сам шаблон поиска email сайт redex101.com. Для исключения чего-то нужно писать в (?!"text")
allresults02 = re.findall(emaillookfor, myfile02)
for item in allresults02:    
    writefile01.write(item + "\n")
    print(item)
print("Total email :" + str(len(allresults02)))
print("=========================================================================================\nEND\n=========================================================================================\n")

