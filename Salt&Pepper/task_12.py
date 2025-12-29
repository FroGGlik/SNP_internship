# from task_11 import Dessert
# Можно просто импортировать класс Dessert из нашего файла или создать новый в этом файле.
class Dessert():
    def __init__(self, name='Unnamed', calories=0):
        self._name = name
        self._calories = calories
        self._is_healthy = None
        self._is_delisious = True
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value

    @property
    def calories(self):
        return self._name
    
    @calories.setter
    def calories(self, value):
        self._calories = value

    def get_info(self):
        return self._name, self._calories
    
    def is_healthy(self):
        return self._calories < 200
    
    def is_delicious(self):
        return True
    
    def set_healthy(self):
        self._is_healthy = self._calories < 200
    
    def __str__(self):
        info = f'Название блюда: {self._name}\nКалорийность блюда: {self._calories}\nЗдоровое ли блюдо: {'Да' if self.is_healthy() else 'Нет'}\nВкусное ли блюдо: {'Да' if self.is_delicious() else 'Нет'}\n'
        return info


class JellyBean(Dessert):
    def __init__(self, name='Unnamed', calories=0, flavor = 'Unknown'):
        super().__init__(name, calories)
        self._flavor = flavor

    @property
    def flavor(self):
        return self._flavor
    
    @flavor.setter
    def flavor(self, value):
        self._flavor = value

    def info(self):
        return self._name, self._calories, self._flavor

    def is_delicious(self):
        if self._flavor == 'black licorice':
            return False
        else:
            return True

    def __str__(self):
        info = f'Название блюда: {self._name}\nКалорийность блюда: {self._calories}\nЗдоровое ли блюдо: {'Да' if self.is_healthy() else 'Нет'}\nВкусное ли блюдо: {'Да' if self.is_delicious() else 'Нет это black licorice'}\n'
        return info


try:
    dessert1 = JellyBean('Шоколадный торт', 450, 'black licorice')
    dessert2 = JellyBean('Салат "весенний"', 150)
    dessert3 = JellyBean('Суп грибной')
    dessert4 = JellyBean()

    print(dessert1)
    print(dessert2)
    print(dessert3)
    print(dessert4)
except TypeError:
    print('Введите правильное кол-во аргументов')