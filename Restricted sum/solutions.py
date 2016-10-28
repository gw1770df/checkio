checkio = lambda x: 0 if not len(x) else x[0] + checkio(x[1:])

if __name__ == '__main__':
    print checkio([1, 2, 3])
