import csv


class IncorrectKeyError(Exception):
    def __init__(self, file_keys, dict_keys):
        self.file_keys = file_keys
        self.dict_keys = dict_keys
        self.message = "The chosen index does not fit within that of the length of the file"


class InvalidIndexValue(Exception):
    def __init__(self, min_index, max_index, chosen_index):
        self.max_index = max_index
        self.min_index = min_index
        self.chosen_index = chosen_index


def add_to_csv(dict_to_add: dict, csv_file: str, index: int = -1) -> None:
    """
    This functions allows you to add a line to a csv file in whatever place you want
    :param dict_to_add: is the line we want to add to the dictionary in dictionary form
    :param csv_file: is the string value that takes the path to the designated file
    :param index: Is the position at which we want to add it.
    (!The first line containing actual values is considered index 0!)
    :returns: the modified csv file
    """

    # First we check whether we received the right input
    with open(csv_file, "r") as file:

        dict_file = list(csv.DictReader(file))

        # Here we make sure that the dictionary we received is in sync with the file
        for x in dict_file:
            print(x)
        file_keys: tuple = tuple(dict_file[0].keys())

        # We can't add to a file using the DictReader objects if the keys
        # of the file and dictionary don't match up. Here we check that to avoid
        # more trouble further down the line
        if tuple(dict_to_add.keys()) != file_keys:
            print(file_keys)
            print(tuple(dict_to_add.keys()))
            raise IncorrectKeyError(tuple(file_keys), tuple(dict_to_add.keys()))

    # Now we know the keys are correct,
    # all there's left to do is simply adding the dictionary to the file
    # If the index value remains untouched, we assume the user wants to
    # append a line to the file

    # Here we append to the file, given index remains untouched
    if index == -1:
        with open(csv_file, "a") as file:
            writer = csv.DictWriter(file, fieldnames=list(dict_to_add.keys()))
            writer.writerow(dict_to_add)

    # And here we deal with the file if the file has received an index position
    else:

        with open(csv_file, "r") as file:
            reader = csv.reader(file)

            # First we save all the information of the file in a pretty large list
            # The list contains list, where each smaller list represents a line of the file
            # The first line always represents the keys(/row names of the file)
            file_content: list = []
            for line in reader:
                if not line:
                    continue
                file_content.append(line)

        # We have to check whether the given index is a valid one
        # If not, we raise another error
        if index not in range(1, len(file_content)-1):
            raise InvalidIndexValue(1, len(file_content)-1, index)

        # If the chosen index is valid we will add the dictionary
        # to the right file at the correct index

        # Here the file gets wiped in order to rewrite it
        with open(csv_file, "w") as file:
            dict_writer = csv.DictWriter(file, fieldnames=list(file_content[0]))
            list_writer = csv.writer(file)
            for line in file_content:

                # Here we re-add the header of the csv file
                if file_content.index(line) == 0:
                    list_writer.writerow(line)

                # Here we add the dict_line variable we received as input
                # The dict_to_add variables goes before the line at that current index
                elif file_content.index(line) == index:
                    list_writer.writerow(line)
                    dict_writer.writerow(dict_to_add)

                # And here the line just gets appended if it doesn't interfere with the chosen index
                else:
                    list_writer.writerow(line)


path: str = "../datasets/test_csv.csv"
add_to_csv({"name": "Pootis Mann", "grade": 65, "passed": True}, path, 2)
