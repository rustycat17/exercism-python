def classify(number):
    if number < 1:
        raise ValueError("number must be larger than 0")

    res = 0
    for i in range(1, number // 2 + 1):
        if number % i == 0:
            res += i

    if res == number:
        return "perfect"
    elif res > number:
        return "abundant"
    else:
        return "deficient"
