a = int(input("Enter a "))
b = int(input("Enter b "))
c = int(input("Enter c "))
answer = False

if a + b > c and a + c > b and b + c > a and a > 0 and b > 0 and c > 0:
    answer = True
print(answer)