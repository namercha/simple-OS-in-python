from lexer import Lexer

while True:
    text = input("PseudoScript: ")
    tokenizer = Lexer(text=text)
    tokens = tokenizer.tokenize()

    print(tokens)
