def test():
    a = 1000
    b = 'thousand'
    print(a, b)


test()


def test2(a=1, b= '"буква Б"', c=10):
    print(a, b, c)


test2(c=3, b= 111, a='"буква А"')
