from collections import Counter
from typing import List

def remove_keys(word_list: list, key: any):
    """ removes key"""
    try:
        word_list.pop(key)
    except:
        print("test")
        remove_keys()
    return None
# Single word filter approach


"""
with open("test_textfile.txt") as text_file:
    summary: list = []
    reader = text_file.read()
    reader.replace(".", "")
    word_list: list = reader.split(" ")



    frequencies = Counter(word_list)
    removed_keys: list = []
    for word in frequencies:
        if frequencies[word] <= 1:
            removed_keys.append(word)

        elif word.lower() == "the" or word.lower() == "of":
            print(word)

    for deleted_key in removed_keys:
        remove_keys(deleted_key)

    print(frequencies)
"""

# Sentence structure approach

useless_words: list = ["a", "the", "an"]

with open("test_textfile.txt", "r") as file:
    reader = file.read()
    reader = reader.replace("a.k.a.", "")
    sentences: List[str] = reader.split(".")
    for x in sentences:
        if x.startswith(" ") or x.endswith(" "):

            index_num = sentences.index(x)
            sentences[index_num] = x.strip()
            print("yeey")

            print(sentences)




