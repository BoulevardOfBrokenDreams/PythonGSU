def SortInc(a, b, c):
    if c < b:
        c, b = Swap(c, b)
    if b < a:
        b, a = Swap(b, a)
    return a, b, c


def Swap(a, b):
    return b, a

