# simple-OS-in-python

This python program is an implementation of a simple operating system. It can do simple arithmetic, determine order of operations, and loops. This program is from the Youtube video: https://youtu.be/1WpKsY9LBlY

See examples below:

### Examples

```
PseudoScript > 1 + 3 * 7
22
PseudoScript > (1 + 2) * 3
9
PseudoScript > make a = 50
[make, a, =, 50]
[a, =, 50]
PseudoScript > make a = 1 + 2 * 5
[make, a, =, 1, +, 2, *, 5]
[a, =, [1, +, [2, *, 5]]]
```

## lexer.py

This program does lexical analysis on an input phrase.
For example, if "5 + 3" is the input, the program will parse it [5, +, 3] and perform the arithmetic operation.