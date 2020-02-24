
def square_plus_one(x):
    if not isinstance(x, int):
        raise TypeError('x must be int')

    if x <= 1:
        raise ValueError('x must be greater than one')

    return x**2 + 1


def replace_spaces(s):
    if not isinstance(s, str):
        raise TypeError('s must be string')

    return s.replace(' ', '_')


if __name__ == '__main__':
    print(square_plus_one(2))
