import string


def is_pangram(sentence):
    tmp = set(sentence.lower())
    res = set()
    for element in tmp:
        if element in string.ascii_lowercase:
            res.add(element)

    return len(res) == 26
