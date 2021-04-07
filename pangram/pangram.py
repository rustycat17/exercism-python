import string


def is_pangram(sentence):
    res = set()
    for letter in sentence.lower():
        if letter in string.ascii_lowercase:
            res.add(letter)
            if len(res) == 26:
                return True

    return False
