def SortInc(a, b, c):
    if c < b:
        c, b = Swap(c, b)
    if b < a:
        b, a = Swap(b, a)
    return a, b, c


def Swap(a, b):
    return b, a


a = (input("Enter a "))
b = (input("Enter b "))
c = (input("Enter c "))
if a.isnumeric() and b.isnumeric() and c.isnumeric():
    a, b, c = SortInc(a, b, c)
    print("A = ", a, " B = ", b, " C = ", c)

a = (input("Enter a "))
b = (input("Enter b "))
c = (input("Enter c "))

if a.isnumeric() and b.isnumeric() and c.isnumeric():
    a, b, c = SortInc(a, b, c)
    print("A = ", a, " B = ", b, " C = ", c)
