import sys
from collections import defaultdict

sys.stdin.readline()
my_results = defaultdict(int)


def add_contact(contact):
    for index, _ in enumerate(contact):
        my_contact = contact[0:index]
        my_results[my_contact] +=1


for line in sys.stdin.readlines():
    operation, contact = line.strip().split(' ')

    if operation == 'add':

        map(add_contact, contact)
    else:
        print(my_results[contact])

