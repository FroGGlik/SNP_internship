import re

def is_palindrome(text: str):
    if not isinstance(text, str):
        return False
    pattern = r'[a-zA-Z]'
    string_only_alph = re.findall(pattern, text.lower())
    return string_only_alph == string_only_alph[::-1]

print(is_palindrome("A man, a plan, a canal -- Panama"))
print(is_palindrome("Madam, I'm Adam!"))
print(is_palindrome(333))
print(is_palindrome(None))
print(is_palindrome("Abracadabra"))