'''
Задание является не обязательным, но его выполнение поможет лучше
ознакомиться с итераторами.
Реализовать класс BlockTranspositionCipher, который будет шифровать и
расшифровывать текст методом блочной перестановки с помощью текстового
ключа.
Основная идея:

1. Ключ — строка, состоящая из уникальных английских букв. Пример:
acb
2. Шифрование — алгоритм, который преобразует исходный текст в
набор зашифрованных символов.
3. Дешифрование — алгоритм, который преобразует набор
зашифрованных символов в исходный текст.

Ключ и его обработка:

• ключ состоит только из букв английского алфавита
• символы в ключе должны быть уникальны (регистр букв не имеет
значения — "A" и "a" считаются одинаковыми)
• ключ преобразуется в числовой массив. Каждому символу
присваивается его порядковый номер в алфавите (a = 0, b = 1, ..., z =
25)

Правила шифрования:

• исходный текст делится на блоки длины, равной длине ключа
• если длина блока не кратна длине ключа, то оставшийся блок
дополняется пробелами
• в каждом из блоков символы переставляются согласно порядку из
ключа

Пример алгоритма шифрования:
Ключ: "acb"
Текст: "helloworld"
Блоки: ["hel", "low", "orl", "d "]
Блоки после перестановки: ["hle", "lwo", "olr", "d "]
Результат: "hlelwoolrd "
Правила дешифрование:

• исходный порядок восстанавливает символы в каждом блоке
• лишние пробелы после дешифровки удаляются

Валидации и работа с ошибками:

• проверяется, что ключ состоит только из букв английского алфавита
• проверяется, что все буквы в ключе уникальны, игнорируя регистр
• если ключ не соответствует требованиям, вызывается исключение
ValueError с понятным сообщением об ошибке

Тесты для примеров и проверки:
Пример 1: Шифрование с явной итерацией по блокам
text = "HELLOWORLD"
key = "bAc"
print("Процесс шифрования по блокам:")
cipher = BlockTranspositionCipher(text, key)
for i, encrypted_block in enumerate(cipher, 1):
print(f"Блок {i}: '{encrypted_block}'")*

Пример 2: Полное шифрование
cipher = BlockTranspositionCipher(text, key)
encrypted = ''.join(cipher)
print(f"\nПолный зашифрованный текст: '{encrypted}'")
Пример 3: Дешифрование с итерацией
print("\nПроцесс дешифрования по блокам:")
decipher = BlockTranspositionCipher(encrypted, key, decrypt=True)
for i, decrypted_block in enumerate(decipher, 1):
print(f"Блок {i}: '{decrypted_block}'")
Пример 4: Полное дешифрование с обрезкой пробелов
decipher = BlockTranspositionCipher(encrypted, key, decrypt=True)
decrypted = ''.join(decipher)
print(f"\nПолный расшифрованный текст: '{decrypted}'")
'''

class BlockTranspositionCipher():
    def __init__(self, text, key, decrypt=False):
        self.text = text
        self.key = key.lower()
        self.decrypt = decrypt
        self.encrypted = None

        if not self.key.isalpha():
            raise ValueError('Ключ должен содержать только буквы')
        if len(set(key)) == len(key):
            raise ValueError('Все буквы ключа должны быть уникальными')
        
        self.block_size = len(key)
        self._prepare_permutation()
        self._create_block()

        self._index = 0

    def _prepare_permutation(self):
        sorted_letters = sorted(enumerate(self.key), key=lambda x: x[1])
        self.order = [index for index, _ in sorted_letters]

        self.inverse_order = [0] * self.block_size
        for i, pos in enumerate(self.order):
            self.inverse_order[pos] = i

    def _create_block(self):
        text_len = len(self.text)
        self.blocks = [self.text[i:i + self.block_size].ljust(self.block_size) for i in range(0, len(text_len), self.block_size)]

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self._index >= len(self.blocks):
            raise StopIteration
        block = self.blocks[self._index]
        self._index += 1

        if self.decrypt:
            chars = [''] * self.block_size
            for i, pos in enumerate(self.inverse_order):
                chars[pos] = block[i]
            return ''.join(chars)
        else:
            chars = [''] * self.block_size
            for i, pos in enumerate(self.order):
                chars[pos] = block[i]
            return ''.join(chars)
        
    def __len__(self):
        return len(self.blocks)


try:
    text = "HELLOWORLD"
    key = "bAc"
    print("Процесс шифрования по блокам:")
    cipher = BlockTranspositionCipher(text, key)
    for i, encrypted_block in enumerate(cipher, 1):
        print(f"Блок {i}: '{encrypted_block}'")


    cipher = BlockTranspositionCipher(text, key)
    encrypted = ''.join(cipher)
    print(f"\nПолный зашифрованный текст: '{encrypted}'")

    print("\nПроцесс дешифрования по блокам:")
    decipher = BlockTranspositionCipher(encrypted, key, decrypt=True)
    for i, decrypted_block in enumerate(decipher, 1):
        print(f"Блок {i}: '{decrypted_block}'")

    decipher = BlockTranspositionCipher(encrypted, key, decrypt=True)
    decrypted = ''.join(decipher)
    print(f"\nПолный расшифрованный текст: '{decrypted}'")
except Exception as ex:
    print(f'Ваша ошибка: {ex}')