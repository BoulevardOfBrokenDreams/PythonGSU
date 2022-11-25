import math

Xval = int(input("Enter X: "))
Yval = int(input("Enter Y: "))
Zval = int(input("Enter Z: "))

Qval = math.sin(math.sin(math.cos(math.cos(Yval)))) / math.sqrt(2 - Zval) + pow(Yval, 2) / (pow(Xval, 2) - 2) * \
       pow(math.e, Xval) * math.sqrt(Xval - math.pow(Yval, Xval))
print("Answer = ", Qval)
