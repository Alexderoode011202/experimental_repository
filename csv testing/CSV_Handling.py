import csv

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

"""

with open("C:/Users/Alexd/Downloads/Business-employment-data-september-2022-quarter-csv/Business-employment-data-september-2022-quarter-csv.csv", "r") as file:
    csv_file = csv.DictReader(file)


    csv_file = tuple(csv_file)
    print(csv_file[0].keys())
    print(csv_file[0].values())

    print("\n {}".format(csv_file[0]))
"""

""" 
with open("C:/Users/Alexd/Downloads/Adressen_Arnhem.csv") as file:
    csv_reader = csv.reader(file)
    csv_copy_list: list = []

    for line in csv_reader:
        csv_copy_list.append(line)

print(csv_copy_list)
"""
from csv import writer
with open("../datasets/test_csv.csv", "a") as test_file:
    # reader = csv.reader(test_file)
    # print(tuple(reader))
    field_names: dict = {"name": "Poes", "grade": 9.9, "passed": True}
    list_values: list = ["Poes", 9.9, True]
    keys_list: list = ["name", "grade", "passed"]

    writer_obj = csv.writer(test_file, fieldnames=keys_list)

    writer_obj.writerow(field_names)

    test_file.close()

with open("../datasets/test_csv.csv", "r") as read_file:
    dict_obj = csv.DictReader(read_file)

    for line in dict_obj:
        print(line)

with open("new_csv.csv", "w") as new_file:
    writer_obj = csv.Dictwriter()

    




    test_file.close()