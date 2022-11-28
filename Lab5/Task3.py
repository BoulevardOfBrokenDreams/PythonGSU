import math
def Mean(X, Y):
    AMean = (X + Y) / 2
    GMean = (math.sqrt(X * Y))
    return AMean, GMean

while True:
    try:
        X = input("Enter X ")
        Y = input("Enter Y ")

        if not (X.isnumeric() and Y.isnumeric()) and type(eval(X)) != float and type(eval(Y)) != float:
            raise Exception("Entered non numeric parameters")
        if not (eval(X) >= 0 and  eval(Y) >= 0):
            raise Exception("Entered one or two of parameters non natural")
        break
    except Exception as e:
        print(e)

AMean, GMean = Mean(eval(X), eval(Y))

print(f"Amean  {AMean} \nGmean {GMean}")