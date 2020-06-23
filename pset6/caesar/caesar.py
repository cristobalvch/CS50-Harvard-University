from sys import argv
from cs50 import get_string


if len(argv) !=2:
    print('Usage: ./caesar ley')
    exit(1)

key = int(argv[1])
plaintext = get_string("plaintext: ")

for i in range(len(plaintext)):
    c = plaintext[i]
    if c.isalpha():
        m ='A'
    elif c.islower():
        m = 'a'
        print("{}".format((c-m+key))
    else:

        print(c)

