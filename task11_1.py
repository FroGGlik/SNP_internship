class Dessert:
    def __init__(self, name='Unnamed', calories=None):
        self._name = name
        self.calories = calories

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value

    @property
    def calories(self):
        return self._calories
    
    @calories.setter
    def calories(self, value):
        print(f"Setting calories to {value}")
        if isinstance(value, str):
            if value.isdigit():
                self._calories = int(value)
            else:
                self._calories = 0
        elif isinstance(value, int):
            self._calories = value
        else:
            self._calories = 0
    
    def is_healthy(self):
        return self._calories < 200
    
    def is_delicious(self):
        return True
    
    def set_healthy(self):
        self._is_healthy = self._calories < 200
    
    def __str__(self):
        return (f'Название блюда: {self._name}\n'
                f'Калорийность блюда: {self._calories}\n'
                f'Здоровое ли блюдо: {"Да" if self.is_healthy() else "Нет"}\n'
                f'Вкусное ли блюдо: {"Да" if self.is_delicious() else "Нет"}')


desserts = []

try:
    desserts.append(Dessert("Шоколадный торт", 450))
    desserts.append(Dessert("Салат 'весенний'", 150))
    desserts.append(Dessert())

    for d in desserts:
        print(d)
except TypeError:
    print('Введите правильное кол-во аргументов')