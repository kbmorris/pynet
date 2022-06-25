#! /usr/bin/env python3

from pprint import pprint


with open('.\\week2\\show_arp.txt') as f:
    arp_output = f.readlines()[1::]

pprint(arp_output)

arp_output.sort()

pprint(arp_output)

arp_entries = arp_output[:3]
arp_entries = ''.join(arp_entries)

with open('.\\week2\\arp_entries.txt','w') as f:
    f.write(arp_entries)

