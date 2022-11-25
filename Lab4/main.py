import Task1
from functionPack.Sorting import SortInc

X = int(input("Enter X "))
Y = int(input("Enter Y "))
AMean, GMean = Task1.Mean(X, Y)
print("Amean ", AMean)
print("Gmean ", GMean)

a = (input("Enter a "))
b = (input("Enter b "))
c = (input("Enter c "))
if a.isnumeric() and b.isnumeric() and c.isnumeric():
    a, b, c = SortInc(a, b, c)
    print("A = ", a, " B = ", b, " C = ", c)