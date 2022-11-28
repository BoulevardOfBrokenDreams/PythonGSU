with open("data.txt", "r") as file:
    data = file.readline().split()
    file.close()

result_list = {0}
i = -1
while True:
    try:
        i += 1
        if i >= len(data) - 1:
            break
        result_list.add(eval(data[i]))

    except Exception as e:
        print(e)
        i += 1
print(result_list)