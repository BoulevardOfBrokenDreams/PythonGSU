N = int(input("Enter N "))
result = 1

if N > 0:
    for item in range(1, N + 1):
        result *= item
    print(result)

    N = result

    for item in range(1, N + 1):
        result *= item

print(result)