import re

# 3. Similar to lesson3, exercise4 write a function that normalizes a MAC address to the following format:
def mac_normalize(mac_addr):
# 01:23:45:67:89:AB

# This function should handle the lower-case to upper-case conversion.
    mac_addr = mac_addr.upper()
    delimiter = re.search(r"[^A-F^0-9]{1}", mac_addr).group()
    mac_addr_parts = mac_addr.split(delimiter)

# It should also handle converting from '0000.aaaa.bbbb' and from '00-00-aa-aa-bb-bb' formats.
    if len(mac_addr_parts)<4:
        new = []
        for part in mac_addr_parts:
            new.append(part[:2])
            new.append(part[2:])
        mac_addr_parts = new

# Single digit bytes should be zero-padded to two digits. In other words, this:
# a:b:c:d:e:f
# should be converted to:
# 0A:0B:0C:0D:0E:0F
    if len(mac_addr_parts)>3:
        for i in range(len(mac_addr_parts)):
            if len(mac_addr_parts[i])<2:
                mac_addr_parts[i] = '0'+mac_addr_parts[i]
    
# The function should have one parameter, the mac_address. It should return the normalized MAC address
    return(":".join(mac_addr_parts))

# Write several test cases for your function and verify it is working properly.
print(mac_normalize('1:1:1:1:1:1'))
print(mac_normalize('1234.abcd.6789'))
print(mac_normalize('00-00-aa-aa-bb-bb'))
print(mac_normalize('a:b:c:d:e:f'))
print(mac_normalize('01:23:45:67:89:AB'))

