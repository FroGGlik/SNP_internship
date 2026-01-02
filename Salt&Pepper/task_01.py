import re

string = input('Введите текст: ').lower()
pattern = r'[a-zA-Z]'
string_only_alph = re.findall(pattern, string)

# 1 способ через цикл while
left, right = 0, len(string_only_alph) - 1
flag = True
while left < right:
    if string_only_alph[left] != string_only_alph[right]:
        flag = False
        break
    left += 1
    right -= 1
if flag:
    print("Это палиндром")
else:
    print("Это не палиндром")

# 2 способ с изпользованием среза, с добавлением шабона
reverse_string = string_only_alph[::-1]
if string_only_alph == reverse_string:
    print("Это палиндром")
else:
    print("Это не палиндром")