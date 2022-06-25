#! /bin/usr/env python3

import ipaddress


addresses = []

addresses.append(ipaddress.ip_address('2.2.2.2'))
addresses.extend([ipaddress.ip_address('1.1.1.1'),ipaddress.ip_address('3.3.3.3')])
addresses = addresses + [ipaddress.ip_address('4.4.4.4'),ipaddress.ip_address('5.5.5.5')]

print('Printing IP Address List')
for address in addresses:
    print(address)
print('\n')

print(f"First address: {addresses[0]}")

print(f"Last address: {addresses[-1]}")

print('\nPopping first and last address.')
print(addresses.pop(0))
print(addresses.pop(-1))

addresses[0] = ipaddress.ip_address('2.2.2.2')

print('Printing IP Address List')
for address in addresses:
    print(address)
