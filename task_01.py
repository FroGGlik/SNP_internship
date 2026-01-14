import re

def is_palindrome(text):
    if isinstance(text, int):
        str_num = str(text)
        return str_num == str_num[::-1]

    if not isinstance(text, str):
        return False

    pattern_letters = r'[a-zA-Z]'
    letters = re.findall(pattern_letters, text.lower())

    pattern_digits = r'\d'
    digits = re.findall(pattern_digits, text)

    combined = letters + digits

    return combined == combined[::-1]


print(is_palindrome("A man, a plan, a canal -- Panama"))
print(is_palindrome("Madam, I'm Adam!"))
print(is_palindrome(333))
print(is_palindrome(None))
print(is_palindrome("Abracadabra"))