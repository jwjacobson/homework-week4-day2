#! /usr/bin/python
import re

with open('./regex_test.txt') as file:
    data = file.readlines()

pattern = re.compile('([A-Z]\w+) ([A-Z]\w*)? ?([A-Z]\w+)')

for name in data:
    if pattern.search(name):
        print(name.rstrip())    # strip off the newlines to condense output
    else:
        print("None")

file.close()