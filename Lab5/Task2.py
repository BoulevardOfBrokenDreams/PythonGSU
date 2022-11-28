

while True:
    try:
        a = input("Enter a ")
        b = input("Enter b ")
        c = input("Enter c ")

        if eval(a) <= 0 or eval(b) <= 0 or eval(c) <= 0:
            raise Exception("Entered incorrect data")
        else:
            break
    except Exception as e:
        print(e)

answer = False
if (eval(a) > 0 and eval(b) > 0 and eval(c) > 0) and \
        (eval(a) + eval(b) > eval(c) and eval(a) + eval(c) > eval(b) and eval(b) + eval(c) > eval(a)):
    answer = True
print(answer)
