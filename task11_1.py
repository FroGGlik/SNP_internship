class Dessert:
    def __init__(self, name=None, calories=None):
        self._name = name
        self._calories = calories

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
        self._calories = value
    
    def is_healthy(self):
        return self._calories is not None and self._calories < 200
    
    def is_delicious(self):
        return True
    
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


dessert1 = Dessert("Vanilla Ice Cream", 250)

print("Название:", dessert1.name)
print("Калории:", dessert1.calories)

dessert1.name = "Strawberry Sorbet"
dessert1.calories = 180

print("Обновленное название:", dessert1.name)
print("Обновленные калории:", dessert1.calories)

print("Это полезно?", dessert1.is_healthy())