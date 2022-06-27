#! /usr/bin/env python3

import re
from pprint import pprint

SPLIT_FIELDS_RE = r'\s{2,}'
FIELDS = ['protocol','ip_addr','age','mac_addr','type','interface']
IPAM = {'10.220.88.1': 'Default gateway',
        '10.220.88.30': 'Arista3'}

with open('.\\week3\\show_arp.txt') as f:
    output = f.read().splitlines()

arp_entries = []

for line in output[1:]:
    data = re.split(SPLIT_FIELDS_RE,line)
    arp_entry = dict(zip(FIELDS,data))
    arp_entries.append(arp_entry)

for arp_entry in arp_entries:
    if arp_entry['ip_addr'] in IPAM.keys():
        print(f"{IPAM[arp_entry['ip_addr']]} IP/Mac is {arp_entry['ip_addr']}")
        