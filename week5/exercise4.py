# Copy your solution from exercise3 to exercise4. Add an 'import pdb' and pdb.set_trace() statement outside of your function (i.e. where you have your function calls).
# Inside of pdb, experiment with:
# Listing your code.
# Using 'next' and 'step' to walk through your code. Make sure you understand the difference between next and step.
# Experiment with 'up' and 'down' to move up and down the code stack.
# Use p <variable> to inspect a variable.
# Set a breakpoint and run your code to the breakpoint.
# Use '!command' to change a variable (for example !new_mac = [])

import re

def mac_normalize(mac_addr):

    mac_addr = mac_addr.upper()
    delimiter = re.search(r"[^A-F^0-9]{1}", mac_addr).group()
    mac_addr_parts = mac_addr.split(delimiter)

    if len(mac_addr_parts)<4:
        new = []
        for part in mac_addr_parts:
            new.append(part[:2])
            new.append(part[2:])
        mac_addr_parts = new

    if len(mac_addr_parts)>3:
        for i in range(len(mac_addr_parts)):
            if len(mac_addr_parts[i])<2:
                mac_addr_parts[i] = '0'+mac_addr_parts[i]
    
    return(":".join(mac_addr_parts))

import pdb
pdb.set_trace()

print(mac_normalize('1:1:1:1:1:1'))
print(mac_normalize('1234.abcd.6789'))
print(mac_normalize('00-00-aa-aa-bb-bb'))
print(mac_normalize('a:b:c:d:e:f'))
print(mac_normalize('01:23:45:67:89:AB'))

