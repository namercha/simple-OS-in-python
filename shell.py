from lexer import Lexer
from parser_1 import Parser
from interpreter import Interpreter

while True:
    text = input("PseudoScript > ")
    
    tokenizer = Lexer(text=text)
    tokens = tokenizer.tokenize()

    print(tokens)

    parser = Parser(tokens=tokens)
    tree = parser.parse()

    print(tree)

    # interpreter = Interpreter(tree=tree)
    # result = interpreter.interpret()

    # print(result)
