# я не понял, что было написано в задании 12
# поэтому сделал задание 20
# Дан строковый файл. Создать новый строковый файл, содержащий все строки
# исходного файла наибольшей длины (в обратном порядке).
with open("dataTask2.txt", "r", encoding="utf-8") as file:
    data = file.readlines()

print(data)

max_length = 0
for word in data:
    if len(word) > max_length:
        max_length = len(word)

file = open("resultTask2.txt", "w")
for i in range(0, len(data)):
    if len(data[len(data) - 1 - i]) == max_length:
        file.write(data[len(data) - 1 - i])
