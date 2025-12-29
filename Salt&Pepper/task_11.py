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

try:
    dessert1 = Dessert('Шоколадный торт', 450)
    dessert2 = Dessert('Салат "весенний"', 150)

    print(dessert1)
    print(dessert2)
except TypeError:
    print('Введите правильное кол-во аргументов')