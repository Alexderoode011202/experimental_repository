"""This program attempts to create summaries from larger bodies of text.
We try to recognize the program by paying special attention to the first and last sentence of each paragraph,
as well as focussing on often recurring nouns.
I still need to learn a bit more about paragraph structure.
What happens in the first half is that we split the article up into the paragraphs.
And We split those paragraphs up in lists of sentences, with each list containing the sentences of that particular
paragraph.
There still is quite a lot to be done to get something good out of this.
We can also take out sentences which don't contain any keywords
"""

import re
import collections
with open("../nu.nl_file") as file:
    reader = file.read()

    # Here we split the article up into paragraphs
    paragraphs: list = reader.split("\n")
    for x in paragraphs:
        print("---------\n{}".format(x))

    # With the paragraphs of the text seperated
    # We go and get the first and last sentence of each paragraph:
    paragraphs_sentences: list = []
    for par in paragraphs:
        paragraphs_sentences.append(par.split(". "))

    print(paragraphs_sentences)

    print("\n\n---------\n---------")


    # And here we look at each individual sentences of the paragraphs
    for sentence in paragraphs_sentences:

        if sentence[0] == sentence[-1]:
            continue

        if "vuurwerk" in sentence[0]:
            print(sentence[0])

        if "vuurwerk" in sentence[-1]:
            print(sentence[-1])


