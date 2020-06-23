from sys import argv
import csv
from cs50 import SQL

#Input condition
if len(argv) != 2:
    print("Usage: python import.py data.csv ")
    exit(1)

#Open the SQL file to save data
db = SQL("sqlite:///students.db")

#Open csv file
with open(argv[1],"r") as csvdata:

    reader = csv.DictReader(csvdata, delimiter = ",")

    #Iterate to each column
    for row in reader:
        name = row['name'].split()

        if len(name) ==2:
            first = name[0]
            middle = None
            last = name[1]

        if len(name) ==3:
            first = name[0]
            middle = name[1]
            last = name[2]

        house = row['house']
        birth = int(row['birth'])


        db.execute("INSERT INTO students(first,middle,last,house,birth) VALUES(?,?,?,?,?)",
                    first,middle,last,house,birth)

