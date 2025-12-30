'''
Реализуйте класс EvenNumbers, который в конструкторе принимает целое число n
— количество чётных чисел для генерации. Итератор должен выдавать числа по
порядку, начиная с 0: 0, 2, 4, ..., 2*(n-1).
Тесты для примеров и проверки:
evens = EvenNumbers(5)
for num in evens:
print(num) # Должно вывести 0, 2, 4, 6, 8
'''
class EvenNumbers():
    def __init__(self, n: int):
        self.n = n
        self.count = 0
        self.counter = 0

    def __iter__(self):
        self.count = 0
        self.counter = 0
        return self

    def __next__(self):
        if self.count >= self.n:
            raise StopIteration
        value = 2 * self.counter 
        self.count += 1
        self.counter += 1
        return value


try:
    evens = EvenNumbers(5)

    for num in evens:
        print(num) # Должно вывести 0, 2, 4, 6, 8
except TypeError as ex:
    print(f'Ваша ошибка: {ex}')