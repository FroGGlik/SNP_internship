def combine_anagrams(words_array: list) -> list:
    anagram_dict = {}

    for word in words_array:
        key = ''.join(sorted(word.lower()))
        anagram_dict.setdefault(key, []).append(word)

    return list(anagram_dict.values())


print(combine_anagrams(["cars", "for", "potatoes", "racs", "four", "scar", "creams", "scream"]))