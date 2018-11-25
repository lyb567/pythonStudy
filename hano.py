def hano(n, a, b, c):
    if n == 1:
        print("{0}-->{1}".format(a, c))
        return None
    if n == 2:
        print("{0}-->{1}".format(a, b))
        print("{0}-->{1}".format(a, c))
        print("{0}-->{1}".format(b, c))
        return None
    hano(n-1, a, c, b)
    print("{0}-->{1}".format(a, c))
    hano(n-1, b, a, c)
    return None


hano(8, 'a', 'b', 'c')
