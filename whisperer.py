from enum import Enum
from collections import namedtuple


def take_while(predicate, iterator):
    for i in iterator:
        yield i
        if not predicate(i):
            break


class TokenType(Enum):
    TEXT = 0
    VARIABLE = 1
    INPUT = 2
    CONDITIONAL = 3
    BLOCK = 4


Token = namedtuple('Token', ['type', 'data'])


def tokenize(text: str) -> list:
    text_iter = iter(text)
    tokens = []
    for char in text_iter:
        if char.isspace():
            take_while(lambda c: c.isspace, text_iter)
        elif char == '*':
            data = list(take_while(lambda c: not c.isspace(), text_iter))
            tokens.append(Token(TokenType.VARIABLE, ''.join(data[:-1])))  # cut off end symbol
            tokens.append(Token(TokenType.TEXT, data[-1]))                # and add it as separate token
        elif char == '#':
            data = list(take_while(lambda c: c != '\n', text_iter))
            for d in ''.join(data).split():
                tokens.append(Token(TokenType.INPUT, ''.join(d)))
        elif char == '{':
            data = list(char)
            data.extend(take_while(lambda c: c != '}', text_iter))
            if data[-1] != '}':
                raise RuntimeError('Closing \'}\' is missing')
            tokens.append(Token(TokenType.BLOCK, ''.join(data)))
        elif char == '|':
            data = list(char)
            data.extend(take_while(lambda c: not c.isspace(), text_iter))
            tokens.append(Token(TokenType.CONDITIONAL, ''.join(data)))
        else:
            data = list(char)
            data.extend(take_while(lambda c: not c.isspace(), text_iter))
            tokens.append(Token(TokenType.TEXT, ''.join(data)))
    return tokens
