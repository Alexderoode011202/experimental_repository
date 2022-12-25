
"""
with open("test_textfile.txt", "r") as file:
    reverse_list: list = []
    for line in file:
        line = line.replace("\n", "")
        reverse_list.append(line[::-1])

print(reverse_list)

for x in reverse_list:
    print(x)

with open("test_textfile.txt", "a") as file:
    file.write("\n")
    for line in reverse_list:
        file.write(line + "\n")
"""

import csv
with open("C:/Users/Alexd/Downloads/spotify-dataset.csv", "r") as file:
    csv_file = csv.reader(file)

    for line in csv_file:
        try:
            print("test")
            print(line)

        except Exception as e:
            print(e)



