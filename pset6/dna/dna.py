from sys import argv
import csv

if len(argv) != 3:
    print("Usage: python dna.py data.csv sequence.txt")
    exit(1)

filedata = open(argv[1],'r')
filetext = open(argv[2],'r')

def max_number(s,sub):
    ans = [0] * len(s)
    for i in range(len(s) - len(sub), -1, -1):
        if s[i: i + len(sub)] == sub:
            if i + len(sub) > len(s) -1:
                ans[1] = 1
            else:
                ans[i] = 1 + ans[i + len(sub)]
    return max(ans)

def print_match(reader,actual):
    for line in reader:
        person = line[0]
        values = [int(val) for val in line[1:]]
        if values == actual:
            print(person)
            return
    print("No match")


with filedata as csv_file:
    reader = csv.reader(csv_file)
    sequences = next(reader)[1:]


    with filetext as txt_file:
        s = txt_file.read()
        actual = [max_number(s,seq) for seq in sequences]


    print_match(reader,actual)