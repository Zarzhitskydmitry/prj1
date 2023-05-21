
print("=========================================================================================\nРабота с классами\n=========================================================================================\n")
class Hero():
    """Class to create Hero for our game"""
    def __init__(self, name, level, race):                                                  # Создаем функцию для параметров героя
        """Iniciiruem etogo geroya"""
        self.name = name                                                                    # Определяем параметры героя
        self.level = level
        self.race = race
        self.health = 100
        
    def show_hero(self):                                                                    # функция показывает параметры героя
        discription = (self.name + "\n level is: " + str(self.level) + "\n race is: " + self.race + "\n health is:" + str(self.health)).title()
        print (discription)
        
    def level_up(self):                                                                     # функция повышения уровня героя
        self.level += 1                                                                     # повышаем уровень на 1
        print(self.name + " level up - " + str(self.level))
    
    def move(self):
        print("Hero " + self.name + " start moving")
    
    def set_health(self, new_health):                                                       # напрямую желательно не изменять параметр, а создать функцию для изменения
        self.health = new_health
        

#================================================================================================================================#
class SuperHero(Hero):                                                                      # создаем класс супергероя и подключаем класс героя, т.к. берем одни и теже значения и будут полностью работать
    def __init__(self, name, level, race, magiclevel):                                      # Супергерою мы добавим одну способность магии
        super().__init__(name, level, race)                                                 # super.()__init__ мы берем уже существующие параметры у Hero, так же можно и отдельные
        self.magiclevel = magiclevel
        self.__magic = 100                                                                  # для запрета изменения значения извне класса нужно использовать __ перед нашим параметром
    # __ называется инкапсуляция
    def use_magic(self):                                                                    # Создаем функцию использования магии
        self.__magic -= 10
        
    def show_hero(self):                                                                    # функция показывает параметры героя
        discription = (self.name + "\n level is: " + str(self.level) + "\n race is: " + self.race 
                       + "\n health is:" + str(self.health) + "\n Magic is: " + str(self.__magic)).title()
        print (discription)
print("=========================================================================================\nEND\n=========================================================================================\n")






