import math

while True:
    try:
        X_value = input("Enter X: ")
        Y_value = input("Enter Y: ")
        Z_value = input("Enter Z: ")

        if not (type(eval(X_value)) == int or type(eval(Y_value)) == int or type(eval(Z_value)) == int):
            raise Exception("Entered not numeric values")
        if int(Z_value) > 2:
            raise Exception("Z number must be less or equal 2")
        if int(X_value) < pow(int(Y_value), int(X_value)):
            raise Exception("X value must be bigger or equal Y^X")
        break
    except Exception as e:
        print(e)

Qval = math.sin(math.sin(math.cos(math.cos(int(Y_value))))) / math.sqrt(2 - int(Z_value)) + pow(int(Y_value), 2) / \
       (pow(int(X_value), 2) - 2) * \
       pow(math.e, int(X_value)) * math.sqrt(int(X_value) - math.pow(int(Y_value), int(X_value)))
print("Answer = ", Qval)
