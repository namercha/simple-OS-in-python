from tokens import Operation, Integer, Float, Declaration, Variable

class Lexer:
    """Converts the user input into machine readable types and classes."""

    digits = "0123456789"
    letters = "abcdefghijklmnopqrstuvwxyz"
    operations = "+-/*()="
    stop_words = [" "]
    declarations = ["make"]

    def __init__(self, text) -> None:
        self.text = text
        self.idx = 0
        self.tokens = []
        self.char = self.text[self.idx]
        self.token = None

    def tokenize(self):
        while self.idx < len(self.text):
            if self.char in Lexer.digits:
                self.token = self.extract_number()

            elif self.char in Lexer.operations:
                self.token = Operation(self.char)
                self.move()

            elif self.char in Lexer.stop_words:
                self.move()
                continue

            elif self.char in Lexer.letters:
                word = self.extract_word()
                if word in Lexer.declarations:
                    self.token = Declaration(word)
                else:
                    self.token = Variable(word)

            self.tokens.append(self.token)

        return self.tokens

    def extract_number(self):
        number = ""
        isFloat = False
        while (self.char in Lexer.digits or self.char == ".") and (self.idx < len(self.text)):
            if self.char == ".":
                isFloat = True

            number += self.char
            self.move()

        return Integer(number) if not isFloat else Float(number)

    def extract_word(self):
        word = ""
        while (self.char in Lexer.letters and self.idx < len(self.text)):
            word += self.char
            self.move()

        return word


    def move(self):
        self.idx += 1
        if self.idx < len(self.text):
            self.char = self.text[self.idx]
