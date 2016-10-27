B_M = {']': '[', '}': '{', ')': '('}
B_S = set('{}[]()')

def checkio(e):
    return not reduce(lambda x,y: x[:-1] if y in B_M and x.endswith(B_M[y]) else x + y, (x for x in e.encode('utf-8') if x in B_S), '')

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"((5+3)*2+1)") == True, "Simple"
    assert checkio(u"{[(3+1)+2]+}") == True, "Different types"
    assert checkio(u"(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio(u"[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio(u"(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio(u"2+3") == True, "No brackets, no problem"
