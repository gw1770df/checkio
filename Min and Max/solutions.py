def min(*args, **kwargs):
    fun, m1, m2 = kwargs.get('key', lambda x : x), None, None
    args = args if hasattr(args, 'next') or len(args) > 1 else args[0]
    for i in args:
        ii = fun(i)
        if m1 == None or m1 > ii:
            m1, m2 = ii, i
    return m2

def max(*args, **kwargs):
    fun, m1, m2 = kwargs.get('key', lambda x : x), None, None
    args = args if hasattr(args, 'next') or len(args) > 1 else args[0]
    for i in args:
        ii = fun(i)
        if m1 == None or m1 < ii:
            m1, m2 = ii, i
    return m2


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
