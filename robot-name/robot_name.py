import random
import string


class Robot:
    def __init__(self):
        random.seed(random.randint(1, 1e6))
        letters = "".join(random.choice(string.ascii_uppercase) for x in range(2))
        numbers = "".join(random.choice(string.digits) for x in range(3))
        name = letters + numbers

        self.name = name

    def reset(self):
        random.randint(1, 1e9)
        self.__init__()
