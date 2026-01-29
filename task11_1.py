class Dessert:
    def __init__(self, name=None, calories=None):
        self._name = name
        self._calories = calories

    def get_name(self):
        return self._name

    def _set_name(self, name):
        self._name = name

    def get_calories(self):
        return self._calories

    def set_calories(self, calories):
        self._calories = calories

    def is_healthy(self):
        if isinstance(self._calories, (int, float)):
            return self._calories < 200
        return False

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