import string


def is_pangram(sentence):
    unique_letters = set(sentence.lower())
    res = unique_letters.intersection(string.ascii_lowercase)

    return len(res) == 26
