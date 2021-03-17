import string

def is_pangram(sentence):
    res = []
    for letter in sentence.lower():
        if letter in string.ascii_lowercase:
            res.append(letter)

    res = set(res)
    return True if len(res) == 26 else False
