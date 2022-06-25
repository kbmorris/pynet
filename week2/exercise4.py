#! /usr/bin/env python3

from pprint import pprint

with open('.\\week2\\show_ip_int_brief.txt') as f:
    output = f.readlines()

interfaces = []

fields = output[0].split()

for line in output[1:]:
    data = line.split()
    entry = dict(zip(fields, data))
    interfaces.append(entry)

for interface in interfaces:
    if interface['Interface'] == 'FastEthernet4':
        result = (interface['Interface'], interface['IP-Address'])


pprint(result)
