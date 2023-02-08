import sqlite3 as sqlite
from tkinter import *

root = Tk()
specific_table: sqlite.Connection = None
def make_connection(database_name: str) -> None:
    """ Makes connection to the specific database"""

# Make the buttons
question: Label = Label(root, text="what is the name of your folder?", width=20, height=10)
answer_db: Entry = Entry(root, width=20)
answer_db.insert(0, "DB Name")
answer_table: Entry = Entry(root, width=2)
answer_table.insert(0, "Table Name")
confirmation: Button = Button(root, width=20, height=10, command= lambda x=answer_db.get(), y=answer_table.get(): ...)

# question
# answer_db
# Answer_table
# Confirmation

# Step 1: ask for input
# Step 2: connect to db
# step 3: connect to table
# step 4: offer client options
# step 5: do what the client asks


