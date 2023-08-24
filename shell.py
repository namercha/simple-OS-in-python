from lexer import Lexer
from parser_1 import Parser
from interpreter import Interpreter
from data import Data

base = Data()

while True:
    text = input("PseudoScript > ")
    
    tokenizer = Lexer(text=text)
    tokens = tokenizer.tokenize()

    print(tokens)

    parser = Parser(tokens=tokens)
    tree = parser.parse()

    print(tree)

    interpreter = Interpreter(tree=tree, base=base)
    result = interpreter.interpret()

    print(result)
