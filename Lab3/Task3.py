import math
def Mean(X, Y):
    AMean = (X + Y) / 2
    GMean = (math.sqrt(X * Y))
    return AMean, GMean


X = int(input("Enter X "))
Y = int(input("Enter Y "))
AMean, GMean = Mean(X, Y)
print("Amean ", AMean)
print("Gmean ", GMean)


