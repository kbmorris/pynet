#! /usr/bin/env python3

import re


#  Read the 'show_lldp_neighbors_detail.txt' file. 
with open('.\\week3\\show_lldp_neighbors_detail.txt') as f:
    output = f.read().splitlines()

port_id = system_name = None

#  Loop over the lines of this file. 
for line in output: 

#  Keep reading the lines until you have encountered the remote "System Name" and remote "Port id". 
#  Save these two items into variables
    if m := re.search(r'^Port id: ([0-9]+)', line):
        port_id = m.group(1)
    elif m := re.search(r'System Name: (.*)', line):
        system_name = m.group(1)

#  Break out of your loop once you have retrieved these two items.
    if not port_id is None and not system_name is None:
        continue

#  print them to the screen.
print(f"Neighbor {system_name} is on port {port_id}.")
 