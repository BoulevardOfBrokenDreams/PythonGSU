import math
from array import array


def IsPowerN(K, N):
    for i in range(1, K):
        if math.pow(N, i) == K:
            return True
    return False

def Powerl(A, B):
    if A <= 0:
        return 0
    return math.exp(B * math.log(A))

N = float(input("Enter N "))
mass = array('i')
for i in range(10):
    mass.append(int(input("Enter number mass = ")))
counter = 0
for i in mass:
    if(IsPowerN(i, N)):
        counter += 1
print("answer = ", counter)

print("--------------------")

P = float(input("Enter P "))
A = float(input("Enter A "))
B = float(input("Enter B "))
C = float(input("Enter C "))

print("Ap", Powerl(A, P))
print("Bp", Powerl(B, P))
print("Cp", Powerl(C, P))