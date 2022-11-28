
with open("dataTask1.txt", "r", encoding='utf-8') as file_read:
    data = file_read.readline()

strings = ""
for i in range(0, len(data)):
    if data[i] == '.' or data[i] == ',' or data[i] == '!':
        continue
    else:
        strings += data[i]
data = strings.split()

biggest_word = data[0]

for word in data:
    if len(word) > len(biggest_word):
        biggest_word = word

print(biggest_word)
with open("resultTask1.txt", "w") as file_write:
    file_write.write(biggest_word)