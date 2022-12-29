import csv

with open("test_csv.csv" ,"r") as file:
    reader = csv.DictReader(file)
    reader_list = tuple(reader)
    print(reader_list)

