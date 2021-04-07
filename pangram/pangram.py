import string


def is_pangram(sentence):
    tmp = set(sentence.lower())
    res = [element for element in tmp if element in string.ascii_lowercase]

    return len(res) == 26
