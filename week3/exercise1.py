#! /usr/bin/env python3
import re
from pprint import pprint

SHOW_VLAN_RE = r'^([0-9]{1,4})\s{1,6}([^\s]{1,32})\s{1,32}.*'

with open('.\\week3\\show_vlan.txt') as f:
    output = f.read().splitlines()

vlans = []
for line in output:
    results = re.search(SHOW_VLAN_RE,line)
    if results == None:
        continue
    vlans.append(results.groups())

pprint(vlans)