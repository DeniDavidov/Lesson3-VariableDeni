def test(*params):
    print(params)


test(111, *'список', 11.333)  # с разбивкой строки 'список'


def multiplier(n):
    if n == 1:
        return 1
    else:
        return n * multiplier(n - 1)


print(multiplier(5))
