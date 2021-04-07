import random
import string


class Robot:
    def __init__(self):
        # random.seed(random.randint(1, 1e6))
        letters = random.choices(string.ascii_uppercase, k=2)
        numbers = random.choices(string.digits, k=3)
        name = "".join(letters + numbers)

        self.name = name

    def reset(self):
        random.seed(random.randint(1, 1e9))
        self.__init__()
