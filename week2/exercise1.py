#! /usr/bin/env python3

f = open('.\\week2\\show_version.txt')
output = f.read()
f.close()

print(output)
print(type(output))


with open('.\\week2\\show_version.txt') as f:

    output = f.readlines()

print(type(output))

