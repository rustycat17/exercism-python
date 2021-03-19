def is_armstrong_number(number):
    res = 0
    for digit in str(number):
        res += int(digit) ** len(str(number))

    return True if res == number else False
