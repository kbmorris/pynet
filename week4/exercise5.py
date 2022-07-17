import re
# Read the 'show_ipv6_intf.txt' file.
with open("week4/show_ipv6_intf.txt") as f:
    output = f.read()

# From this file, use Python regular expressions to extract the two IPv6 addresses.
# Try to use re.DOTALL flag as part of your search. Your search pattern should not include any of the literal characters in the IPv6 address.
ip_address_string = re.search("IPv6 address:\s*(.*)\s*IPv6 subnet:", output, re.DOTALL).group(1)

# The two relevant IPv6 addresses you need to extract are:
#     2001:11:2233::a1/24
#     2001:cc11:22bb:0:2ec2:60ff:fe4f:feb2/64
# From this, create a list of IPv6 addresses that includes only the above two addresses.
ip_addresses = re.findall("[0-9a-f:/]+", ip_address_string)

# Print this list to the screen.
print(ip_addresses)