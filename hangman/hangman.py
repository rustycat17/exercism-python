# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman:
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.word = word
        self.known_characters = []

    def guess(self, char):
        if self.status == STATUS_WIN or self.remaining_guesses < 0:
            raise ValueError(r".+")
        if char not in self.word or char in self.known_characters:
            self.remaining_guesses -= 1
        else:
            self.known_characters.append(char)
            current_res = self.get_masked_word()
            if "_" not in current_res:
                self.status = STATUS_WIN

    def get_masked_word(self):
        masked_word = ""
        for i in range(len(self.word)):
            if self.word[i] in self.known_characters:
                masked_word += self.word[i]
            else:
                masked_word += "_"
        return masked_word

    def get_status(self):
        if self.remaining_guesses < 0:
            self.status = STATUS_LOSE
        return self.status
