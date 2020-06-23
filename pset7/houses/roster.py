from sys import argv
from cs50 import SQL


if len(argv) != 2:
    print("Usage: python roster.py housename")
    exit(1)


db = SQL("sqlite:///students.db")

house = argv[1]
query = db.execute("SELECT first,middle,last,birth FROM students WHERE house=? ORDER BY last ASC;",house)


for row in query:

    if row['middle'] == None:
       names = row['first'] + ' '+ row['last']
    else:
        names = row['first'] + ' '+ row['middle'] + ' '+  row['last']

    birth = row['birth']

    print(f"{names}, born {birth}")
