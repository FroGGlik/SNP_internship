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


class JellyBean(Dessert):
    def __init__(self, name=None, calories=None, flavor='Unknown'):
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
        return self._flavor.lower() != 'black licorice'

    def __str__(self):
        info = (
            f'Название блюда: {self._name}\n'
            f'Калорийность блюда: {self._calories}\n'
            f'Здоровое ли блюдо: {"Да" if self.is_healthy() else "Нет"}\n'
            f'Вкусное ли блюдо: {"Да" if self.is_delicious() else "Нет, это black licorice"}'
        )

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


dessert5 = Dessert("Vanilla Ice Cream", 250)

print("Название:", dessert5.name)
print("Калории:", dessert5.calories)

dessert5.name = "Strawberry Sorbet"
dessert5.calories = 180

print("Обновленное название:", dessert5.name)
print("Обновленные калории:", dessert5.calories)

print("Это полезно?", dessert5.is_healthy())
