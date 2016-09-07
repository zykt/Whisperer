from whisperer import TokenType, tokenize


def parse(text: str):
    tokens = tokenize(text)
    variables = {
        'name': 'zykt'
    }
    for token in tokens:
        if token.type is TokenType.TEXT:
            print(token.data, end='')
        elif token.type is TokenType.VARIABLE:
            try:
                print(variables[token.data], end='')
            except KeyError:
                print('{} NOT FOUND '.format(token.data), end='')
        elif token.type is TokenType.INPUT:
            inp = input('input {}\n'.format(token.data))
            variables[token.data] = inp
            # print("INPUT {}".format(token.data), end='')
        else:
            print(token, end='')


if __name__ == '__main__':
    with open('text.txt') as f:
        text = f.read()
        parse(text)
