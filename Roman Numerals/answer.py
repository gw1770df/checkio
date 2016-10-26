# I（1）、V（5）、X（10）、L（50）、C（100）、D（500）和M（1000）

SUPER_UITL = [( lambda x: x % 10, ('I', 'V', 'X')),
              (lambda x: x / 10 % 10, ('X', 'L', 'C')),
              (lambda x: x / 100 % 10, ('C', 'D', 'M')),
              (lambda x: x / 1000 % 10, ('M', 'V', 'X'))]

def checkio(data):
    ss = []
    for fun, util in SUPER_UITL:
        ss.append(fuck(fun(data), *util))

    return ''.join(ss[::-1])

def fuck(n, n1, n5, n10):
    if 0 < n <= 3:
        return n1 * n
    elif n == 4:
        return n1 + n5
    elif 5 <= n <= 8:
        return n5 + n1 * (n-5)
    elif n == 9:
        return n1 + n10
    else:
        return ''

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
