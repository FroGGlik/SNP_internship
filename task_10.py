def count_words(text: str) -> dict:
    punctuation = ',.?!:;-()'

    for ch in punctuation:
        text = text.replace(ch, '')

    words = text.lower().split()

    words_count = {}

    for word in words:
        words_count.setdefault(word, 0)
        words_count[word] += 1

    return words_count


print(count_words("A man, a plan, a canal -- Panama"))
print(count_words("Doo bee doo bee doo"))